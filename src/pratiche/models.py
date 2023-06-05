from django.db import models
from django.urls import reverse
from .choices import *

class Pratica(models.Model):
	prot = models.IntegerField(null=False, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	tipologia = models.PositiveSmallIntegerField(choices=tipo_choices)
	# tipologia = models.ForeignKey('Tipo', on_delete=models.SET_NULL, null=True, blank=False)
	agente = models.ForeignKey('Agente', on_delete=models.SET_NULL, null=True, blank=True)
	magistrato = models.ForeignKey('Magistrato', on_delete=models.SET_NULL, null=True, blank=True)
	rgnr = models.CharField(max_length=10)
	fncr = models.CharField(max_length=10, choices=fncr_choices)
	# fncr = models.ForeignKey('Fncr', on_delete=models.SET_NULL, null=True, blank=False)
	data_delega = models.DateField(auto_now=False, auto_now_add=False)
	indagati = models.ForeignKey('Indagato', on_delete=models.SET_NULL, null=True, blank=True)
	attivita = models.TextField(max_length=1000, null=True, blank=True)
	data_restituzione = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	note = models.TextField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return '{0} ({1})'.format(self.prot, self.tipologia)

	def get_absolute_url(self):
		return reverse('pratiche:pratica-detail',kwargs={'id':self.id})


class Agente(models.Model):
	nome = models.CharField(max_length=50, null=True, blank=True)
	cognome = models.CharField(max_length=50, null=False, blank=False)
	caratt = models.CharField(max_length=7, null=False, blank=False, default='')

	def __str__(self):
		return self.cognome


class Magistrato(models.Model):
	nome = models.CharField(max_length=50, null=True, blank=True)
	cognome = models.CharField(max_length=50, null=False, blank=False)
	ufficio = models.CharField(max_length=100, null=True, blank=True)
	tel_ufficio = models.CharField(max_length=15, null=False, blank=False, default='No')
	cellulare = models.CharField(max_length=15, null=True, blank=True)

	def __str__(self):
		return self.cognome


class Indagato (models.Model):
	nome = models.CharField(max_length=50, null=False, blank=False)
	cognome = models.CharField(max_length=50, null=False, blank=False)
	data_nascita = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)

	def __str__(self):
		return self.cognome
