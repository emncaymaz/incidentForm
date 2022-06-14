from django.core.management.base import BaseCommand, CommandError
from incidentform.models import Incident
from datetime import datetime, timedelta
from incidentform.settings.common import DELETE_AFTER_TIME


class Command(BaseCommand):
    help = 'delete a form that has been over 14 days'

    def handle(self, *args, **options):
        try:
            incidents = Incident.objects.all()
            date_now = datetime.now().timestamp()
            incident_time = timedelta(DELETE_AFTER_TIME)
            for incident in incidents:
                created_date = incident.created_date
                incident_delete_date = (created_date + incident_time).timestamp()
                if incident_delete_date < date_now:
                    incident.delete()
                    self.stdout.write(self.style.SUCCESS('Incident is deleted'))
                else:
                    self.stdout.write(self.style.WARNING(f'delete_date is lees than '
                                        f'created_date for incident {incident.violation_name}'))
        except Incident.DoesNotExist:
            raise CommandError('Incident is not exist ')
