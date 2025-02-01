from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)

    def get_translated_text(self, lang_code):
        return getattr(self, f"question_{lang_code}", self.question)

    def __str__(self):
        return self.question
