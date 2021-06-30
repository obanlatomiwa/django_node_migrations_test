from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    phone_number = models.CharField(max_length=80, unique=True,
                                    validators=[
                                        RegexValidator('^\+\d{1,3}\d{3,}$', 'Make sure you add valid a phone number. '
                                                                            'Add country code in number e.g +234XXXX',
                                                       'invalid phone number')])
    email = models.CharField(max_length=80, null=True, blank=True)
    date_of_birth = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Post(models.Model):
    user = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Account, default=1, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.user.username
