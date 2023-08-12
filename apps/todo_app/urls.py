from django.urls import path

from .views import(
    car_list,
    create_car,
    update_car,
    delete_car,
)

urlpatterns = [
    path('', car_list),
    path('create/', create_car),
    path('update/<id>/', update_car),
    path('delete/<id>/', delete_car),
]