from rest_framework import serializers
from watchlist_app.models import (Review, WatchList,
 StreamPlatform)

class ReviewSerializer(serializers.ModelSerializer):
# add reviews from this serializer
    class Meta:
        model = Review
        exclude = ('watchlist',)

        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # custom field that is not inside our Model or View
    # len_name = serializers.SerializerMethodField()
    # this is a get field, reading only
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"

        # fields = ['id', 'name', 'about']
        # exclude = ['id']
class StreamPlatformSerializer(serializers.ModelSerializer):
# "watchlist" has been defined in models.py,
# therefore we using it as a variable
# this shows all the details like timestamp, platform etc
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    # this shows just the name of the movie
    #  watchlist = serializers.StringRelatedField(many=True)
    
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = 'movie-detail'
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     about = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # instance has old value and 
#         # validated_data has new/updated value
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# # object level validation
#     def validate(self, data):
#         if data['name'] == data['about']:
#             raise serializers.ValidationError("Title and About should be different")
#         return data

# field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value

