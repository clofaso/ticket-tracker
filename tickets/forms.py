from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter a Title"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Please describe your issue",
                "cols": 80
            }
        )
    )
    priority = forms.IntegerField(initial=4)
    class Meta:
        model = Ticket
        fields = [
            'title', 
            'description',
            'priority',
        ]

# class RawTicketForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter a Title"}))
#     description = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder": "Please describe your issue",
#                 "cols": 80
#             }
#         )
#     )
#     priority = forms.IntegerField(initial=4)