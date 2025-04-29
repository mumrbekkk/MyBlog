from django.contrib.auth.models import User


def create_new_user(username, email, password, **kwargs):
    new_user = User.objects.create_user(username=username, email=email, password=password, **kwargs)
    
    if new_user:
        new_user.save()
    
    #TODO else raise an error


def filter_by(**kwargs):
    return User.objects.filter(**kwargs)

