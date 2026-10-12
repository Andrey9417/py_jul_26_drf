from rest_framework import viewsets, filters
from django_filters import rest_framework as rest_filters

from messenger.filters import MessageFilter
from messenger.models import Message, Tag
from messenger.pagination import MessagePagination
from messenger.serializers import MessageSerializer, TagSerializer, MessageListSerializer, MessageDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user")
    serializer_class = MessageSerializer
    filter_backends = [
        filters.SearchFilter,
        rest_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["text", "user__username"]
    filterset_class = MessageFilter
    ordering_fields = ["created_at"]
    pagination_class = MessagePagination

    def get_serializer_class(self):
        match self.action:
            case "list":
                return MessageListSerializer
            case "retrieve":
                return MessageDetailSerializer
            case _:
                return MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
