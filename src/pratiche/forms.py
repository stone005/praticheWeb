from django import forms
from .models import Pratica,Agente,Magistrato,Indagato
from .choices import *


class PraticaForm(forms.ModelForm):
	prot = forms.IntegerField(
					label='Protocollo',
					widget=forms.NumberInput(
						attrs={
							'min':'0',
							'readonly':'readonly'
							}
						)
					)
	tipologia = forms.IntegerField(
					label='Tipologia',
					widget=forms.Select(choices=tipo_choices),
					)
	agente = forms.ModelChoiceField(
				label='Agente',
				queryset=Agente.objects.all(),
					)
	magistrato = forms.ModelChoiceField(
				label='Magistrato',
				queryset=Magistrato.objects.all(),
					)
	fncr = forms.CharField(
					label='FNCR',
					widget=forms.Select(choices=fncr_choices),
					)
	rgnr = forms.CharField(
				label='R.G.N.R.', 
				widget=forms.TextInput(attrs={'placeholder':'R.G.N.R.'})
				)	
	data_delega = forms.DateField()
	indagati = forms.ModelChoiceField(
				label='Indagato',
				queryset=Indagato.objects.all(),
					)
	attivita = forms.CharField(
			required=False, 
			widget=forms.Textarea(
				attrs={
					'placeholder':'Attività',
					'class': 'new-class-name two',
					'rows': 20,
					'cols': 50,
					}
				)
			)
	note = forms.CharField(
			required=False, 
			widget=forms.Textarea(
				attrs={
					'placeholder':'Note',
					'class': 'new-class-name two',
					'rows': 20,
					'cols': 100,
					}
				)
			)
	data_restituzione = forms.DateField()

	class Meta:
		model = Pratica
		exclude = ('timestamp',) 
