from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Mood, Flick, Mood


class FlickMoodView(ViewSet):
    """Flick mood view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single flick mood

        Returns:
            Response -- JSON serialized flick mood
        """

        try:
            flick_mood = Flick_Mood.objects.get(pk=pk)
            serializer = FlickMoodSerializer(flick_mood)
            return Response(serializer.data)
        except Flick_Mood.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all flick moods

        Returns:
            Response -- JSON serialized list of flick moods
        """
        flick_moods = Flick_Mood.objects.all()
        id_for_flick = request.query_params.get('flick', None)
        if id_for_flick is not None:
            flick_moods = flick_moods.filter(flick_id=id_for_flick)
        serializer =  FlickMoodSerializer(flick_moods, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick mood instance
        """

        print(request.data)
        flick = Flick.objects.get(id=request.data["flick_id"])
        mood = Mood.objects.get(id=request.data["mood_id"])
        flick_mood = Flick_Mood.objects.create(
            flick=flick,
            mood=mood,
        )
        serializer = FlickMoodSerializer(flick_mood)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for flick_mood

        Returns:
            Response -- Empty body with 204 status code
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        mood = Mood.objects.get(id=request.data["mood_id"])
        flick_mood = Flick_Mood.objects.get(pk=pk)
        flick_mood.flick = flick
        flick_mood.mood = mood

        flick_mood.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all flicks"""
        flick_mood = Flick_Mood.objects.get(pk=pk)
        flick_mood.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FlickMoodSerializer(serializers.ModelSerializer):
    """JSON serializer for Flick moods
    """
    class Meta:
        model = Flick_Mood
        fields = ('id', 'flick_id', 'mood_id')
