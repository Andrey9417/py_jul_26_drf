from django_filters import rest_framework as rest_filters

from messenger.models import Message


class MessageFilter(rest_filters.FilterSet):
    created_at = rest_filters.DateFromToRangeFilter()

    class Meta:
        model = Message
        fields = ["created_at"]
