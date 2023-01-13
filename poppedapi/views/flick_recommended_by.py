from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from poppedapi.models import Flick_Recommended_By


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
        serializer =  FlickRecommendedBySerializer(flick_recommended_bys, many=True)
        return Response(serializer.data)

class FlickRecommendedBySerializer(serializers.ModelSerializer):
    """JSON serializer for flick recommended by
    """
    class Meta:
        model = Flick_Recommended_By
        fields = ('id', 'flick_id', 'recommended_by')
