from django import forms
from upload.models import register

class formregister(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'
    def clean_username(self):
        u = self.cleaned_data['username']
        if not(3<=len(u)):
            raise forms.ValidationError("plz enter above 3 characters")
        if not(len(u)<=20):
            raise forms.ValidationError("plz enter below 20 characters")
        return u
    def clean_password(self):
        u = self.cleaned_data['password']
        if not(3<=len(u)):
            raise forms.ValidationError("plz enter above 3 characters")
        if not(len(u)<=15):
            raise forms.ValidationError("plz enter below 15 characters")
        if not(u[0].isupper()):
            raise forms.ValidationError("password first letter should be alphabet and uppercase")
        return u

    def clean_phone(self):
        u = self.cleaned_data['phone']
        if not(len(str(u))==10):
            raise forms.ValidationError("plz phone number should be ten digits")
        if not(str(u)[0] in ['6','8','9','7']):
            raise forms.ValidationError("plz enter indian mobile number startwith 6 or 7 or 8 or 9")
        return u

    def clean_img(self):
        new=self.cleaned_data['img']
        list1 = ['jpg','png','jpeg','gif']
        if str(new).split('.')[-1].lower() not in list1:
            raise forms.ValidationError("plz upload image should be jpg or jpeg or png or gif only")
        return new

    def clean_file(self):
        new=self.cleaned_data['file']
        list1 = ['txt','doc','docx','pdf','csv']
        if str(new).split('.')[-1].lower() not in list1:
            raise forms.ValidationError("plz upload file should be 'txt','doc','docx','pdf','csv' only")
        return new

    def clean_age(self):
        new=self.cleaned_data['age']
        if not(10<=int(new)):
            raise forms.ValidationError("plz your age should be above 10 years")
        if not(50>=int(new)):
            raise forms.ValidationError("plz your age should be below 50 years")
        return new


class loginform(forms.ModelForm):
    class Meta:
        model= register
        fields= ['username','password']
    def clean_username(self):
        u = self.cleaned_data['username']
        print("hello")
        print(u)
        if 10==10:
            raise forms.ValidationError("plz enter above 3 characters")
        if len(u)<=15:
            raise forms.ValidationError("plz enter below 15 characters")
        print(u)
        return u
