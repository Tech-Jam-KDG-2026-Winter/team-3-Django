from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.Form):
    username = forms.CharField(label="ユーザー名")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    age = forms.IntegerField(label="年齢", min_value=0, max_value=120)

    password1 = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="パスワード（確認）",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = None

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError("パスワードが一致しません")

        validate_password(p2)
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
