from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.exchange_rate_service import ExchangeRateService


class ExchangeRateView(APIView):
    def get(self, request):
        base = request.query_params.get("base")
        target = request.query_params.get("target")

        if not base or not target:
            return Response(
                {"detail": "Missing 'base' or 'target' query parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            rate = ExchangeRateService.get_exchange_rate(base, target)
            return Response(rate, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": "Internal server error."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
