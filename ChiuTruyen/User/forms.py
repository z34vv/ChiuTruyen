from django import forms
from .models import CustomUser
import re


class RegisterForm(forms.ModelForm, forms.Form):
    repassword = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']
        field_classes = {

        }
        widgets = {
            'email': forms.EmailInput()
        }

    def clean_repassword(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            repassword = self.cleaned_data['repassword']
            if password == repassword and password:
                return repassword
        raise forms.ValidationError("Mật khẩu không hợp lệ!")

    def clean_name(self):
        username = str(self.cleaned_data['username']).replace(' ', '')
        if len(username) < 6 or len(username) > 100:
            raise forms.ValidationError("Tên tài khoản phải có ít nhất 6 ký tự và ít hơn 100 ký tự!")
        if not re.search(r'^\w+&', username):
            raise forms.ValidationError("Tên tài khoản không được có kí tự đặc biệt!")
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại!")

    def clean_email(self):
        email = str(self.cleaned_data['email']).replace(' ', '')
        if ('@' not in email) or ('.' not in email):
            raise forms.ValidationError("Email không hợp lệ!")
            print("Email không hợp lệ!")
        else:
            mail_item = email.split('@')
            if mail_item[0] == '':
                raise forms.ValidationError("Email không hợp lệ!")
                print("Email không hợp lệ!")
            else:
                mail_item = mail_item[1].split('.')
                if (mail_item[0] == '') or (mail_item[1] == ''):
                    raise forms.ValidationError("Email không hợp lệ!")
                    print("Email không hợp lệ!")
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại!")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

    def save(self, **kwargs):
        userName = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = CustomUser.objects.create_user(username=userName, email=email, password=password, first_name='', last_name='')