from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Call parent's constructor
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # Now we can access fields property and change a required field
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

        # Set password widget
        widgets = {
            'password': forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SetPasswordFormNew(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password and also only requires the user to enter the password once and they
    can confirm using the show/hide button (up to date UX)
    """

    new_password = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        password = self.cleaned_data["new_password"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class UpdateUserInfo(forms.ModelForm):
    """
    A form for users to change their existing account information
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

