
from django.db.models.signals import post_save
from account.models import User
from django.dispatch import receiver
from cartapp.models import Cart



@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        cart = Cart.objects.create(
            owner=instance,

        )
        print(f'Cart for the User created {instance.email} created successfully.')

    return 
