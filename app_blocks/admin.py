from django.contrib import admin
from .models import Block


@admin.register(Block)
class ProfileAdmin(admin.ModelAdmin):
    """
    ./manage.py syncdb before start
    username: admin
    password: 123123
    """
    list_display = ['height', 'hash', 'timestamp', 'miner', 'transactions_count', 'date']
    model = Block
