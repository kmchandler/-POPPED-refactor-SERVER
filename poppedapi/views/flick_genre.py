from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Genre, Flick


class FlickGenreView(ViewSet):
    """Flick genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single flick genre

        Returns:
            Response -- JSON serialized flick genre
        """

        try:
            flick_genre = Flick_Genre.objects.get(pk=pk)
            serializer = FlickGenreSerializer(flick_genre)
            return Response(serializer.data)
        except Flick_Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all flick genres

        Returns:
            Response -- JSON serialized list of flick genres
        """
        flick_genres = Flick_Genre.objects.all()
        serializer =  FlickGenreSerializer(flick_genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick genre instance
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        flick_genre = Flick_Genre.objects.create(
            flick_id=flick,
            genre_id=request.data["genre_id"],
        )
        serializer = FlickGenreSerializer(flick_genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for flick_genre

        Returns:
            Response -- Empty body with 204 status code
        """

        flick_genre = Flick_Genre.objects.get(pk=pk)
        flick_genre.flick_id = request.data["flick_id"]
        flick_genre.genre_id = request.data["genre_id"]

        flick_genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all flicks"""
        flick_genre = Flick_Genre.objects.get(pk=pk)
        flick_genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FlickGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for Flick genres
    """
    class Meta:
        model = Flick_Genre
        fields = ('id', 'flick_id', 'genre_id')
