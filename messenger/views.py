from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .tasks import send_msg_to_ext_system
from . import services
from .serializers import MessageCreateSerializer, MessageSerializer


class MessageApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        """Get message by id or list messages"""
        msg_id = request.query_params.get('id')
        if msg_id:
            msg_data = services.get_msg_by_id(msg_id)
            if not msg_data:
                return Response("Message is not exist", status=status.HTTP_400_BAD_REQUEST)
            msg_data = services.msg_is_read_mark(msg_id)
            serializer = self.serializer_class(msg_data)
            response_data = serializer.data
        else:
            msg_data = services.get_msg_list()
            if not msg_data:
                return Response("Message is not exist", status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(msg_data, many=True)
            response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Set message read flag"""
        response_data = {}
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        json_data = serializer.validated_data
        msg_id = request.query_params.get('id')
        if msg_id:
            msg_data = services.change_msg_data(msg_id, json_data)
            if not msg_data:
                return Response("Message is not exist", status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(msg_data)
            response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, *args, **kwargs):
        """Delete message by id"""
        msg_id = request.query_params.get('id')
        if msg_id:
            msg_data = services.delete_msg_by_id(msg_id)
            if not msg_data:
                return Response("Message is not exist", status=status.HTTP_400_BAD_REQUEST)
        return Response("Ok", status=status.HTTP_200_OK)


class MessageCreateApiView(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'create'

    @staticmethod
    def post(request, *args, **kwargs):
        """Create message"""
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_data = serializer.validated_data
        msg_id = services.create_message(post_data)
        if msg_id:
            send_msg_to_ext_system.delay(msg_id=msg_id)
        return Response("OK", status=status.HTTP_200_OK)
