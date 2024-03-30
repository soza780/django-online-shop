from django import forms
from .models import Coupon


class CouponApplyForm(forms.ModelForm):
    code = forms.CharField()