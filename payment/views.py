import razorpay
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from storeapp.models import Product
from storeapp.serializers import ProductSerializer
from rest_framework import status
from cartapp.models import Order, Orderitem, Transaction, PaymentFailure, Address
from cartapp.models import Cart, Cartitems
from payment.serializers import OrderSerializers 





RAZORPAY_KEY_ID = "rzp_test_DqyEDw9vF6Y4kA"
RAZORPAY_KEY_SECRET = "uibpbafCZAypJUX226PdWxBs"








class OrdersView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = request.user

        order_items = Orderitem.objects.filter(order__owner=user)
        serializer = OrderSerializers(order_items, many=True)
        print(serializer.data)

        print(order_items)
        return Response (serializer.data , status=status.HTTP_200_OK)










class CreateRazorpayCheckOutPaymentView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        print("inde------------------------------------")
        
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
       
        # cart_id = request.data.get("cart_id") # i can get the cart by user no need to have data
        user = request.user
      
        total_price = 0
        product_ids = []
        cart_id = Cart.objects.filter(owner=user).first()
        cart_items = Cartitems.objects.filter(cart=cart_id)

        #createing single order for each product for simplycity

        for item in cart_items:
            product_ids.append(str(item.product.id))
            total_price +=item.product.price

       

        amount =  int(total_price) * 100
        amount = int(amount)
        currency = 'INR'
        payment_capture = '1'
        order_data = {
            'amount': amount,
            'currency': currency,
            'payment_capture': payment_capture,
            "notes" : {
                "product_ids":product_ids,
                "price":amount,
            },
        

        }


        razorpay_order = client.order.create(data=order_data)
        order_id = razorpay_order.get('id')

        # print(product_ids, amount)



        return Response ({'order_id': order_id, 'amount': amount, 'currency': currency , 
                    
                             "razorpay_key":RAZORPAY_KEY_ID}, status=status.HTTP_200_OK)

# "notes" : {
#  "product_ids":product_ids,
#     "price":amount
# },

class VerifyCheckOutPaymentView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        
        # print(request.data)
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.fetch(request.data.get('razorpay_order_id'))
        items_details = razorpay_order.get('notes', {})

        # print(items_details, "ids---------------------------------")
 
        
        amount = items_details.get("price")
        amount = amount//100
     

        try:
            response = client.utility.verify_payment_signature({
                'razorpay_order_id': request.data.get('razorpay_order_id'),
                'razorpay_payment_id': request.data.get('razorpay_payment_id'),
                'razorpay_signature': request.data.get('razorpay_signature')
            })
            # creating Transaction
            Transaction.objects.create(
                payment_id =  request.data.get('razorpay_payment_id'),
                order_id  =  request.data.get('razorpay_order_id'),
                signature =  request.data.get('razorpay_signature'),
                amount = amount,

            )     
            return Response({"status":"success"})
        except razorpay.errors.SignatureVerificationError:
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)
   


class CheckOutPaymentSuccessOrderCreateView(GenericAPIView):

    def post(self, request , *args, **kwargs):
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.fetch(request.data.get('razorpay_order_id'))
        items_details = razorpay_order.get('notes', {})
        print(items_details)
        print(request.data)
        amount = items_details.get("price") //100
        print(amount)
        address = Address.objects.all().first()
        order = Order.objects.create(
            address = address,
            payment_status = "C",
            owner = request.user,
            order_payment_id =request.data.get('razorpay_payment_id'),
            isPaid=True,
            amount= items_details.get("price"),
            order_id= request.data.get('razorpay_order_id'),
        )
        product_ids = items_details.get("product_ids")
        print(product_ids)
        for id in product_ids:
            print(id)
            product = Product.objects.get(id=id)

            orderitem = Orderitem.objects.create(
                order = order,
                product = product,
                quantity= "1",
            )

        cart = Cart.objects.get(
            owner=request.user
        )
        print(cart)

        cart_items = Cartitems.objects.filter(cart=cart) 
        print(cart_items)
        cart_items.delete()



        return Response({"payment": "success"}, status=status.HTTP_201_CREATED)




class CreateRazorpayOrder(GenericAPIView):

    def post(self,request, *args,  **kwargs):
        
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        print("inside create payment")

        # Extract payment details from the request
        product_id = request.data.get('id')  # Amount should be in paise
        product_instance = Product.objects.filter(id=product_id)
        if product_instance.exists():
            product_instance = product_instance.first()
            serialized_data = ProductSerializer(product_instance)
            product_details = serialized_data.data
            amount =  int(product_instance.price) * 100
            amount = int(amount)
            currency = 'INR'
            payment_capture = '1'  # Auto-capture after order creation
            

            order_data = {
                'amount': amount,
                'currency': currency,
                'payment_capture': payment_capture,
                "notes" : product_details,
            }
            #i can pass some meta deta here aslo 

            razorpay_order = client.order.create(data=order_data)
            order_id = razorpay_order.get('id')

            return Response({'order_id': order_id, 'amount': amount, 'currency': currency , "notes":product_details,
                             "razorpay_key":RAZORPAY_KEY_ID})

        return Response ( {"status" :"Product doesn't exists " }, status=status.HTTP_404_NOT_FOUND)



class VerifyRazorpayPaymentView(GenericAPIView):
    def post(self, request, *args, **kwargs):
       
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.fetch(request.data.get('razorpay_order_id'))
        product_details = razorpay_order.get('notes', {})

    
        try:
            response = client.utility.verify_payment_signature({
                'razorpay_order_id': request.data.get('razorpay_order_id'),
                'razorpay_payment_id': request.data.get('razorpay_payment_id'),
                'razorpay_signature': request.data.get('razorpay_signature')
            })


            print("amount -------------------",request.data['notes']["price"] or 0)
            Transaction.objects.create(
                payment_id = request.data.get('razorpay_payment_id'),
                order_id  = request.data.get('razorpay_order_id'),
                signature = request.data.get('razorpay_signature'),
                amount = request.data['notes']["price"] or 0

            )
        # here logic will come of your order place
            # Handle successful payment verification (e.g., update order status)
            
            return Response({"status": "success"})
        except razorpay.errors.SignatureVerificationError:
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)




class PaymentSuccessOrderCreateView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        # print(request.data,"--------------------------------")
        print("inside payment success--------------")
        
        address = Address.objects.all().first()
        order = Order.objects.create(
            address = address,
            payment_status = "C",
            owner = request.user,
            order_payment_id = request.data.get("razorpay_payment_id"),
            order_id =   request.data.get("razorpay_order_id")  ,
            isPaid = True,
            amount = request.data["notes"]['price'] or 0,

        )
        print("order created ", order)
        product_instance = Product.objects.filter(id=request.data["notes"]['id'])
        if not product_instance.exists():
            return Response({"error": f"product with this id doesnt exists {request.data["notes"]['id']}"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            pro_inst = product_instance.first()
            print(pro_inst)

        Orderitem.objects.create(
            order = order,
            product = pro_inst,
            quantity = 1,

        )
       

        return Response({"payment": "success"}, status=status.HTTP_201_CREATED)





class PaymentFailedView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        print(user)
        print("payment fail-----------------------------------------")
        # print(request.data,"------------------------failed")
        meta_data = request.data.get("error").get("metadata")
        # print("meta ---------- ", meta_data)
        payment_id = meta_data.get("payment_id")
        order_id =  meta_data.get("order_id")
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.fetch(order_id)
        product_details = razorpay_order.get('notes', {})
        # print("deta-----------------", product_details)

        address = Address.objects.all().first()
        order = Order.objects.create(
            address = address,
            payment_status = "F",
            owner = user,
            order_payment_id = payment_id,
            order_id =   order_id ,
            isPaid = True,
            amount = product_details['price'] or 0,

        )
        PaymentFailure.objects.create(
            payment_id= payment_id,
            order_id =order_id,
            user = user
        )


        return Response({"status":"failed"}, status=status.HTTP_400_BAD_REQUEST)
