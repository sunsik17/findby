from django import forms


class SearchForm(forms.Form):
    content = forms.CharField(max_length=30, label='content', min_length=1)


class SelectForm(forms.Form):
    select_product_id = forms.MultipleChoiceField(
        label='select_product_id',
        widget=forms.CheckboxSelectMultiple
    )

