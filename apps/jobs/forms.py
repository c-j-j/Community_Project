from django import forms


class CommentForm(forms.Form):
    name= forms.CharField(label="Your name", max_length=200)