from rest_framework import serializers
from .models import countries,categories,platforms,Game,Profile,News,Comment
from django.contrib.auth.models import User


class countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields= '__all__'

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'
class platformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = platforms
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
