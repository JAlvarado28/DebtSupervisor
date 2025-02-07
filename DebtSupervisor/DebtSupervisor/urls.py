"""DebtSupervisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app1 import views as app1_views
from addTransaction import views as addTransaction_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app1_views.home),
    path('home/',app1_views.home, name='home'),

    path('updateProfilePic/', app1_views.updateProfilePic, name='updateProfilePic'),

    path('addDebt/',app1_views.addDebt, name='addDebt'),
    path('debt/edit/<int:id>',app1_views.edit),

    path('afford/',app1_views.afford),
    path('result/', app1_views.calculate_affordability, name='calculate_affordability'),

    path('transaction/',addTransaction_views.transactions),
    path('transaction/addtransaction', addTransaction_views.add),
    path('transaction/edit/<int:id>',addTransaction_views.edit),

    path('join/', app1_views.join),
    path('login/', app1_views.user_login),
    path('logout/', app1_views.user_logout),

    path('debtstrategies/',app1_views.debtStrageties),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
