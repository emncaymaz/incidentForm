from django.core.mail import EmailMessage
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import IncidentForm, AlwaysValidIncidentForm
from .models import Incident
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .settings.common import CC_CONTACT_EMAIL, CC_SENDER_EMAIL, CC_RECEIVER_EMAIL
from django.contrib import messages


def send_email(send_e_mail):
    if send_e_mail.request.method == 'POST' and 'send' in send_e_mail.request.POST and send_e_mail.get_form().is_valid():
        if 'send' in send_e_mail.request.POST:
            subject = f"{send_e_mail.request.user} hat ein Formular geschickt"
            sender = CC_SENDER_EMAIL
            recipients = [CC_RECEIVER_EMAIL]
            text_content = render_to_string('email/email.txt', {'incident': send_e_mail.object})
            msg = EmailMessage(subject, text_content, sender, recipients)
            msg.send()
           # messages.success(send_e_mail.request, f'Ihre Email ist mit Erfolg zu {recipients} gesendet')
    #else:
       # messages.add_message(send_e_mail.request, messages.ERROR,
          #             'Das Formular wurde nicht korrekt ausgefüllt.'
          #             'Bitte überprüfen Sie die einzelnen Felder noch einmal')
   # return reverse_lazy('home')


class FormViewPage(TemplateView):
    model = Incident
    template_name = 'incidentform/home.html'

    def get_context_data(self, **kwargs):
        context = super(FormViewPage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['object_list'] = Incident.objects.filter(user=self.request.user)
        return context


class IncidentFormPage(CreateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incidentform/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        send_email(self)
        return reverse_lazy('home')

    def get_form_class(self):
        if self.request.method == 'POST' and 'save' in self.request.POST:
            return AlwaysValidIncidentForm
        return IncidentForm


class IncidentFormUpdatePage(UpdateView):
    model = Incident
    form_class = IncidentForm
    template_name = 'incidentform/update.html'

    def get_success_url(self):
        send_email(self)
        return reverse_lazy('home')

    def get_form_class(self):
        if self.request.method == 'POST' and 'save' in self.request.POST:
            return AlwaysValidIncidentForm
        return IncidentForm


class IncidentFormDeletePage(DeleteView):
    model = Incident
    template_name = 'incidentform/delete.html'
    success_url = reverse_lazy('home')
