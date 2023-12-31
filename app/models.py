from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name= models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic_name
    




class Webpage(models.Model):
    topic_name= models.ForeignKey(Topic, on_delete= models.CASCADE) #This row is created for Connection Between Topic and Webpage.

    # The variables are created for taking name and webpage.
    name= models.CharField(max_length= 100)
    url= models.URLField()

    def __str__(self):
        return self.name






class AccessRecord(models.Model):
    name= models.ForeignKey(Webpage, on_delete= models.CASCADE) # This row is created for Connection Between Webpage and AccessRecord.

    date= models.DateField(auto_now=True)
    author= models.CharField(max_length=100)
    email= models.EmailField(default='soubhagyaranjannanda360@gmail.com')

    def __str__(self):
        return self.author