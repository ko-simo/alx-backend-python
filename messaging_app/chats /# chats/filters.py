# chats/filters.py

import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    created_at__gte = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='gte')
    created_at__lte = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'created_at__gte', 'created_at__lte']
