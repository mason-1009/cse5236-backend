"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.core.exceptions import ValidationError

# Import subapplication routers and create the master API
from ninja import NinjaAPI
from accounts.api import router as accounts_router
from workouts.api import router as workouts_router
from nutrition.api import router as nutrition_router

from backend.auth import APIKeyAuth
from backend.errors import NotSuperUserError

api = NinjaAPI(auth=APIKeyAuth())

api.add_router('/accounts/', accounts_router)
api.add_router('/workouts/', workouts_router)
api.add_router('/nutrition/', nutrition_router)

@api.exception_handler(ValidationError)
def validation_error(request, exc):
    return api.create_response(
        request,
        {'detail': str(exc)},
        status=400
    )

@api.exception_handler(NotSuperUserError)
def not_super_user_error(request, exc):
    return api.create_response(
        request,
        {'detail': 'User needs to be superuser'},
        status=401
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
