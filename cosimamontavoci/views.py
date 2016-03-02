from django.shortcuts import render, redirect
from cosimamontavoci.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
import random

def home(request):
    background_list=['jumbotron', 'jumbojumbo', 'jumbojumbojumbo']
    return render(request,'index.html', {'which_background': random.choice(background_list)})

def about(request):
    return render(request,'about.html')

def contact(request):
    form_class= ContactForm
    if request.method== 'POST':
        form= form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',''
            )
            contact_email = request.POST.get(
                'contact_email',''
            )
            form_content= request.POST.get(
                'content',''
            )

            template = get_template('contact_template.html')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content= template.render(context)

            email= EmailMessage("New contact form submission",
                                content,
                                "Cosima Montavoci" + " ",
                                ["lucabontempi@hotmail.it"],
                                headers= {'Reply-To': contact_email})
            email.send()
            return redirect('contact')
    return render(request,'contact.html', {'form':form_class})