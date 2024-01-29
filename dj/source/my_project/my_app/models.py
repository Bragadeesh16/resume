from django.db import models

class default_template(models.Model):
    profile = models.ImageField(upload_to="images/")
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.IntegerField()
    address =  models.CharField(max_length = 100)
    pin_code = models.IntegerField()
    nationality = models.CharField(max_length = 20)
    linkedin = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.first_name
