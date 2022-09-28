from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from unicodedata import decimal
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    descricao = models.TextField(default=None, null=True)
    quantidade = models.IntegerField(null=True,blank=True,default=None)
    imagem = models.ImageField(upload_to='items',null=True,blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    nota = models.IntegerField()
    descricao = models.TextField(default=None,null=True,blank=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    
    def __str__(self):
        return ""+self.nota
