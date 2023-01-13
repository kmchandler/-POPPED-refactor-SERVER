from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Genre

class MoodView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single genre
        """
        try:    
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all genres"""
        genres = Genre.objects.all()

        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized genre instance
        """
        genre = Genre.objects.create(
            id=request.data["id"],
            genre_name=request.data["genre_name"]
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a genre

        Returns:
            Response -- Empty body with 204 status code
        """

        genre = Genre.objects.get(pk=pk)
        genre.genre_name = request.data["genre_name"]

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all genre"""
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class GenreSerializer(serializers.ModelSerializer):
    """"JSON serializer for genres"""
    class Meta:
        model = Genre
        fields = ('id', 'genre_name')
