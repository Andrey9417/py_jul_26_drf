from django.db import transaction
from rest_framework import serializers

from messenger.models import Message, Tag, MessageImage
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "text", "created_at")


class MessageCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        required=False,
        write_only=True,
    )

    class Meta:
        model = Message
        fields = ("id", "text", "images", "created_at")

    def create(self, validated_data):
        images = validated_data.pop("images", None)

        with transaction.atomic():
            message = Message.objects.create(**validated_data)
            if images:
                images = [
                    MessageImage(
                        message=message,
                        image=image,
                    )
                    for image in images
                ]
                MessageImage.objects.bulk_create(images)

        return message


class MessageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageImage
        fields = ("id", "image")


class MessageListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", allow_null=True)
    images = MessageImageSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = (
            "id",
            "created_at",
            "text_preview",
            "user",
            "images"
        )


class MessageDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "created_at", "text_preview", "text", "user")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
