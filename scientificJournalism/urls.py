
from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
    path("login", views.logging_in, name="logging_in"),
    path("logout", views.logout, name="logout"),
    path('register', views.register, name='register'),
    path("registering", views.registering, name="registering"),
    path("activation", views.activation, name="activation"),
    path("writer", views.writer_homepage, name="writer_homepage"),
    path("new article", views.new_article, name="new_article"),
    path("submit article", views.submit_article, name="submit_article"),
    path("my articles", views.my_articles, name="my_articles"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("subscribing", views.subscribing, name="subscribing"),
    path("subscriber", views.subscriber_homepage, name="subscriber_homepage"),
    path("ajax/rate", views.rating_article, name="rating_article"),
    path("ajax/comment", views.commenting_article, name="commenting_article"),
    path("article/<int:article_ID>", views.show_article, name="show_article"),
    path("archived_article/<int:article_ID>", views.show_archived_article, name="show_archived_article"),
    path("article/<field>/", views.get_field_articles, name="get_field_articles"),
    path("article/archive/<field>/", views.get_archived_field_articles, name="get_archived_field_articles"),
    path("buy article/<int:article_ID>", views.buy_article, name="buy_article"), 
    path("online_search", views.online_search, name="online_search"),  
    path("archive_search", views.archive_search, name="archive_search"),  
    path("change_lang/<lang>/", views.change_lang, name='change_lang'),
    path("archive", views.archive, name='archive'),
    
    path("EIC homepage", views.EIC_homepage, name='EIC_homepage'),
    path("just_accept_article/<int:article_ID>", views.just_accept_article, name='just_accept_article'),
    path("accept_article_in_details", views.accept_article_in_details, name='accept_article_in_details'),
    path("reject_article", views.reject_article, name='reject_article'),
    path("assign_article", views.assign_article, name='assign_article'),
    path("grap_article/<int:article_ID>", views.grap_article, name='grap_article'),
    path("show_EIC_article/<int:article_ID>", views.show_EIC_article, name='show_EIC_article'),
    path("show_new_EIC_article/<int:article_ID>", views.show_new_EIC_article, name='show_new_EIC_article'),
 

    path("AE homepage", views.AE_homepage, name='AE_homepage'),
    path("AE_apologize/<int:article_ID>", views.AE_apologize, name='AE_apologize'),
    path("show_new_AE_article/<int:article_ID>", views.show_new_AE_article, name='show_new_AE_article'),
    path("invite_reviewer", views.invite_reviewer, name='invite_reviewer'),
    path('comment_article_as_AE', views.comment_article_as_AE, name='comment_article_as_AE'),
    path("grap_reviewer_article/<int:article_ID>", views.grap_reviewer_article, name='grap_reviewer_article'),
    path("show_AE_article/<int:article_ID>", views.show_AE_article, name='show_AE_article'),



    path("reviewer homepage", views.reviewer_homepage, name='reviewer_homepage'),
    path("show_new_reviewer_article/<int:article_ID>", views.show_new_reviewer_article, name='show_new_reviewer_article'),
    path("reviewer_apologize/<int:article_ID>", views.reviewer_apologize, name='reviewer_apologize'),
    path('comment_article_as_reviewer', views.comment_article_as_reviewer, name='comment_article_as_reviewer'),

    path('admin/statistics/', views.view_statistics, name='statistics'),
 
]



