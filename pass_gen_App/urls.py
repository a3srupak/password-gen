from django.urls import path
from pass_gen_App import views
urlpatterns = [
    #login
    path('', views.login,name='login'),
    path('login/', views.login,name='login'),
    path('login_submit/', views.login_submit, name='login_submit'),
    #logout
    path('User_RegiterSubmit/', views.User_RegiterSubmit, name='User_RegiterSubmit'),
    # path('logout/', views.logout,name='logout'),
    #path('password/', views.password, name="password"),
    path('listpass/', views.listpass, name="listpass"),
    path('deletepass/<str:id>/', views.deletepass, name="deletepass"),
    path('backlistdata/', views.backlistdata, name="backlistdata"),
    path('addpass/', views.addpass, name="addpass"),
    path('listpass_submit/', views.listpass_submit, name="listpass_submit"),

]