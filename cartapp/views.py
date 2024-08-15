from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from cartapp.models import  Cartitems, Cart , Address, Order , Orderitem, Transaction, PaymentFailure
from storeapp.models import Product
from django.db import transaction
# from cartapp.serializers import CartItemsListSerializer, CartItemsSerializer, CartSerializer, NewcartitemSerializer
from rest_framework.response import Response
from cartapp.serializers import ( NewcartitemSerializer, CartSerilizer,
                                  SimpleProductSerializer, GetCartitemSerializer
                                  ,AddressSerializer, OrderSerializer, OrderItemSerializer,
                                  TransactionSerializer, PaymentFailureSerializer
                                 
)
from rest_framework import status
from storeapp.serializers import ProductSerializer 
from rest_framework.permissions import  IsAuthenticated
from rest_framework.views import APIView
import razorpay


from shiprocket.create_quick_order import create_quick_order

# PUBLIC_KEY = "rzp_test_b6Q27ppeBNZtMJ"
# SECRET_KEY = "gLCNbZNqQes9bX74Db4Wn19u"



PUBLIC_KEY = "rzp_test_DqyEDw9vF6Y4kA",

SECRET_KEY ="uibpbafCZAypJUX226PdWxBs"





# def create_order(amount, currency):
#     client = razorpay.Client(auth=("rzp_test_DqyEDw9vF6Y4kA", "uibpbafCZAypJUX226PdWxBs"))
#     response = client.order.create(
#         {
#         'amount': amount,
#         'currency': currency,
#         'payment_capture': 1  # Automatically capture payments
#     }
#     )
#     return response


# def capture_payment(order_id, payment_id):
#     client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))
#     client.payment.capture(payment_id, order_id)







#adding item to cart and updating and delete item
class CartItemview(generics.GenericAPIView):   # here we need quantity
    permission_classes = [IsAuthenticated]

    def post(self,  request, *args, **kwargs):
        default_quantity = 1
        data = request.data
        id = kwargs.get('product_id')
        # cart_ins = Cart.objects.get(owner=request.user)
        cart_ins, created = Cart.objects.get_or_create(
            owner=request.user,

        )

       
        # if product doest exists need to take care of it
        product_exist = Cartitems.objects.filter(product=id, cart=cart_ins.id).exists()
        if product_exist:
            product = Cartitems.objects.filter(product=id, cart=cart_ins.id).first()

            product_quantity = get_object_or_404(Product,id=id)
            print(product_quantity.product_quantity, "----------------------------------------")
            if product_quantity.product_quantity  < 1:
                return Response("product quantity not avalible", status=status.HTTP_403_FORBIDDEN)
            customer_demant_quantity = request.data.get('quantity')
            if  product_quantity.product_quantity < int(customer_demant_quantity):#####################################
                return Response("product quantity not avalible", status=status.HTTP_403_FORBIDDEN)
            
            if product_quantity.product_quantity > request.data.get('quantity',default_quantity):
               
                if product is not None:
                    
                    quantity = request.data.get('quantity',default_quantity)
                    print("-------------------------quantity",quantity)
                    new_qwn = quantity + product.quantity
                    print("---------new q", new_qwn)
                    if product_quantity.product_quantity <  new_qwn:
                        return Response("cant add more unit out of stock", status=status.HTTP_200_OK)

                    print(product.quantity,"------------prod")
                    if "quantity" not in request.data:
                        print("insde con")
                        product.quantity = new_qwn
                    else:
                        product.quantity = quantity
                        
                    print("out con")
                    product.save()
                    serializer = NewcartitemSerializer(product, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
    
        # this create new cartitem
        product = Product.objects.get(id=id)
        cart_ins = Cart.objects.get(owner=request.user)
        data['cart'] = cart_ins.id
        data['product'] = product.id


        serializer = NewcartitemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

            return Response( status=status.HTTP_400_BAD_REQUEST)
 
        return Response({"error":"error"},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,  request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        cart_ins = Cart.objects.get(owner=request.user)
        carttiem = Cartitems.objects.filter(cart= cart_ins  , product=product_id)
        carttiem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

        





# cartitems view and total
class CartView(generics.GenericAPIView):


    def get(self, request, *args, **kwargs):
        cart_owner = request.user
        print(cart_owner)
        objs, created = Cart.objects.get_or_create(owner=cart_owner)
        
        if created:
            return Response("no items on cart", status=status.HTTP_200_OK)
        
        objs = Cart.objects.filter(owner=cart_owner)
      
        serializer = CartSerilizer(objs, many=True)
 
        user_cart_items = Cartitems.objects.filter(cart=objs[0])

        cartitems_serializer = GetCartitemSerializer(user_cart_items, many=True)
       
        cart_total = sum([i.quantity * i.product.price for i in user_cart_items]) 
     
        response_data = {
            **serializer.data[0],
            'cart_total' :cart_total,
            'cart_item' : cartitems_serializer.data,
        }

       
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(response_data, status=status.HTTP_200_OK)
    


class AddressView(generics.GenericAPIView):
    serializer_class = AddressSerializer
    # queryset = Address
    
    def post(self,  request, *args, **kwargs):
        data=request.data
        data['user'] = request.user.id
        serializer = AddressSerializer(data=data)
        print(data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("errrrrrr-------------")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,  request, *args, **kwargs):

        objs = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class AddressDetailsView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        print("api triggered")
        address_id = kwargs.get("address_id")
        qs = Address.objects.filter(id=address_id)

        if qs.exists():
            address_instance = qs.first()
            serializer = AddressSerializer(address_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the updated instance
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

        
    
    def get(self, request, *args, **kwargs):
        address_id = kwargs.get("address_id")
        qs = Address.objects.filter(id=address_id)
        if qs.exists():
            serializer = AddressSerializer(qs.first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        address_id = kwargs.get("address_id")
        qs = Address.objects.filter(id=address_id)
        if qs.exists():
            qs.first().delete()
            return Response({"message": "Address deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)




class PlaceOrderView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user, "im user")
        order = Order.objects.filter(owner=user.id).first()
        print(order)
        if order is not None:
            serializers = OrderSerializer(order)

            orderitems = Orderitem.objects.filter(order=order)
            orderitems_serializer = OrderItemSerializer(orderitems, many=True)
        
            # print(serializers.data)
            # print(serializers)
            response_data = {
                **serializers.data,
                'orderitem' : orderitems_serializer.data,

            }
            # print(response_data)
        else:
            response_data = {
                
                    'orderitem' : "No item in cart"

                }
     
        return Response(response_data, status=status.HTTP_200_OK) 


    def post(self, request, *args, **kwargs):
        # print('outer side')
        

        try:
            user_id = request.user.id

            total_cartitems = Cartitems.objects.filter(cart__owner__id = user_id)
            total_price = sum([i.quantity * i.product.price for i in total_cartitems])

            # print('inner body')

            # order_data = create_order(total_price, "INR")
    
            client = razorpay.Client(auth=("rzp_test_DqyEDw9vF6Y4kA", "uibpbafCZAypJUX226PdWxBs"))

            data = { "amount": int(total_price) *100, "currency": "INR", "receipt": "order_rcptid_11" ,"payment_capture": "1",}
            payment = client.order.create(data=data)

            print("-----------------------------------------------",payment)
        
            user=request.user
            
            try:
                
                cartitems = Cartitems.objects.filter(cart__owner=user)
                
                print(cartitems, "-------------------------cartitems")
            except Exception as e:
                return Response("No items added in cart please add item first", status=status.HTTP_204_NO_CONTENT)
                # print('after cartitems----------------------', cartitems)
            
            try:
            
                address = Address.objects.filter(user=user.id).first()
            
            except Exception as e:
                return Response("first add your address", status=status.HTTP_204_NO_CONTENT)
            

            ########### payment logic after payment this will run 
        
            with transaction.atomic():        
                order = Order.objects.create(address=address, payment_status='P',owner= user, amount=total_price, order_payment_id = payment['id']) 
                orderitem =  [  Orderitem(order=order, product=item.product, quantity=item.quantity)    for item in cartitems ]
                Orderitem.objects.bulk_create(orderitem)
            
                # order_payment_id=payment.get('id')

                # for i in cartitems:
                #     product = i.product
                #     if product.product_quantity >= i.quantity:
                #         product.product_quantity -= i.quantity
                #     else:
                #         return Response({"error":"error not sufficent quantity"} ,status=status.HTTP_400_BAD_REQUEST)

                #     product.save()    
                
                # cartitems.delete()

                serializer = OrderSerializer(order)
                data = {
                    "payment": payment,
                    "order": serializer.data,
                    
                }
                return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            
            return Response({'done':'Something went wrong try again',"error":str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                
        return Response({'done':'done', }, status=status.HTTP_200_OK)





class TransactionView(generics.GenericAPIView):
    serializer_class = TransactionSerializer
    # queryset = Transaction

    def post(self, request, *args, **kwargs):

        with transaction.atomic():
            serialzier = TransactionSerializer(data=request.data)
            # print(request.data)
            if serialzier.is_valid():
            

                try:
                    
                    razorpay_order_id =  serialzier.validated_data.get('order_id')
                    razorpay_payment_id = serialzier.validated_data.get('payment_id')
                    razorpay_signature = serialzier.validated_data.get('signature')
                    

                    client = razorpay.Client(auth=("rzp_test_DqyEDw9vF6Y4kA", "uibpbafCZAypJUX226PdWxBs"))         
                    client.utility.verify_payment_signature({
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': razorpay_payment_id,
                    'razorpay_signature': razorpay_signature
                    })
                    print("sig", razorpay_signature)
                    print("id payment", razorpay_payment_id, )
                    print("order id", razorpay_order_id)
                    
                    cartitems = Cartitems.objects.filter(cart__owner=request.user)
                    print(cartitems,"-------------------------cccccccccccccc") 
                    print(cartitems.first().quantity)
                    # cartitems.delete()
                    #whill have to use loop beacuse every single order has diffrent quantity
                    for items in cartitems:
                        product = Product.objects.get(id=items.product.id)
                        print("product", product)
                        print("prod q", product.product_quantity)

                        product.product_quantity -= items.quantity
                        
                        product.save() 
                        print(product.product_quantity)

                    cartitems.delete()

                    try:
                        order = Order.objects.get(order_payment_id = razorpay_order_id)
                    
                        order.isPaid = True
                        order.payment_status = "C"
                        order.save()
                        
                    except  Exception as e:
                        pass
                    
                    #here will have to create shipment of product 
                    shipment = create_quick_order("add","pro")

                except Exception as e :
                    return Response({"error":str(e), "payment":"payment not verify"})
                serialzier.save()
                return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response( serialzier.errors,status=status.HTTP_400_BAD_REQUEST)




#this view need to be completed
class PaymentFailureView(generics.GenericAPIView):
    serializer_class = PaymentFailureSerializer

    
    def post(self, request, *args, **kwargs):
        print(request.data)
        user = request.user

        if ("order_id" and "payment_id") in request.data:
            failed_payment = PaymentFailure.objects.create(
                    user = request.user,
                    order_id = request.data.get("order_id"),
                    payment_id = request.data.get("payment_id")

            )
            serializer = PaymentFailureSerializer(failed_payment)
                
            return Response({"test":serializer.data}, status=status.HTTP_204_NO_CONTENT)
        return Response({"test":"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        
    




























































# class CartItemsView(generics.ListCreateAPIView, generics.UpdateAPIView):
    
#     def get_queryset(self):
#         return Cartitems.objects.filter(cart=self.request.user.cart_owner_user.id)

#     # def get_queryset(self):
#     #     return Cartitems.objects.filter(cart=self.kwargs.get('uuid'))
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return CartItemsListSerializer
#         return CartItemsSerializer
    

#     def get_serializer_context(self):
#         cart_id =self.request.user.cart_owner_user.id
        
#         return {'product_id':self.kwargs.get('uuid'),'cart_id':cart_id}
    



    
# class CartItemsView(generics.GenericAPIView):
    

#     def get(self, request, *args, **kwargs):
#         cartitems = Cartitems.objects.filter(cart=request.user.cart_owner_user.id) 
#         serializer = CartSerializer(cartitems,  many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request,  *args, **kwargs):
#         cartitems = Cartitems.objects.filter(cart=request.user.cart_owner_user.id) 
#         if property.id in cartitems:
#             print("yes")
    
    
#     def get_serializer_context(self):
#         cart_id =self.request.user.cart_owner_user.id
        
#         return {'product_id':self.kwargs.get('uuid'),'cart_id':cart_id}
    







# class CartView(APIView):
#     # serializer_class = CartSerializer
#     # # queryset = Cart.objects.all()

#     # def get_queryset(self):
#     #     pk = self.kwargs.get('cart_id')
#     #     return get_object_or_404(Cart,id=pk)
    
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('cart_id')
    
#         query_set = get_object_or_404(Cart, id=pk)
#         serializer = CartSerializer(query_set, many=False)

#         return Response(serializer.data,  status=status.HTTP_200_OK)
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('cart_id')
        
#         query_set = get_object_or_404(Cart, id=pk)
#         query_set.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)








# class CartItemViewSet(generics.ListAPIView):
    
#     serializer_class = CartItemsListSerializer

#     def get_queryset(self):
#         print(self.request.user.id)
#         cart_id =  self.kwargs.get('uuid')
#         return  Cartitems.objects.get(cart__owner__id=self.request.user.id)
    

 # return Response({"payment": payment})
        
        # data = None

        # client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))
        # print(client,'--------------------')
        
        # payment  = {
        #         'amount': int(total_price) * 100,  # Amount in paise
        #         'currency': 'INR',
        #         "payment_capture": "1",
        #     }
        # payment = client.order.create(data=payment_data)
        
        
        

        """order response will be 
            {'id': 17, 
            'order_date': '23 January 2021 03:28 PM', 
            'order_product': '**product name from frontend**', 
            'order_amount': '**product amount from frontend**', 
            'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""
        # print(payment,'________________________________------------')
