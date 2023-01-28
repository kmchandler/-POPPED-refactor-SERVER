from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Genre, Flick, Genre


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
        id_for_flick = request.query_params.get('flick', None)
        if id_for_flick is not None:
            flick_genres = flick_genres.filter(flick=id_for_flick)

        serializer =  FlickGenreSerializer(flick_genres, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick genre instance
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        genre = Genre.objects.get(id=request.data["genre_id"])
        flick_genre = Flick_Genre.objects.create(
            flick=flick,
            genre=genre,
        )
        serializer = FlickGenreSerializer(flick_genre)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for flick_genre

        Returns:
            Response -- Empty body with 204 status code
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        genre = Genre.objects.get(id=request.data["genre_id"])
        flick_genre = Flick_Genre.objects.get(pk=pk)
        flick_genre.flick = flick
        flick_genre.genre = genre

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
