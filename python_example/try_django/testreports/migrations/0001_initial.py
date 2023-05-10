# Generated by Django 3.2 on 2023-05-10 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testservers', '0001_initial'),
        ('testcases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=50, null=True)),
                ('run_step', models.IntegerField(choices=[(0, 'others'), (1, 'Prepare'), (2, 'Install'), (3, 'Testing'), (4, 'Finished'), (5, 'Aborted'), (6, 'Promoted'), (7, 'Blocked')], default=0)),
                ('run_status', models.BooleanField(default=True)),
                ('report_type', models.IntegerField(choices=[(0, 'others'), (1, 'presubmission'), (2, 'daily'), (3, 'weekly'), (4, 'release'), (5, 'manually')], default=0)),
                ('test_report_url', models.CharField(blank=True, max_length=256, null=True)),
                ('artifactory_url', models.CharField(blank=True, max_length=1024, null=True)),
                ('comment', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('requester', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('requester_ip', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('test_end_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCaseRun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase_name', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(choices=[(0, 'waiting'), (1, 'running'), (2, 'pass'), (3, 'failed'), (4, 'abort'), (5, 'timeout'), (6, 'regression')], default=0)),
                ('result', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('detail_url', models.CharField(default=None, max_length=255, null=True)),
                ('detail_file', models.FileField(max_length=5000, upload_to='test_case_run/')),
                ('testcase_run_type', models.IntegerField(choices=[(0, 'testrun'), (1, 'prepare'), (2, 'post')], default=0)),
                ('comment', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('test_case', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='testcase_run', to='testcases.testcases')),
                ('test_report', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testcase_run', to='testreports.testreports')),
                ('test_server', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='testcase_run', to='testservers.testservers')),
            ],
        ),
        migrations.CreateModel(
            name='ReportComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(blank=True, max_length=50, null=True)),
                ('component_value', models.CharField(blank=True, max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('test_report', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_component', to='testreports.testreports')),
            ],
        ),
    ]
