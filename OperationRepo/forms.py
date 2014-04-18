from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required = True)
	format = forms.CharField(required = True, widget=forms.HiddenInput(),  initial="pretty")

	class Meta:
		fields = ('search', 'format')