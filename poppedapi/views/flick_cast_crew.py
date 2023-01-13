from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Cast_Crew


class FlickGenreView(ViewSet):
    """Flick cast crew"""

    def retrieve(self, request, pk):
        """Handle GET requests for single flick cast crew

        Returns:
            Response -- JSON serialized flick cast crew
        """

        try:
            flick_cast_crew = Flick_Cast_Crew.objects.get(pk=pk)
            serializer = FlickCastCrewSerializer(flick_cast_crew)
            return Response(serializer.data)
        except Flick_Cast_Crew.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all flick cast crew

        Returns:
            Response -- JSON serialized list of flick cast crew
        """
        flick_cast_crews = Flick_Cast_Crew.objects.all()
        serializer =  FlickCastCrewSerializer(flick_cast_crews, many=True)
        return Response(serializer.data)

class FlickCastCrewSerializer(serializers.ModelSerializer):
    """JSON serializer for flick cast crew
    """
    class Meta:
        model = Flick_Cast_Crew
        fields = ('id', 'flick_id', 'cast_crew')
