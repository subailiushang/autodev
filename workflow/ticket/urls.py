from django.urls import path
from ticket import views
from ticket.process import tickets, projects

urlpatterns = [
    path('index', tickets.inex, name='index'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('register', views.userregister, name='register'),

    path('create_tickets', tickets.create_ticket, name='create_tickets'),
    path('ticket_modal', tickets.ticket_modal, name='ticket_modal'),

    path('projects', projects.projects, name='projects'),
    path('create_projects', projects.create_projects, name='create_projects'),
]
