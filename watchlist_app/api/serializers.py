from rest_framework import serializers
from watchlist_app.models import Movie
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    about = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance has old value and 
        # validated_data has new/updated value
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
        
    