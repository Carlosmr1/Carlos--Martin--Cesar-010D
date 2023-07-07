# Generated by Django 4.1.9 on 2023-07-07 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_delete_tablegamesn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.marca')),
            ],
        ),
        migrations.RemoveField(
            model_name='videogames',
            name='marca',
        ),
        migrations.DeleteModel(
            name='Tablegames',
        ),
        migrations.DeleteModel(
            name='Videogames',
        ),
    ]
