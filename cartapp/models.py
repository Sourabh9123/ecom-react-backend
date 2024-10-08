from django.db import models
from account.models import User
from django.contrib.auth import get_user_model
import uuid
from storeapp.models import Product




User = get_user_model()




class Cart(models.Model):
    owner  = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart_owner_user')
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.email


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE  , related_name='cart_user', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)



    def __str__(self):
        return self.cart.owner.first_name
    

    



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,  related_name='address')
    name = models.CharField(max_length=250, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    land_mark =models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.address} of ----> {self.user.email}"


class Order(models.Model):

    status = (
        ('P','pending'),
        ('F', 'fail'),
        ('C', 'complete')

    )
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, )
    payment_status = models.CharField(max_length=10, choices=status, default='P')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_payment_id = models.CharField(max_length=254, null=True)
    isPaid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.payment_status} --- {self.owner.first_name}"


class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchased', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    

    def __str__(self):
        return f"{self.order.payment_status}----{self.order.owner}"
    

######################




# this is payment success Transaction
class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    payment_id = models.CharField(max_length=254)
    order_id = models.CharField(max_length=254)
    signature = models.CharField(max_length=254)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.payment_id
    
class PaymentFailure(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    payment_id = models.CharField(max_length=254)
    order_id = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)


    def __str__(self):
        return self.payment_id






class PaymentSuccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)  
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PaymentSuccess by {self.user.email} for {self.amount}"