from django.utils.translation import gettext as _
from .choices import *
from .models import Incident
from .validators import *

INCIDENT_WIDGETS = {
    'violation_start': forms.DateTimeInput(attrs={'placeholder': 'format: 12.12.2022 12:12'}),
    'violation_end': forms.DateTimeInput(attrs={'placeholder': 'format: 12.12.2022 12:12'}),
    'violation_time': forms.DateTimeInput(attrs={'placeholder': 'format: 12.12.2022 12:12'}),
    'processor_time': forms.DateTimeInput(attrs={'placeholder': 'format: 12.12.2022 12:12'}),
    'violation_name': forms.TextInput(attrs={'placeholder': 'Begriff des Verstoßes'}),
    'names_functions_third': forms.Textarea(
        attrs={'placeholder': _('Namen und Funktionen (z.B Verantwortliche, Provider)'), 'rows': 5}),
    'violation_description': forms.Textarea(
        attrs={'placeholder': _('Bitte beschreiben Sie, wie der Verstoß festgestell wurde'), 'rows': 5}),
    'description': forms.Textarea(
        attrs={'placeholder': _('Mit diesem Feld könen Sie o.g. Zeitpunkte erläutern'), 'rows': 5}),
    'incident_description': forms.Textarea(
        attrs={'placeholder': _('Bitte beschreiben Sie den Vorfall eingehend'), 'rows': 5}),
    'incident_reason': forms.Textarea(
        attrs={'placeholder': _('Bitte geben Sie den Grund des Vorfalls an'), 'rows': 5}),
    'record_affected_min': forms.TextInput(attrs={'placeholder': 'Min. betroffene Datensätze'}),
    'record_affected_max': forms.TextInput(attrs={'placeholder': 'Max. betroffene Datensätze'}),
    'other_people': forms.TextInput(
        attrs={'placeholder': 'Bitte geben sie an, welche anderen Personengruppen betroffen'}),
    'affected_person_min': forms.TextInput(attrs={'placeholder': 'Min. betroffene Person'}),
    'affected_person_max': forms.TextInput(attrs={'placeholder': 'Max. betroffene Person'}),
    'description_before_incident': forms.Textarea(
        attrs={'placeholder': _('Bitte beschreiben Sie welche Maßnahmen zur Vermeidung von Verstößen'
                                'vor dem Vorfall in Kraft waren'), 'rows': 5}),
    'potential_impact': forms.Textarea(attrs={'placeholder': _('Bitte beschreiben Sie, welche Auswirkungen der Verstoß haben kann'), 'rows': 5}),
    'description_after_incident': forms.Textarea(attrs={'placeholder': _('Bitte beschreiben Sie, welche Maßnahmen zur Abwehr und Beseitigung des Verstoßes ergriffen wurden'), 'rows': 5}),
    'incident_location': forms.TextInput(attrs={'placeholder': _('Ort eingeben')}),
    'files': forms.ClearableFileInput(attrs={'placeholder': _('Zusätzliche Anlagen beifügen'), 'multiple': True}),


}


class AlwaysValidIncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'
        exclude = ('user',)
        widgets = INCIDENT_WIDGETS


class IncidentForm(forms.ModelForm):
    severity_potential_impact = forms.ChoiceField(choices=SEVERITY_POTENTIAL_IMPACT, widget=forms.RadioSelect,
                                                  label=_('Die Betroffenen wurden unterrichtet'), required=False)

    class Meta:
        model = Incident
        fields = '__all__'
        exclude = ('user',)
        widgets = INCIDENT_WIDGETS

    def clean_violation_name(self):
        violation_name = self.cleaned_data.get('violation_name')
        if violation_name is None:
            raise forms.ValidationError('Bitte einen Name eingeben')
        return violation_name

    def clean_participation_of_third(self):
        participation_of_third = self.cleaned_data.get('participation_of_third')
        return participation_of_third

    def clean_names_functions_third(self):
        participation_of_third = self.cleaned_data.get('participation_of_third')
        names_functions_third = self.cleaned_data.get('names_functions_third')
        if participation_of_third is not None and names_functions_third == '':
            if 'yes' in participation_of_third:
                raise forms.ValidationError('Bitte geben Sie den Namen und die Funktionen der Dritten an')
        return names_functions_third

    def clean_violation_start(self):
        violation_start = self.cleaned_data.get('violation_start')
        if violation_start is None:
            raise forms.ValidationError('Bitte das Datum eingeben')
        if violation_start is not None:
            now = datetime.now().timestamp()
            date = violation_start.timestamp()
            if now < date:
                raise forms.ValidationError('Das Datum darf nicht größer als aktuelle Zeit sein')
        return violation_start

    def clean_violation_end(self):
        violation_end = self.cleaned_data.get('violation_end')
        violation_start = self.cleaned_data.get('violation_start')
        now = datetime.now().timestamp()
        if violation_end is None:
            raise forms.ValidationError('Bitte das Datum eingeben')
        if violation_end and violation_start is not None:
            if violation_start.timestamp() > violation_end.timestamp() or violation_end.timestamp() > now:
                raise forms.ValidationError(
                    'Die Endzeit darf nicht früher als die Anfangszeit sein und das Datum darf nicht später als die aktuelle Zeit sein')
        return violation_end

    def clean_violation_time(self):
        violation_end = self.cleaned_data.get('violation_end')
        violation_start = self.cleaned_data.get('violation_start')
        violation_time = self.cleaned_data.get('violation_time')
        print(violation_time)
        print(violation_end)
        print(violation_start)
        if violation_time is None:
            raise forms.ValidationError('Bitte das Datum eingeben')
        if violation_end and violation_start and violation_time is not None:
            if violation_time.timestamp() > violation_end.timestamp():
                raise forms.ValidationError('Die Zeit der Kenntnisnahme darf nicht später als die Endzeit sein')
            if violation_time.timestamp() < violation_start.timestamp():
                raise forms.ValidationError('die Zeit der Kenntnisnahme darf nicht früher als die Angangszeit sein')
        return violation_time

    def clean_violation_description(self):
        violation_description = self.cleaned_data.get('violation_description')
        if violation_description == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return violation_description

    def clean_processor_time(self):
        processor_time = self.cleaned_data.get('processor_time')
        if processor_time is None:
            raise forms.ValidationError('Bitte Datum eingeben')
        return processor_time

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return description

    def clean_protection_affected(self):
        protection_affected = self.cleaned_data.get('protection_affected')
        if not protection_affected:
            raise forms.ValidationError('Mindestens ein Schutziel auswählen')
        return protection_affected

    def clean_incident_type(self):
        incident_type = self.cleaned_data.get('incident_type')
        if not incident_type:
            raise forms.ValidationError('Mindestens einen Art auswählen')
        return incident_type

    def clean_incident_description(self):
        incident_description = self.cleaned_data.get('incident_description')
        if incident_description == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return incident_description

    def clean_incident_reason(self):
        incident_reason = self.cleaned_data.get('incident_reason')
        if incident_reason == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return incident_reason

    def clean_personal_data(self):
        personal_data = self.cleaned_data.get('personal_data')
        if not personal_data:
            raise forms.ValidationError('Mindestens eine Date auswählen')
        return personal_data

    def clean_record_affected_min(self):
        record_affected_min = self.cleaned_data.get('record_affected_min')
        if record_affected_min is None:
            raise forms.ValidationError('Bitte ausfüllen')
        return record_affected_min

    def clean_record_affected_max(self):
        record_affected_max = self.cleaned_data.get('record_affected_max')
        if not record_affected_max:
            raise forms.ValidationError('Bitte ausfüllen')
        return record_affected_max

    def clean_affected_people(self):
        affected_people = self.cleaned_data.get('affected_people')
        if not affected_people:
            raise forms.ValidationError('Mindestens eine Gruppe auswählen')
        return affected_people

    def clean_other_people(self):
        other_people = self.cleaned_data.get('other_people')
        affected_people = self.cleaned_data.get('affected_people')
        if other_people is None:
            return 'nicht pflicht'
        if affected_people is not None:
            if not affected_people:
                raise forms.ValidationError(
                    'Sie müssen dieses Feld ausfüllen, weil keine gültige Personengruppe ausgewählt wurde ')
        return other_people

    def clean_affected_person_min(self):
        affected_person_min = self.cleaned_data.get('affected_person_min')
        if not affected_person_min:
            raise forms.ValidationError('Bitte ausfüllen')
        return affected_person_min

    def clean_affected_person_max(self):
        affected_person_max = self.cleaned_data.get('affected_person_max')
        if not affected_person_max:
            raise forms.ValidationError('Bitte ausfüllen')
        return affected_person_max

    def clean_description_before_incident(self):
        description_before_incident = self.cleaned_data.get('description_before_incident')
        if description_before_incident == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return description_before_incident

    def clean_potential_impact(self):
        potential_impact = self.cleaned_data.get('potential_impact')
        if potential_impact == '':
            raise forms.ValidationError('Bitte ausfüllen')
        return potential_impact

    def clean_description_after_incident(self):
        description_after_incident = self.cleaned_data.get('description_after_incident')
        if len(description_after_incident) < 10:
            raise forms.ValidationError('bitte ausfüllen')
        return description_after_incident

    def clean_incident_location(self):
        incident_location = self.cleaned_data.get('incident_location')
        if incident_location is None:
            raise forms.ValidationError('Bitte ausfüllen')
        return incident_location

    def clean(self):
        data = super().clean()

        return data
