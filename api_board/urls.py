from django.urls import path
from . import views

app_name = 'api_user'
urlpatterns = [
    path('', views.BoardView.as_view()),  # User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:id>', views.BoardView.as_view())
]
