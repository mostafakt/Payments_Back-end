from django.contrib import admin
from django.urls import path, include
from .views import all_sallry, FBV_List, FBV_Id, PAIDS_List, PAID_Id, UserVeiwSet
from rest_framework.routers import DefaultRouter
import logging
urlpatterns = [

    path('api/', all_sallry),
    path('salary/', FBV_List),
    path('salary/<int:id>/', FBV_Id),
    path('paid/', PAIDS_List),


    path('paid/<int:id>/', PAID_Id),

]

router = DefaultRouter()
router.register(r'users', UserVeiwSet, basename='user')
urlpatterns += router.urls
logging.warning(router.get_routes)
 