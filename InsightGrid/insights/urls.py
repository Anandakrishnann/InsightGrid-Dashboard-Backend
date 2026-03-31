from django.urls import path
from .views import *

urlpatterns = [
    path('insights/', InsightListView.as_view(), name='insights'),
    path('country-intensity/', CountryIntensityView.as_view(), name='country-intensity'),
    path('year-trend/', YearTrendView.as_view(), name='year-trend'),
    path('topic-distribution/', TopicDistributionView.as_view(), name='topic-distribution'),
    path('heatmap/', HeatMapView.as_view(), name='heatmap'),
    path('export/csv/', InsightCSVExportView.as_view(), name='export-csv'),
]