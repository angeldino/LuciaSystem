from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    ap_pat = models.CharField(max_length=50, null=True, blank=True)
    ap_mat = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    rebe_user = models.CharField(max_length=50, null=True, blank=True)
    pc_user = models.CharField(max_length=50, null=True, blank=True)
    shift = models.CharField(max_length=50, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name + " " +  self.ap_pat + " " + self.ap_mat + " - Turno: " + self.shift
    
class Supplier(models.Model):
    id = models.IntegerField(primary_key=True)
    plant_code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    convenio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.plant_code + " - " + self.name