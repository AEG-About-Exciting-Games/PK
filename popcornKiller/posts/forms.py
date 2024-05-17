from django import forms
from .models import Posts


# creating a form
class PostsForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Posts

		# specify fields to be used
		fields = [
			"writer",
			"movie",
			"content",
			"date",
		]
