from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required = True)

	class Meta:
		fields = ('search',)