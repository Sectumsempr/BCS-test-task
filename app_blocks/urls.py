from django.urls import path
from .views import AllBlocksView, DayBlocksView, BlockDetailView


urlpatterns = [
    path('', AllBlocksView.as_view(), name='all_blocks'),
    path('<str:date>/', DayBlocksView.as_view(), name='all_blocks'),
    path('blocks/<int:block_height>/', BlockDetailView.as_view()),
]
