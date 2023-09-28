# Generated by Django 4.2.3 on 2023-09-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplement_store', '0006_slideshowimages_alter_user_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShowImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='static/supplement_store/images/slide_show_images/')),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='SlideShowImages',
        ),
    ]