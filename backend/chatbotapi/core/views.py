from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import APIKey


# Create your views here.

# this defines the API endpoint


class GenerateAPIKeyView(APIView):
    def post(self, request):
        api_key = APIKey.objects.create()
        return Response({"api_key": str(api_key.key)}, status=status.HTTP_201_CREATED)


class ChatView(APIView):
    def post(self, request):
        api_key = request.headers.get("Authorization")
        user_input = request.data.get("message")
 
    # this checks if the API key is provided and valid
    # If not, it returns a 403 Forbidden response with an error message.
        if not APIKey.objects.filter(key=api_key).exists():
            return Response({"error": "Invalid API Key"}, status=403)

    #  If no message was provided in the request, it returns a 400 Bad Request.
        if not user_input:
            return Response({"error": "No message provided"}, status=400)

        reply = f"🤖 You said: {user_input}. I'm your assistant, how can I help?"

    # this returns a JSON response containing the reply message.
        return Response({"response": reply})
