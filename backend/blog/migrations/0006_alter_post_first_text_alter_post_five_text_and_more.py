# Generated by Django 5.1.2 on 2024-11-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_post_five_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="first_text",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="five_text",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="fourth_text",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="second_text",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="third_text",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]