from django.urls import path
from . import views

# http://127.0.0.1:8000/admin/staff/item/
# http://127.0.0.1:8000/portal/list/
# http://127.0.0.1:8000/portal/new/
urlpatterns = [
    path("list/", views.staff_list, name="staff_list"),
    path("user/<int:user_id>/", views.staff_detail, name="staff_detail"),
    path("new/", views.employee_create, name="employee_create"),
]
