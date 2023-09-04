# Generated by Django 4.2.4 on 2023-09-04 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailnetwork',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='goods.contact', verbose_name='Контакт'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='good',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='goods.good', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='goods.supplier', verbose_name='Поставщик'),
        ),
    ]
