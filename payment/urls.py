from django.urls import path
from payment.views import ( CreateRazorpayOrder, VerifyRazorpayPaymentView,
                           PaymentSuccessOrderCreateView, PaymentFailedView, 
                           CreateRazorpayCheckOutPaymentView, VerifyCheckOutPaymentView,
                           CheckOutPaymentSuccessOrderCreateView, OrdersView, 
                           RazorpayPaymentRefundView


)

urlpatterns = [
    path("refund/payment/",RazorpayPaymentRefundView.as_view(), name="refund"),
    path("get-all-orders/",OrdersView.as_view(), name="orders" ),
    path("create/order/", CreateRazorpayOrder.as_view(), name="create_payment_order"),
    
   
    path("verify/",VerifyRazorpayPaymentView.as_view(), name="verify-payment"),
    path("success/payment/",PaymentSuccessOrderCreateView.as_view(), name="success-payment"),
    path("failed/payment/", PaymentFailedView.as_view(), name="failed-payment"),


    path("check-out-payment/", CreateRazorpayCheckOutPaymentView.as_view(), name="create_check_out_payment"),
    
    path("check-out-verify-payment/", VerifyCheckOutPaymentView.as_view(), name="check_out_verify_payment"),
    
    path("check-out-success/payment/", CheckOutPaymentSuccessOrderCreateView.as_view(), name="check-out-success"),
    
]
