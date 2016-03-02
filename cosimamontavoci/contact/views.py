import json
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.core.mail import mail_admins
from cosimamontavoci.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context


def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            # Imaginable form purpose. Post to admins.
            message = """From: %s <%s>\r\nMessage:\r\n%s\r\n""" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            mail_admins('Contact form', message)

            # Only executed with jQuery form request
            if request.is_ajax():
                return HttpResponse('OK')
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here 
                pass

            template = get_template('contact_template.html')
            context = Context({
                'contact_name': form['name'],
                'contact_email': form['email'],
                'form_content': form['message'],
            })
            content= template.render(context)

            email= EmailMessage("New contact form submission",
                                content,
                                "Cosima Montavoci" + " ",
                                ["lucabontempi@hotmail.it"],
                                headers= {'Reply-To': form.cleaned_data['email']})
            email.send()
            #return redirect('contact_form')
        else:
            if request.is_ajax():
                # Prepare JSON for parsing
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)

                return HttpResponseBadRequest(json.dumps(errors_dict))
            else:
                # render() form with errors (No AJAX)
                pass
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form':form})