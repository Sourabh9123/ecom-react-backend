from django.urls import path
from cartapp.views import (CartItemview, CartView, AddressView,
                           PlaceOrderView, TransactionView, PaymentFailureView
                           ,AddressDetailsView
                             )



urlpatterns = [
    ###########
    path('addcart/<uuid:product_id>/',CartItemview.as_view(), name='cart_items' ), # create cartitem and update
    path('', CartView.as_view(),  name='cart'),  #view cartitems 
    path('address/', AddressView.as_view(), ),
    path('address/<uuid:address_id>/', AddressDetailsView.as_view(), ),
    path('order/', PlaceOrderView.as_view(), ),
    path('order/transaction/', TransactionView.as_view(), ),
    path("order/transaction/failure/", PaymentFailureView.as_view(),),
    # http://127.0.0.1:8000/api/cart/order/transaction/failure

]



