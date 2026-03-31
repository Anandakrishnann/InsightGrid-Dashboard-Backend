# Generated migration for DB indexes

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_alter_insight_options_insight_added_insight_end_year'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['country'], name='insights_country_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['year'], name='insights_year_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['topics'], name='insights_topics_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['sector'], name='insights_sector_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['region'], name='insights_region_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['end_year'], name='insights_end_year_idx'),
        ),
        migrations.AddIndex(
            model_name='insight',
            index=models.Index(fields=['country', 'year'], name='insights_country_year_idx'),
        ),
    ]
