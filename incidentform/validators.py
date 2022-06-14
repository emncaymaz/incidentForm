from django import forms
from datetime import datetime


def check_description_after_incident(self):
    description_after_incident = self.cleaned_data.get('description_after_incident')
    if len(description_after_incident) < 10:
        raise forms.ValidationError('bitte ausfüllen')
    return description_after_incident


def check_violation_start(self):
    violation_start = self.cleaned_data.get('violation_start')
    if violation_start is None:
        raise forms.ValidationError('Bitte ausfüllen')
    if violation_start is not None:
        now = datetime.now().timestamp()
        date = violation_start.timestamp()
        if now < date:
            raise forms.ValidationError('Datum darf nicht größer als aktuelle Zeit')
    return violation_start


def check_violation_end(self):
    violation_end = self.cleaned_data.get('violation_end')
    violation_start = self.cleaned_data.get('violation_start')
    now = datetime.now().timestamp()
    if violation_end and violation_start is not None:
        if violation_start.timestamp() > violation_end.timestamp() or violation_end.timestamp() > now:
            raise forms.ValidationError(
                'Datum des Endes des Verstoßes darf nicht kleiner als Datum des Anfangs des Verstoßes sein oder Datum darf nicht größer als aktuelle Zeit')
    return violation_end


def clean_description_before_incident(self):
    description_before_incident = self.cleaned_data.get('description_before_incident')
    if description_before_incident is '':
        raise forms.ValidationError('Bitte ausfüllen')
