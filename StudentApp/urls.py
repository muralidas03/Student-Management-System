from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.loginFunc,name='loginFunc'),
    path('registerFunc',views.registerFunc,name='registerFunc'),
    path('add',views.home,name='add'),
    path('homePage',views.homePage,name='homePage'),
    path('edit/<int:id>',views.editDetails,name='edit'),
    path('delete/<int:id>',views.deleteDetails,name='delete'),
    path('dummy',views.dummy,name='dummy'),
    path('logout',views.logoutFunc,name="logout"),
    path('search',views.search,name='search')
]