from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from credit_app.utils import get_producer_ids


class ProducerIdsAPIView(APIView):
    def get(self, request, contract_id):
        try:
            producer_ids = get_producer_ids(contract_id)
            return Response(
                {"producer_ids": producer_ids}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
