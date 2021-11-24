from django. urls import path
from myapp import views
urlpatterns=[

    path('add-order',views.add_order, name='add_order'),
    path('orders',views.order_list, name='order_list')

]