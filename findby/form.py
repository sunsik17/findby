from django import forms


class SearchProductForm(forms.Form):
    category = forms.CharField(label='category', required=True)
    contents = forms.CharField(max_length=30, min_length=1, label='contents', required=True)
