import json
from django.core.management.base import BaseCommand
from insights.models import Insight

class Command(BaseCommand):
    help = 'Load JSON data into database'

    def handle(self, *args, **kwargs):
        with open('jsondata.json') as file:
            data = json.load(file)

            for item in data:
                Insight.objects.create(
                    intensity=item.get('intensity'),
                    likelihood=item.get('likelihood'),
                    relevance=item.get('relevance'),
                    year=item.get('start_year'),
                    end_year=item.get('end_year'),
                    country=item.get('country'),
                    city=item.get('city'),
                    region=item.get('region'),
                    topics=item.get('topic'),
                    sector=item.get('sector'),
                    pestle=item.get('pestle'),
                    source=item.get('source'),
                    swot=item.get('swot'),
                )

        self.stdout.write(self.style.SUCCESS('Data Loaded Successfully'))