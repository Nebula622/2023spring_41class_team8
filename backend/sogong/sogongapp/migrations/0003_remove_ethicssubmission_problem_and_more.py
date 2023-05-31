# Generated by Django 4.2.1 on 2023-05-31 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sogongapp", "0002_remove_user_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="ethicssubmission", name="problem",),
        migrations.RemoveField(model_name="ethicssubmission", name="user",),
        migrations.RenameField(
            model_name="codingproblem", old_name="answer", new_name="gpt_answer",
        ),
        migrations.DeleteModel(name="CodingSubmission",),
        migrations.DeleteModel(name="EthicsSubmission",),
    ]