from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")
    return value
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
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

# object level validation
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError("Title and About should be different")
        return data

# field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value

