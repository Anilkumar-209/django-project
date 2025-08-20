from django.urls import path
from .views import ParagraphInputView, WordSearchView, ParagraphListView

# url patterns for paragraph-related endpoints
urlpatterns = [
    path('input/', ParagraphInputView.as_view(), name='paragraph_input'),  # endpoint for adding paragraphs
    path('search/', WordSearchView.as_view(), name='word_search'),  # endpoint for searching word occurrences
    path('', ParagraphListView.as_view(), name='paragraph_list'),  # endpoint for listing all paragraphs
]
