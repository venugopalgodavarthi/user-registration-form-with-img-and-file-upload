from django import forms
from django.forms import widgets
from modelform.models import register
from django.utils.translation import gettext_lazy

class registerform(forms.ModelForm):
    class Meta:
        model = register
        fields='__all__'
        widgets = {'username':forms.TextInput(),'password':forms.PasswordInput(),'address':forms.Textarea()}
        labels ={'username':gettext_lazy('USERNAME')}
        help_texts={"username":gettext_lazy("plz enter the username")}






'''
class registerform(forms.ModelForm):
     class Meta:
        model = register
        fields = '__all__'  #all fields

class registerform(forms.ModelForm):
     class Meta:
        model = register
        fields = ["username",'email','gender'] #specified fields

class registerform(forms.ModelForm):
     class Meta:
        model = register
        exclude = ["username",'email','gender'] #except specified fields remaining fields is display


'''




'''
class registerform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    phone= forms.IntegerField()
    age=forms.IntegerField()
    gender = forms.CharField()
    address = forms.CharField()
    
''' 
    
    

















    
'''
   
        #fields = ['username','password','email']
        #exclude = ['username'.'password']
'''
