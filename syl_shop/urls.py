"""syl_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token

from syl_shop.settings import MEDIA_ROOT
from apps.goods.views import GoodslistViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

import xadmin

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodslistViewSet,basename='goods')
# 配置Categroy的url
router.register(r'categorys',CategoryViewSet,basename="categorys")
from apps.users.views import SmsCodeViewset

# 配置codes的url
router.register(r'code', SmsCodeViewset, basename="code")

from apps.users.views import UserViewset
router.register(r'users',UserViewset,basename="users")

#配置用户收藏的url
router.register(r'userfavs',UserViewset,basename="userfavs")

#配置用户留言的url
from apps.user_operation.views import LeavingMessageViewset
router.register(r'messages', LeavingMessageViewset, basename="messages")

#配置收货地址
from apps.user_operation.views import AddressViewset
router.register(r'address',AddressViewset,basename='address')

#配置购物车的url
from apps.trade.views import ShoppingCartViewset
router.register(r'shopcarts',ShoppingCartViewset,basename='shopcarts')

#配置订单的url
from apps.trade.views import OrderViewset
router.register(r'orders', OrderViewset,basename="orders")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include("DjangoUeditor.urls")),
    #  文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # path('goods/',GoodsListView.as_view(),name= 'goods-list'),
    path('docs', include_docs_urls(title='仙剑奇侠传')),
    path('api-auth/', include('rest_framework.urls')),
    # 商品列表页
    re_path('^', include(router.urls)),
    # token
    path('api-token-auth/', views.obtain_auth_token),
    #jwt的token认证接口
    path('jwt-auth/', obtain_jwt_token ),
    # jwt的认证接口
    path('login/', obtain_jwt_token ),
]
