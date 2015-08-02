from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):
	"""
	Form for registering a new user profile.
	"""
	email = forms.EmailField(widget=forms.TextInput,label="Email")
	full_name = forms.CharField(widget=forms.TextInput, label="Full Name")
	password1 = forms.CharField(widget=forms.PasswordInput, 
		label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput, 
		label="Password (again)")


	class Meta:
		model = UserProfile
		fields = ['full_name', 'email', 'password1', 'password2']

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
		return self.cleaned_data

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	"""
	Login Form
	"""
	email = forms.EmailField(widget=forms.widgets.TextInput)
	password = forms.CharField(widget=forms.widgets.PasswordInput)

	class Meta:
		fields = ['email', 'password']
