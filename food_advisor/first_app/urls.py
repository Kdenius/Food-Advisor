from django.urls import path

from . import views

urlpatterns=[
    path('create_person/', views.create_person, name='create_person'),
    path('person_list/', views.person_list, name='person_list'),
    path('create_advisor/', views.create_advisor, name='create_advisor'),
    path('advisor_list/', views.advisor_list, name='advisor_list'),
    path('create_item/', views.create_item, name='create_item'),
    path('item_list/', views.item_list, name='item_list'),
    path('favorite_list/',views.favorite_list,name='favorite_list'),
    path('create_report/', views.create_report, name='create_report'),
    path('report_list/', views.report_list, name='report_list'),
    path('home/',views.home,name='home'),
    path('',views.Login,name='Login'),
    path('logout/',views.Logout,name='Logout'),
    path('add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/',views.remove_from_favorites,name='remove_from_favorites'),
    path('mark_as_eaten/',views.mark_as_eaten,name='mark_as_eaten'),
    path('report_lists/',views.report_lists,name='report_lists'),
    path('set_target/',views.set_target,name='set_target'),
    path('about_us/',views.about_us,name='about_us'),
    path('feedback/',views.feedback,name='feedback'),
    path('home2/', views.home2, name='home2'),
    path('give_advice/', views.give_advice, name='give_advice'),
    path('add_advice/',views.add_advice, name='add_advice'),
    path('delete_advice/',views.delete_advice, name='delete_advice'),
]