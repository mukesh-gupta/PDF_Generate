from django.urls import path
from PdfApp import views
from django.views.generic import ListView


urlpatterns = [
    path('',views.index,name='index'),
    # path('pdf', views.pdf_file, name='pdf'),
    # path('data',views.Customer.as_view(),name='cust'),

path('page/<pk>',views.render_pdf,name='page'),
path('pdf/<pk>',views.pdf_generator,name='pdf'),
path('create',views.create,name='create')
]