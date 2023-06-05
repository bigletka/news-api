from core.models import News

from rest_framework import serializers



class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'date', 'text']
        read_only_fields = ['date', 'text']

    def create(self, validated_data):
        return News.objects.create(**validated_data)
    