from app.models import Profile
from django import forms


class ProfileModelForm(forms.ModelForm):
    first_name_label = 'Имя'
    last_name_label = 'Фамилия'
    phone_label = 'Моб. телефон'
    email_label = 'Email'
    birthday_label = 'Дата рождения'

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': first_name_label,
    }), required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': last_name_label,
    }), required=True)

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'tel',
        'placeholder': phone_label,
        'data-inputmask': '\'alias\': \'+7(999) 999-99-99\'',
    }), required=True)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': email_label,
    }), required=True)

    birthday = forms.CharField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': birthday_label,
        'data-inputmask': '\'alias\': \'date\'',
    }), required=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def clean_birthday(self):
        from datetime import datetime
        birthday = self.cleaned_data.get('birthday')
        try:
            date = datetime.strptime(birthday, '%d/%m/%Y')
        except ValueError:
            raise forms.ValidationError('Дата рождения введена некоректно.', code='invalid')
        return date

    def clean_phone(self):
        import re
        phone = self.cleaned_data.get('phone')
        regex = '[+7_()\s-]'
        clean_phone = re.sub(regex, "", phone)
        if not len(clean_phone) == 10:
            raise forms.ValidationError('Номер телефона введен некоректно.', code='invalid')
        return clean_phone

