from django import forms

class NQueensForm(forms.Form):
    number_of_queens = forms.IntegerField(
        label='Number of Queens',
        min_value=1,
        max_value=15,  # Adjust as needed
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
