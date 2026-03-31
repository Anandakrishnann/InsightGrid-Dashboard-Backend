import django_filters
from .models import Insight

class InsightFilter(django_filters.FilterSet):

    end_year = django_filters.NumberFilter(field_name='end_year')
    topics = django_filters.CharFilter(field_name='topics', lookup_expr='icontains')
    sector = django_filters.CharFilter(field_name='sector', lookup_expr='icontains')
    region = django_filters.CharFilter(field_name='region', lookup_expr='icontains')
    pestle = django_filters.CharFilter(field_name='pestle', lookup_expr='icontains')
    source = django_filters.CharFilter(field_name='source', lookup_expr='icontains')
    swot = django_filters.CharFilter(field_name='swot', lookup_expr='icontains')
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    class Meta:
        model = Insight
        fields = []