# Generated by Django 4.2.4 on 2023-08-22 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='company_id',
        ),
        migrations.AddField(
            model_name='games',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='games.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='games',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.category'),
        ),
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='games',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='games',
            name='rate',
            field=models.SmallIntegerField(),
        ),
    ]
