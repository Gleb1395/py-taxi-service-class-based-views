from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturer-list/", ManufacturerListView.as_view(), name="manufacturer_list"  # NOQA E501
    ),
    path("car-list/", CarListView.as_view(), name="car_list"),
    path("car-detail/<int:pk>", CarDetailView.as_view(), name="car_detail"),
    path("driver-list/", DriverListView.as_view(), name="driver_list"),
    path("driver-detail/<int:pk>", DriverDetailView.as_view(), name="driver_detail"),  # NOQA E501
]

app_name = "taxi"
