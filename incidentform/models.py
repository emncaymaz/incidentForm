from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _
from .choices import *


class Incident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    violation_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Begriff des Verstoßes'))
    participation_of_third = MultiSelectField(choices=PARTICIPATION_OF_THIRD, blank=True, null=True, verbose_name=_('Ist wenigstens ein Dritter außerhalb des Verantwortlichen am betroffenen Dienst beteiligt?'))
    names_functions_third = models.TextField(null=True, blank=True, verbose_name=_('Namen und Funktionen der Dritten'))
    violation_start = models.DateTimeField(null=True, blank=True, verbose_name=_('Start des Verstoßes'))
    violation_end = models.DateTimeField(null=True, blank=True, verbose_name=_('Ende des Verstoßes'))
    violation_time = models.DateTimeField(null=True, blank=True, verbose_name=_('Zeitpunkt der Kenntnisnahme des Verstoßes'))
    violation_description = models.TextField(blank=True, null=True, verbose_name=_('Wie wurde der Verstoß festgestellt?'))
    processor_time = models.DateTimeField(null=True, blank=True, verbose_name=_('Zeitpunkt der Information durch den Auftragsverarbeiter'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Erläuterungen'))

    # 3. breach details
    protection_affected = MultiSelectField(blank=True, null=True, choices=PROTECTION_AFFECTED, verbose_name=_('Betroffene Schutzziele'))
    incident_type = MultiSelectField(max_length=255, blank=True, null=True, choices=INCIDENT_TYPE, verbose_name=_('Art des Vorfalls'))
    incident_description = models.TextField(blank=True, null=True, verbose_name=_('Beschreibung des Vorfalls'))
    incident_reason = models.TextField(blank=True, null=True, verbose_name=_('Grund des Vorfalls'))

    # 4. about the data concerned
    personal_data = MultiSelectField(max_length=255, blank=True, null=True, choices=PERSONAL_DATA, verbose_name=_('Betroffene Kategorien personenbezogener Daten'))
    record_affected_min = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Mindestanzahl der betroffenen Datensätze'))
    record_affected_max = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Höchstzahl der betroffenen Datensätze'))

    # 5. abot the data subjects
    affected_people = MultiSelectField(choices=AFFECTED_PEOPLE, blank=True, null=True, verbose_name=_('Betroffene Personengruppe'))
    other_people = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Beschreibung „anderer“ betroffener Gruppen'))
    affected_person_min = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Mindestanzahl der betroffenen Personen'))
    affected_person_max = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Maxdestanzahl der betroffenen Personen'))
    # 6. Pre incident actions
    description_before_incident = models.TextField(null=True, blank=True, verbose_name=_('Beschreibung ergriffener Maßnahmen vor dem Vorfall'))

    # 7. Consequences
    potential_impact = models.TextField(null=True, blank=True, verbose_name=_('Beschreibung der möglichen Auswirkungen auf die Betroffenen'))
    severity_potential_impact = models.CharField(max_length=255, blank=True, null=True, choices=SEVERITY_POTENTIAL_IMPACT, verbose_name=_('Schwere der möglichen Auswirkungen'))

    # 8.1 Measures intended and implemented
    affected_informed = MultiSelectField(max_length=255, blank=True, null=True, choices=AFFECTED_INFORMED, verbose_name=_('Die Betroffenen wurden unterrichtet'))

    # 8.2 Measures after the incident
    description_after_incident = models.TextField(null=True, blank=True, verbose_name=_('Beschreibung ergriffener Maßnahmen nach dem Vorfall'))
    incident_location = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Wo wurde den Vorfall gemeldet'))

    # 9. Include additional attachments
    files = models.FileField(upload_to='incidentform/', blank=True, null=True, verbose_name=_('Zusätzliche Anlagen beifügen'))
    # speak with dennis
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.violation_name

    class Meta:
        verbose_name = _('Sicherheitvorfall')
        verbose_name_plural = _('Sicherheitvorfälle')
        ordering = [_('-created_date')]

