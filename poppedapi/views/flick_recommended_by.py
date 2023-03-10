from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Recommended_By, Flick


class FlickRecommendedByView(ViewSet):
    """Flick recommended by"""

    def retrieve(self, request, pk):
        """Handle GET requests for single flick recommended by

        Returns:
            Response -- JSON serialized flick recommended by
        """

        try:
            flick_recommended_by = Flick_Recommended_By.objects.get(pk=pk)
            serializer = FlickRecommendedBySerializer(flick_recommended_by)
            return Response(serializer.data)
        except Flick_Recommended_By.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all flick recommended by

        Returns:
            Response -- JSON serialized list of flick recommended by
        """
        flick_recommended_bys = Flick_Recommended_By.objects.all()

        id_for_flick = request.query_params.get('flick', None)
        if id_for_flick is not None:
            flick_recommended_bys = flick_recommended_bys.filter(flick=id_for_flick)

        serializer =  FlickRecommendedBySerializer(flick_recommended_bys, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized flick recommended by instance
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        recommended_by = request.data["recommended_by"]

        flick_recommended_by= Flick_Recommended_By.objects.create(flick=flick, recommended_by=recommended_by)

        serializer = FlickRecommendedBySerializer(flick_recommended_by)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for flick_recommended_by

        Returns:
            Response -- Empty body with 204 status code
        """
        flick = Flick.objects.get(id=request.data["flick_id"])
        flick_recommended_by = Flick_Recommended_By.objects.get(pk=pk)
        flick_recommended_by.flick_id = flick
        flick_recommended_by.recommended_by = request.data["recommended_by"]

        flick_recommended_by.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handle delete requests for all flicks"""
        flick_recommended_by = Flick_Recommended_By.objects.get(pk=pk)
        flick_recommended_by.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FlickRecommendedBySerializer(serializers.ModelSerializer):
    """JSON serializer for flick recommended by
    """
    class Meta:
        model = Flick_Recommended_By
        fields = ('id', 'flick_id', 'recommended_by')
