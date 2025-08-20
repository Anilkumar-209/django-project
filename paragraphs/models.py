from django.db import models
from django.contrib.auth.models import User



"""
represents a paragraph submitted by a specific user.
stores the paragraph text, the user who submitted it,
and the date/time it was created.
"""
class Paragraph(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paragraphs')
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Paragraph {self.id} by {self.user.username}"



"""
tracks how many times a specific word appears in all
paragraphs of a particular user. ensures each (user, word)
pair is unique to avoid duplicate counts.
"""
class WordFrequency(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='word_frequencies')
	word = models.CharField(max_length=100)
	frequency = models.PositiveIntegerField(default=0)

	class Meta:
		unique_together = ('user', 'word')

	def __str__(self):
		return f"{self.word}: {self.frequency} (User: {self.user.username})"
