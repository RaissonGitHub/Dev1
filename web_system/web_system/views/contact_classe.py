from django.shortcuts import render
from django.views import View
from web_system.forms import ContactForm


class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm()
        context = {
            'form': form,
            'url_form': 'class_contact',
        }
        return render(request, 'contact/page_contact.html', context)
    
    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            sender = form.cleaned_data.get("sender")
            cc_myself = form.cleaned_data.get("cc_myself")
            print("Subject:", subject)
            recipients = ['2024010481@aluno.restinga.ifrs.edu.br']
            if cc_myself:
                recipients.append(sender)
            # chamada para eviar e-mail
            # send_mail(subject, message, sender, recipients)
            context = {
                'recipientes': recipients,
                'form': form,
            }
            return render(request, 'contact/thanks.html', context)