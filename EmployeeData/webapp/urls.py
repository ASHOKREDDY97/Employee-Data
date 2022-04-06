from django.urls import path  
from .import views

urlpatterns = [  
    path('', views.index,name='index'),
    path('addnew',views.addnew,name='addnew'),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.destroy),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('upload/', views.dataupload),
    path('inactive_employees',views.inactive_employees,name='inactive_employees'),
    path('submit',views.submit,name='submit'),
    
]