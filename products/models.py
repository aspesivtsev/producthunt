from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=2082)
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(auto_now=True)
    votes_total = models.IntegerField()
    image = models.ImageField(upload_to='images/products/', blank=True)
    icon = models.ImageField(upload_to='images/blog/', blank=True)
    body = models.TextField()


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    def mod_date_pretty(self):
        return self.mod_date.strftime('%b %e %Y, %H:%M')

    def summary(self):
        '''This is shortening of the body text, like a small preview... currently it takes first 20 words.'''
        return " ".join(self.body.split()[:20])+"..."