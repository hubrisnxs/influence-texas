# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-16 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import influencetx.core.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legislators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.DateTimeField(blank=True, null=True)),
                ('last', models.DateTimeField(blank=True, null=True)),
                ('passed_lower', models.DateTimeField(blank=True, null=True)),
                ('passed_upper', models.DateTimeField(blank=True, null=True)),
                ('signed', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('session', models.IntegerField()),
                ('chamber', models.CharField(choices=[('House', 'House'), ('Senate', 'Senate')], max_length=5)),
                ('bill_id', models.CharField(max_length=10)),
                ('openstates_bill_id', models.CharField(max_length=20)),
                ('openstates_updated_at', models.DateTimeField()),
                ('sponsors', models.ManyToManyField(related_name='bills_sponsored', to='legislators.Legislator')),
            ],
        ),
        migrations.CreateModel(
            name='SingleVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[(influencetx.core.constants.Vote('Y'), 'Yay'), (influencetx.core.constants.Vote('N'), 'Nay'), (influencetx.core.constants.Vote('O'), 'Other')], max_length=1)),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='legislators.Legislator')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='VoteTally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamber', models.CharField(choices=[('House', 'House'), ('Senate', 'Senate')], max_length=5)),
                ('session', models.IntegerField()),
                ('yes_count', models.IntegerField(default=0)),
                ('no_count', models.IntegerField(default=0)),
                ('other_count', models.IntegerField(default=0)),
                ('passed', models.BooleanField()),
                ('date', models.DateTimeField()),
                ('openstates_vote_id', models.CharField(db_index=True, max_length=20)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_results', to='bills.Bill')),
            ],
        ),
        migrations.AddField(
            model_name='singlevote',
            name='vote_tally',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='bills.VoteTally'),
        ),
        migrations.AddField(
            model_name='bill',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='bills', to='bills.SubjectTag'),
        ),
        migrations.AddField(
            model_name='actiondates',
            name='bill',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='action_dates', to='bills.Bill'),
        ),
    ]
