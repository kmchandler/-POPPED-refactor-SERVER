from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import User_Genre, User, Genre


class UserGenreView(ViewSet):
    """User genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single user genre

        Returns:
            Response -- JSON serialized user genre
        """

        try:
            user_genre = User_Genre.objects.get(pk=pk)
            serializer = UserGenreSerializer(user_genre)
            return Response(serializer.data)
        except User_Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all user genres

        Returns:
            Response -- JSON serialized list of user genres
        """
        user_genres = User_Genre.objects.all()
        id_for_user = request.query_params.get('userId', None)
        if id_for_user is not None:
            user_genres = user_genres.filter(user_id=id_for_user)

        serializer =  UserGenreSerializer(user_genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized user genre instance
        """
        user = User.objects.get(id=request.data["user_id"])
        genre = Genre.objects.get(id=request.data["genre_id"])
        user_genre = User_Genre.objects.create(
            user_id=user,
            genre_id=genre,
        )
        serializer = UserGenreSerializer(user_genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for user_genre

        Returns:
            Response -- Empty body with 204 status code
        """
        user = User.objects.get(id=request.data["user_id"])
        genre = Genre.objects.get(id=request.data["genre_id"])
        user_genre = User_Genre.objects.get(pk=pk)
        user_genre.user_id = user
        user_genre.genre_id = genre

        user_genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all user genres"""
        user_genre = User_Genre.objects.get(pk=pk)
        user_genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for user genres
    """
    class Meta:
        model = User_Genre
        fields = ('id', 'user_id', 'genre_id')
