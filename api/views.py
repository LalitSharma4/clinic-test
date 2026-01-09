from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 65000},
    {"id": 2, "name": "Phone", "price": 25000},
    {"id": 3, "name": "Tablet", "price": 30000},
]

class ProductListAPI(APIView):
    def get(self, request):
        id = request.query_params.get("id")

        if not id:

            serializer = ProductSerializer(PRODUCTS, many=True)
            return Response({
                "success": True,
                "data": serializer.data
            })
        else:
            product = next((item for item in PRODUCTS if item["id"] == int(id)), None)
            if product:
                serializer = ProductSerializer(product)
                return Response({
                    "success": True,
                    "data": serializer.data
                })
            

