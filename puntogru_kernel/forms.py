from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    text = forms.CharField()
    
    def clean(self):
        return self.cleaned_data