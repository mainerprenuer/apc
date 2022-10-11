from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    lga = models.ForeignKey('Lga', on_delete=models.CASCADE)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    acc_num = models.IntegerField(null=True)
    image = models.ImageField(upload_to="image",null=True)
    
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    

class Lga(models.Model):
    name = models.CharField(max_length=15)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
class Ward(models.Model):
    name = models.CharField(max_length=15)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name





# from django.db import models
# # from agents.models import 


# class State(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Local_gov(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name
        

# class Ward(models.Model):
#     local_gov = models.ForeignKey(Local_gov, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
#     local_gov = models.ForeignKey(Local_gov, on_delete=models.SET_NULL, blank=True, null=True)
#     ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         return self.name