# Generated by Django 3.2.9 on 2021-11-02 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MangaPreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('enlace_img', models.URLField()),
                ('enlace_manga', models.URLField()),
                ('generos', models.CharField(blank=True, max_length=255)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangas.proveedor')),
            ],
        ),
    ]
