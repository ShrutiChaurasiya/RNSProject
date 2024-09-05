from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login1,name="login"),
    path("login/",views.log,name="logout"),
    path("register/",views.register,name="register"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("contact/",views.contact,name="contact"),
    path("t_c/",views.t_c,name="t_c"),
    path('cart/<int:id>', views.cart, name="cart"),
	path("buy/",views.buy,name="buy"),
	path("rosesbuy/",views.rosesbuy,name="rosesbuy"),
    path('rosescart/', views.rosescart, name="rosescart"),
    path('wnmecart/', views.wnmecart, name="wnmecart"),
    path('somethingcart/', views.somethingcart, name="somethingcart"),
    path('gepiccart/', views.gepiccart, name="gepiccart"),


    #  admin site
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_homepg/', views.admin_homepg, name="admin_homepg"),
    path('update_book/<int:id>', views.update_book, name="update_book"),
    path('user_pg/', views.user_pg, name="user_pg"),
    path('update_user/<int:id>', views.update_user, name="update_user"),
    path('add_book/', views.add_book, name="add_book"),
    path("delete_book/<int:id>",views.delete_book,name="delete_book"),
    path("delete_user/<int:id>",views.delete_user,name="delete_user"),
     
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# user_pg pe koi link add nh hai
# user _pg view bhee banana hai