from django.urls import path,include
from .views import decrement_add, first_api,create_user, get_add, get_balans, get_posts,get_step, increment_add,increment_step,set_phone

urlpatterns = [
    path('', first_api),
    path('create_user/', create_user),
    path('set_phone/<int:id>/', set_phone),

    path('get_balans/<int:id>/', get_balans),
    path('get_posts/<int:id>/', get_posts),

    path('get_step/<int:id>/', get_step),
    path('increment_step/<int:id>/', increment_step),

    path('get_add/<int:id>/', get_add),
    path('increment_add/<int:id>/', increment_add),
    path('decrement_add/<int:id>/', decrement_add),
]
