from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick, Flick_Mood, Flick_Genre

class FlickView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single flick
        """
        try:    
            flick = Flick.objects.get(pk=pk)
            serializer = FlickSerializer(flick)
            return Response(serializer.data)
        except Flick.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all flicks"""
        flicks = Flick.objects.all()

        flick_mood = request.query_params.get('mood', None)
        if flick_mood is not None:
            flicks = flicks.filter(mood_id=flick_mood)

        flick_genre = request.query_params.get('genre', None)
        if flick_genre is not None:
            flicks = flicks.filter(genre_id=flick_genre)

        serializer = FlickSerializer(flicks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick instance
        """
        flick_mood = Flick_Mood.objects.get(pk=request.data["flick_mood"])
        flick_genre = Flick_Genre.objects.get(pk=request.data["flick_genre"])

        flick = Flick.objects.create(
            title=request.data["title"],
            type=request.data["type"],
            watched=request.data["watched"],
            favorite=request.data["favorite"],
            image_url=request.data["image_url"],
            rating=request.data["rating"],
            uid=request.data["uid"],
            flick_mood = flick_mood,
            flick_genre = flick_genre
        )
        serializer = FlickSerializer(flick)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a flick

        Returns:
            Response -- Empty body with 204 status code
        """

        flick = Flick.objects.get(pk=pk)
        flick.title = request.data["title"]
        flick.type = request.data["type"]
        flick.watched = request.data["watched"]
        flick.favorite = request.data["favorite"]
        flick.image_url = request.data["image_url"]
        flick.rating = request.data["rating"]
        flick.uid = request.data["uid"]

        flick_genre = Flick_Genre.objects.get(pk=request.data["flick_genre"])
        flick.flick_genre = flick_genre
        flick.save()

        flick_mood = Flick_Mood.objects.get(pk=request.data["flick_mood"])
        flick.flick_mood = flick_mood
        flick.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all flicks"""
        flick = Flick.objects.get(pk=pk)
        flick.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class FlickSerializer(serializers.ModelSerializer):
    """"JSON serializer for flicks"""
    class Meta:
        model = Flick
        fields = ('id', 'title', 'type', 'watched', 'favorite', 'image_url', 'rating', 'uid')
        depth = 2
