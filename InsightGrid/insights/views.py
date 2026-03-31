from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Insight
from .serializers import InsightSerializer
from .filters import InsightFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from django.db.models import Count


def apply_insight_filters(queryset, params):
    """Apply filter params to Insight queryset. Params come from request.GET or request.data."""
    if end_year := params.get('end_year'):
        try:
            queryset = queryset.filter(end_year=int(end_year))
        except (ValueError, TypeError):
            pass
    if topics := params.get('topics'):
        queryset = queryset.filter(topics__icontains=topics)
    if sector := params.get('sector'):
        queryset = queryset.filter(sector__icontains=sector)
    if region := params.get('region'):
        queryset = queryset.filter(region__icontains=region)
    if pestle := params.get('pestle'):
        queryset = queryset.filter(pestle__icontains=pestle)
    if source := params.get('source'):
        queryset = queryset.filter(source__icontains=source)
    if swot := params.get('swot'):
        queryset = queryset.filter(swot__icontains=swot)
    if country := params.get('country'):
        queryset = queryset.filter(country__icontains=country)
    if city := params.get('city'):
        queryset = queryset.filter(city__icontains=city)
    return queryset


class InsightListView(generics.ListAPIView):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer
    filterset_class = InsightFilter


class CountryIntensityView(APIView):

    def get(self, request):
        qs = apply_insight_filters(Insight.objects.all(), request.query_params)
        data = (
            qs.values('country')
            .annotate(avg_intensity=Avg('intensity'))
            .order_by('-avg_intensity')
        )
        return Response(data)


class YearTrendView(APIView):

    def get(self, request):
        qs = apply_insight_filters(Insight.objects.all(), request.query_params)
        data = (
            qs.values('year')
            .annotate(avg_intensity=Avg('intensity'))
            .order_by('year')
        )
        return Response(data)


class TopicDistributionView(APIView):

    def get(self, request):
        qs = apply_insight_filters(Insight.objects.all(), request.query_params)
        data = (
            qs.values('topics')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        return Response(data)


class HeatMapView(APIView):
    """Returns country x year intensity matrix for heat map visualization."""

    def get(self, request):
        qs = apply_insight_filters(Insight.objects.all(), request.query_params)
        data = (
            qs.exclude(country__isnull=True)
            .exclude(country='')
            .exclude(year__isnull=True)
            .values('country', 'year')
            .annotate(avg_intensity=Avg('intensity'))
            .order_by('country', 'year')
        )
        return Response(list(data))


class InsightCSVExportView(APIView):
    """Export filtered insights as CSV."""

    def get(self, request):
        import csv
        from django.http import HttpResponse

        qs = apply_insight_filters(Insight.objects.all(), request.query_params)
        rows = qs.values(
            'intensity', 'likelihood', 'relevance', 'year', 'end_year',
            'country', 'city', 'region', 'topics', 'sector', 'pestle', 'source', 'swot'
        )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="insightgrid-export.csv"'
        writer = csv.writer(response)

        cols = ['intensity', 'likelihood', 'relevance', 'year', 'end_year', 'country', 'city', 'region', 'topics', 'sector', 'pestle', 'source', 'swot']
        writer.writerow(cols)
        for row in rows:
            writer.writerow([row.get(c) for c in cols])

        return response