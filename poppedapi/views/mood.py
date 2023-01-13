from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Mood

class MoodView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single mood
        """
        try:    
            mood = Mood.objects.get(pk=pk)
            serializer = MoodSerializer(mood)
            return Response(serializer.data)
        except Mood.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
 
    def list(self, request):
        """"Handle GET requests for all moods"""
        moods = Mood.objects.all()

        serializer = MoodSerializer(moods, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized mood instance
        """
        mood = Mood.objects.create(
            id=request.data["id"],
            mood_name=request.data["mood_name"]
        )
        serializer = MoodSerializer(mood)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a mood

        Returns:
            Response -- Empty body with 204 status code
        """

        mood = Mood.objects.get(pk=pk)
        mood.mood_name = request.data["mood_name"]

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all moods"""
        mood = Mood.objects.get(pk=pk)
        mood.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class MoodSerializer(serializers.ModelSerializer):
    """"JSON serializer for moods"""
    class Meta:
        model = Mood
        fields = ('id', 'mood_name')
