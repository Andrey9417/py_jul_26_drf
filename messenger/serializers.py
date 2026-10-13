from rest_framework import serializers

from messenger.models import Message, Tag
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "text", "created_at", "user")


class MessageListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", allow_null=True)

    class Meta:
        model = Message
        fields = ("id", "created_at", "text_preview", "user")


class MessageDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "created_at", "text_preview", "text", "user")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
