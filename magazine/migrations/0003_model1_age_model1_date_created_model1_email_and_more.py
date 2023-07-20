from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("magazine", "0002_model1_model2_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="model1",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="model1",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="model1",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
        migrations.AddField(
            model_name="model1",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="model2",
            name="description",
            field=models.TextField(default="Default description"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="model2",
            name="image",
            field=models.ImageField(
                default="model2_images/default_image.jpg", upload_to="model2_images/"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="model2",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="model2",
            name="rating",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
