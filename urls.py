"""
URL configuration for courrier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from accounts.views import login_view, logout_view, register
from Dashboard.views import courrier, create_rappel, delete_rappel, details_courrier, index, update_rappel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login"),
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('index/', index, name="index"),
    path('courrier', courrier, name="courrier"),
    path('courrier/<int:courrier_id>/', details_courrier, name='details_courrier'),
    path('rappel/create/<int:courrier_id>', create_rappel, name='create_rappel'),
    path('rappel/update/<int:rappel_id>/', update_rappel, name='update_rappel'),
    path('rappel/delete/<int:rappel_id>/', delete_rappel, name='delete_rappel'),

]
