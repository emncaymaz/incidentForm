# Generated by Django 3.2.12 on 2022-03-08 13:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Begriff des Verstoßes')),
                ('participation_of_third', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('yes', 'Ja')], max_length=3, null=True, verbose_name='Ist wenigstens ein Dritter außerhalb des Verantwortlichen am betroffenen Dienst beteiligt?')),
                ('names_functions_third', models.TextField(blank=True, null=True, verbose_name='Namen und Funktionen der Dritten')),
                ('violation_start', models.DateTimeField(blank=True, null=True, verbose_name='Start des Verstoßes')),
                ('violation_end', models.DateTimeField(blank=True, null=True, verbose_name='Ende des Verstoßes')),
                ('violation_time', models.DateTimeField(blank=True, null=True, verbose_name='Zeitpunkt der Kenntnisnahme des Verstoßes')),
                ('violation_description', models.TextField(blank=True, null=True, verbose_name='Wie wurde der Verstoß festgestellt?')),
                ('processor_time', models.DateTimeField(blank=True, null=True, verbose_name='Zeitpunkt der Information durch den Auftragsverarbeiter')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Erläuterungen')),
                ('protection_affected', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('confidentiality', 'Vertraulichkeit'), ('integrity', 'Integrität'), ('availability', 'Verfügbarkeit')], max_length=38, null=True, verbose_name='Betroffene Schutzziele')),
                ('incident_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('device_lorS', 'Gerät/Datenträger verloren oder gestohlen'), ('doc_lorS', 'Dokumente verloren, gestohlen oder unsicher aufbewahrt (Papier)'), ('post_orS', 'Post (auch E-Mail) verloren oder geöffnet bevor sie zum Absender zurück kam'), ('hacking', 'Hacking, Malware (z.B. Ransomware) und/oder Phishing'), ('mail', 'Unrichtige Entsorgung personenbezogener Daten auf Papier'), ('incorrect', 'Unrichtige Entsorgung personenbezogener Daten auf Papier'), ('release', 'Unbeabsichtigte Veröffentlichung'), ('data', 'Daten falscher Betroffener im Kundenportal angezeigt'), ('recipient', 'Falscher Empfänger'), ('disclosure', 'Mündliche Bekanntgabe personenbezogener Daten')], max_length=255, null=True, verbose_name='Art des Vorfalls')),
                ('incident_description', models.TextField(blank=True, null=True, verbose_name='Beschreibung des Vorfalls')),
                ('incident_reason', models.TextField(blank=True, null=True, verbose_name='Grund des Vorfalls')),
                ('personal_data', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', (('identity', 'Identität von Betroffenen (Vornamen, Nachnamen, Geburtsdaten)'), ('contact', 'Kontaktdaten'), ('identification', 'Daten zur Identifikation'), ('eco_fin_data', 'Ökonomische Daten sowie Finanzdaten'), ('doc_cert', 'Amtliche Dokumente und Urkunden'), ('loc_mov', 'Standort- sowie Bewegungsdaten'))), ('Besondere Kategorien', (('gen_bio', 'Genetische oder biometrische Daten'), ('criminal', 'Daten über strafrechtliche Verurteilungen, Straftaten sowie Sicherungsmaßnahmen (z.B. Sicherungsverwahrung)'), ('ethnic', 'Daten über die ‚rassische‘ oder ethnische Herkunft'), ('opinion', 'Politische Meinung'), ('belief', 'Religiöse oder weltanschauliche Überzeugung'), ('affiliation', 'Gewerkschaftszugehörigkeit'), ('sex_life', 'Daten zum Sexualleben'), ('health', 'Gesundheitsdaten'), ('not_known', 'Noch nicht bekannt')))], max_length=255, null=True, verbose_name='Betroffene Kategorien personenbezogener Daten')),
                ('record_affected_min', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mindestanzahl der betroffenen Datensätze')),
                ('record_affected_max', models.CharField(blank=True, max_length=255, null=True, verbose_name='Höchstzahl der betroffenen Datensätze')),
                ('affected_people', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('employees', 'Beschäftigte'), ('user', 'Benutzer'), ('subscribers', 'Abonnenten'), ('student', 'Schülerinnen, Schüler sowie Studierende'), ('customer', 'Kunden (aktuelle und potenzielle)'), ('patients', 'Patienten'), ('minor', 'Minderjährige'), ('vulnerable', 'Schutzbedürftige Personen'), ('not_known', 'Noch nicht bekannt')], max_length=79, null=True, verbose_name='Betroffene Personengruppe')),
                ('other_people', models.CharField(blank=True, max_length=255, null=True, verbose_name='Beschreibung „anderer“ betroffener Gruppen')),
                ('affected_person_min', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mindestanzahl der betroffenen Personen')),
                ('affected_person_max', models.CharField(blank=True, max_length=255, null=True, verbose_name='Maxdestanzahl der betroffenen Personen')),
                ('description_before_incident', models.TextField(blank=True, null=True, verbose_name='Beschreibung ergriffener Maßnahmen vor dem Vorfall')),
                ('potential_impact', models.TextField(blank=True, null=True, verbose_name='Beschreibung der möglichen Auswirkungen auf die Betroffenen')),
                ('severity_potential_impact', models.CharField(blank=True, choices=[('slightly', 'Geringfügig'), ('limited', 'Begrenzt'), ('significant', 'Bedeutend'), ('maximum', 'Maximal')], default='slightly', max_length=255, null=True, verbose_name='Schwere der möglichen Auswirkungen')),
                ('affected_informed', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('yes', 'Ja'), ('taught', 'Nein, aber sie werden noch unterrichtet'), ('not_taught', 'Nein, sie werden nicht unterrichtet')], max_length=255, null=True, verbose_name='Die Betroffenen wurden unterrichtet')),
                ('description_after_incident', models.TextField(blank=True, null=True, verbose_name='Beschreibung ergriffener Maßnahmen nach dem Vorfall')),
                ('incident_location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Wo wurde den Vorfall gemeldet')),
                ('files', models.FileField(blank=True, null=True, upload_to='incidentform/', verbose_name='Zusätzliche Anlagen beifügen')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('incident', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sicherheitvorfall',
                'verbose_name_plural': 'Sicherheitvorfälle',
                'ordering': ['-created_date'],
            },
        ),
    ]