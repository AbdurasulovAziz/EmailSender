from django import forms

class EmailForm(forms.Form):
    title = forms.CharField(label='Заголовок:')
    text = forms.CharField(label='Текст:', widget=forms.Textarea)
    emails = forms.CharField(label='Почта получателя: (Введите получателей через запятую)',
                             widget=forms.Textarea)
