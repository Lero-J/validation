from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def validate_title(value):
    if value in ['Shuxnazar', 'gay']:
        raise ValidationError(message='Заголовок нецензурен')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title


def validate_age(data):
    if data > 100:
        raise ValidationError(message='Not appropriate age')


def validate_age_good(data):
    if data < 0:
        raise ValidationError(message='Not a good age')


class User(models.Model):
    name = models.CharField(max_length=100, validators=[validate_title])
    age = models.IntegerField(validators=[validate_age, validate_age_good])
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
