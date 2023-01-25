from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Cast_Crew, Flick


class FlickCastCrewView(ViewSet):
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

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick cast crew instance
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        info = request.data["cast_crew"].split(',')

        for x in info:
            flick_cast_crew = Flick_Cast_Crew.objects.create(
            flick_id=flick,
            cast_crew=x,
            )

        serializer = FlickCastCrewSerializer(flick_cast_crew)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for flick_cast_crew

        Returns:
            Response -- Empty body with 204 status code
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        flick_cast_crew = Flick_Cast_Crew.objects.get(pk=pk)
        flick_cast_crew.flick_id = flick
        flick_cast_crew.cast_crew = request.data["cast_crew"]

        flick_cast_crew.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all flick cast crews"""
        flick_cast_crew = Flick_Cast_Crew.objects.get(pk=pk)
        flick_cast_crew.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FlickCastCrewSerializer(serializers.ModelSerializer):
    """JSON serializer for flick cast crew
    """
    class Meta:
        model = Flick_Cast_Crew
        fields = ('id', 'flick_id', 'cast_crew')
