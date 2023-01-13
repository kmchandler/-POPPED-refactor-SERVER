from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import User_Genre


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
        serializer =  UserGenreSerializer(user_genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized user genre instance
        """
        user_genre = User_Genre.objects.create(
            user_id=request.data["user_id"],
            genre_id=request.data["genre_id"],
        )
        serializer = UserGenreSerializer(user_genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for user_genre

        Returns:
            Response -- Empty body with 204 status code
        """

        user_genre = User_Genre.objects.get(pk=pk)
        user_genre.user_id = request.data["genre_id"]
        user_genre.genre_id = request.data["genre_id"]

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
