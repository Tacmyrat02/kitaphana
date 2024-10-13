# Generated by Django 4.1.3 on 2022-11-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='currentNumber',
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images/%m'),
        ),
        migrations.AlterField(
            model_name='record',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordsBook', to='base.book'),
        ),
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordsUser', to='base.card'),
        ),
    ]
