from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
