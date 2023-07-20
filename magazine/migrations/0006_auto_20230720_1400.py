from django.db import migrations, models


def update_description_to_string(apps, schema_editor):
    Product = apps.get_model('magazine', 'Product')
    Product.objects.update(description='Default description')


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_model1_age_model1_date_created_model1_email_and_more'),
    ]

    operations = [
        migrations.RunPython(update_description_to_string),
    ]

