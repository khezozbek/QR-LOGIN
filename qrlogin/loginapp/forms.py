from django import forms


class QRLoginForm(forms.Form):
    qr_code = forms.ImageField()
