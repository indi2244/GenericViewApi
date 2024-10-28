from django.urls import path
from genericViews import views

urlpatterns = [
   path('list/',views.index),
   path('create/',views.create),
   path('update/<int:id>/',views.update),
   path('count/<int:id>/', views.student_by_id),
]