# plan/urls.py
from django.urls import path
from .views import view_plan, edit_plan, CustomLoginView, RedirectToPlanView

urlpatterns = [
    path('view/', view_plan, name='view_plan'),
    path('edit/<int:entry_id>/', edit_plan, name='edit_plan'),
    path('edit/', edit_plan, name='add_plan'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Użyj '/accounts/login/' jako URL dla logowania
    path('login-success/', RedirectToPlanView.as_view(), name='login_success'),  # Przekierowanie po zalogowaniu
]
