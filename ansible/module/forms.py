'''
Created on Jul 26, 2018

@author: nexii
'''

from django import forms

class Sample(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
