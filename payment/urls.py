from django.urls import path
from payment.views import ( CreateRazorpayOrder, VerifyRazorpayPaymentView,
                           PaymentSuccessOrderCreateView, PaymentFailedView
)

urlpatterns = [
    path("create/order/", CreateRazorpayOrder.as_view(), name="create_payment_order"),
    path("verify/",VerifyRazorpayPaymentView.as_view(), name="verify-payment"),
    path("success/payment/",PaymentSuccessOrderCreateView.as_view(), name="success-payment"),
    path("failed/payment/", PaymentFailedView.as_view(), name="failed-payment"),
]
