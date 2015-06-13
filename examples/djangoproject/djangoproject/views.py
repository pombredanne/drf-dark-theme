from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class TestApiView(APIView):
    def get(self, request):
        data = {
            'string': 'Lorem impsum',
            'number': 1,
            'list': [1, 2, 3 ,4],
            'dict': {
                'a': 1,
                'b': 'b'
            }
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
