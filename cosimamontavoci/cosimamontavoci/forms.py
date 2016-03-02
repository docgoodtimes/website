from django import forms

class ContactForm(forms.Form):
    name= forms.CharField(required=True)
    email= forms.EmailField(required=True)
    message= forms.CharField(
        required=True,
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args,**kwargs)
        self.fields['name'].label = "Your name:"
        self.fields['email'].label = "Your email:"
        self.fields['message'].label="Your message:"


###########
# http://stackoverflow.com/questions/8474409/django-forms-and-bootstrap-css-classes-and-divs
###########