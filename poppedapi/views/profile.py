from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import User_Genre, User, Genre
from .user import UserSerializer
from .user_genre import UserGenreSerializer

class ProfileView(ViewSet):
    def create(self, request):
        try:
            profileData = request.data
            checkedGenres = request.data['checkedGenre']

            user = User.objects.create(
                first_name=profileData["firstName"],
                last_name=profileData["lastName"],
                username=profileData["username"],
                image_url=profileData["imageUrl"],
                uid=profileData["uid"],
            )
            user_genres = [User_Genre(user_id=user, genre_id=Genre.objects.get(id=genre['id'])) for genre in checkedGenres]
            User_Genre.objects.bulk_create(user_genres)

            serializer = ProfileSerializer(user, user_genres)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class ProfileSerializer(serializers.Serializer):
    """"JSON serializer for user profile"""
    user = UserSerializer(required=False)
    user_genre = UserGenreSerializer(many=True)