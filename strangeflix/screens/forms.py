from django import forms
from .models import Comment
PLAN_CHOICES = (
    ('M','Rs 160 : Monthly Plan ( 30 days )'),
    ('H','Rs 900 : 6 Months Plan ( 180 days )'),
    ('Y','Rs 1700 : Yearly Plan ( 365 days )')
)

class SelectPlanForm(forms.Form):
    plan_option = forms.ChoiceField(
        widget=forms.RadioSelect(),choices=PLAN_CHOICES)

class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)