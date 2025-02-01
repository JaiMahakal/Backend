from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get("lang", "en")
        faqs = self.queryset
        for faq in faqs:
            faq.question = faq.get_translated_text(lang)
        return faqs
