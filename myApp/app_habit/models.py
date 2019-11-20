from django.db import models

class Habit(models.Model) :
    title = models.CharField(max_length = 100)  #title of habit
    category = models.CharField(max_length = 50, blank = True)  #type of habit
    number = models.IntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add = True)  #created time
    content = models.TextField(blank = True, null = True)  #content

    def __str__(self) :
        return self.title

    class Meta:  #order desc by created time
        ordering = ['-date_time']
