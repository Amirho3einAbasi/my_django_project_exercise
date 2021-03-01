from django import forms
from django.contrib.auth.models import User
from django.core import validators

class login_form(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خودرا وارد کنید'}),
        label='نام کاربری'
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز ورود خودرا وارد کنید'}),
        label='رمز عبور',
    )
    def clean_user_name(self):
        username = self.cleaned_data.get('user_name')
        user_name_exists = User.objects.filter(username=username).exists()
        if not user_name_exists :
            raise forms.ValidationError('این نام کاربری قبلا ثبت نام نکرده است')
        return username




class register_form(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خودرا وارد کنید'}),
        label='نام کاربری'
    )
    user_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خودرا وارد کنید'}),
        label='ایمیل'

    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز ورود خودرا وارد کنید'}),
        label='رمز ورود'
    )
    user_confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز عبور خوذرا تکرار کنید'}),
        label='تکرار رمز عبور'
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get('user_name')
    #     user_name_exists = User.objects.filter(username=user_name).exists()
    #     if  user_name_exists:
    #         raise forms.ValidationError('این نام کاربری قبلا ثبت نام کرده است')

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        user_name_exists = User.objects.filter(username=user_name).exists()
        if user_name_exists:
            raise forms.ValidationError('این نام کاربری قبلا ثبت نام کرده است')
        if len(user_name) < 8 :
            raise forms.ValidationError('تعداد کاراکتر های نام کاربری کمتر از 8 کاراکتر است')
        return user_name

    def clean_user_email(self):
        email = self.cleaned_data.get('user_email')
        user_email_exists = User.objects.filter(email=email).exists()
        if user_email_exists:
            raise forms.ValidationError('این ایمیل قبلا ثبت نام کرده است')
        return email

    def clean_user_confirm_password(self):
        password = self.cleaned_data.get('user_password')
        password_confirm = self.cleaned_data.get('user_confirm_password')
        if password != password_confirm:
            raise forms.ValidationError('رمز  های ورود یکی نیستند')
        return password
