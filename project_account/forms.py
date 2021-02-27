from django import forms


class login_form(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خودرا وارد کنید'}),
        label='نام کاربری'
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا رمز ورود خودرا وارد کنید'}),
        label='رمز عبور'
    )
