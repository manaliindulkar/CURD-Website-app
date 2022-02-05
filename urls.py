from django.contrib import admin
from django.urls import path
from employee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginUser,name="login"),
    path('show',views.show ,name="show"),
    path('signup',views.handleSignUp,name="signup"),
    path('logout',views.user_logout,name='logout'),
    path('emp', views.emp),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]