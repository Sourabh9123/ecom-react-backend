from django.contrib import admin
from cartapp.models import ( Address , Order, Orderitem,
                             Transaction, PaymentFailure, PaymentSuccess

)

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(PaymentFailure)
admin.site.register(PaymentSuccess)



class TransactionAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'order_id', 'signature', 'amount', 'create_at']
    ordering = ['-create_at', 'payment_id']

admin.site.register(Transaction, TransactionAdmin)