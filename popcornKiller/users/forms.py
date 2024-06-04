from django import forms
from .models import User


# creating a form
class UserForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = User

		# specify fields to be used
		fields = [
			"name",
			"email",
			"password",
		]
