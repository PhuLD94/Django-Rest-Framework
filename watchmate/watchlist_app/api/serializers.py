from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    def get_len_name(self, object): #Create a new field in api called len_name
        return len(object.title)

    def validate_name(self, value): #Validate name field
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
#
    def validate(self, data): #Object level validation
        if data['title'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different!")
        return data

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')

    class Meta:
        model = StreamPlatform
        fields = '__all__'

# def name_lenth(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_lenth()])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         return instance
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different!")
#         return data