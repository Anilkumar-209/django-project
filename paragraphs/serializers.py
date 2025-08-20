from rest_framework import serializers
from .models import Paragraph


"""
serializes the paragraph model for api responses.
includes paragraph id, text content, and creation date.
"""
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at']



"""
handles the input for searching a specific word
across stored paragraphs.
"""
class WordSearchSerializer(serializers.Serializer):
    word = serializers.CharField()



"""
handles input for adding multiple paragraphs at once.
paragraphs should be separated by two newlines, and an
optional title can be provided.
"""
class ParagraphInputSerializer(serializers.Serializer):
    text = serializers.CharField(
        help_text="Multiple paragraphs separated by two newlines. Example: 'Para 1\\n\\nPara 2'"
    )
    title = serializers.CharField(required=False)



# serializer for search results with count
class ParagraphSearchResultSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()  # number of times the word appears

    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'count']
    