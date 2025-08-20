from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from paragraphs.serializers import ParagraphInputSerializer, ParagraphSerializer, WordSearchSerializer
from paragraphs.models import Paragraph, WordFrequency
from django.db.models import F
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView


"""
ParagraphInputView:
- Handles POST requests to input multiple paragraphs for the authenticated user.
- Splits input text into separate paragraphs by two newlines.
- Creates Paragraph objects for each paragraph.
- Updates or creates WordFrequency entries for each word in the paragraphs.
- Returns serialized data of created paragraphs.
"""
class ParagraphInputView(APIView):
	permission_classes = [IsAuthenticated]

	@extend_schema(
		request=ParagraphInputSerializer,
		responses={201: ParagraphSerializer(many=True)},
		description="Input multiple paragraphs separated by two newlines."
	)
	def post(self, request):
		serializer = ParagraphInputSerializer(data=request.data)
		if serializer.is_valid():
			paragraphs_text = serializer.validated_data['text']
			paragraphs = [p.strip() for p in paragraphs_text.split('\n\n') if p.strip()]
			created = []
			for para in paragraphs:
				p = Paragraph.objects.create(user=request.user, text=para)
				created.append(p)
				# token and update the words
				words = para.split()
				for word in words:
					freq_obj, _ = WordFrequency.objects.get_or_create(user=request.user, word=word)
					freq_obj.frequency = F('frequency') + 1
					freq_obj.save()
			return Response({'created': ParagraphSerializer(created, many=True).data}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
WordSearchView:
- Handles GET requests to search for a specific word in the authenticated user's paragraphs.
- Counts occurrences of the given word in each paragraph.
- Returns the top 10 paragraphs containing the word, sorted by frequency in descending order.
"""
import re

class WordSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.query_params.get('word')
        if not word:
            return Response({'error': 'word parameter is required'}, status=400)
        user_paragraphs = Paragraph.objects.filter(user=request.user)
        para_counts = []
        pattern = re.compile(r'\b{}\b'.format(re.escape(word)), re.IGNORECASE)
        for para in user_paragraphs:
            count = len(pattern.findall(para.text))
            if count > 0:
                para_counts.append({'paragraph': para, 'count': count})
        top = sorted(para_counts, key=lambda x: x['count'], reverse=True)[:10]
        return Response({'results': [
            {'id': x['paragraph'].id, 'text': x['paragraph'].text, 'count': x['count']} for x in top
        ]})

"""
ParagraphListView:
- Provides a list of all paragraphs created by the authenticated user.
- Uses ParagraphSerializer for serialization.
"""
class ParagraphListView(ListAPIView):
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Paragraph.objects.filter(user=self.request.user)

