from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .helpers import get_blocks, get_block
from .models import Block
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def update_blocks(date: datetime):
    date_for_blocks = date if date else datetime.today()
    for block in get_blocks(date):
        context = {
            'hash': block['hash'],
            'timestamp': block['timestamp'],
            'miner': block['miner'],
            'transactions_count': block['transactionCount'],
            'date': date_for_blocks
        }
        block_height = block['height']
        if Block.objects.filter(height=block_height).exists():
            existing_block = Block.objects.get(height=block_height)
            if existing_block.auto_update:
                Block.objects.filter(height=block_height).update(**context)
        else:
            context['height'] = block_height
            obj = Block.objects.create(**context)
            obj.refresh_from_db()


class AllBlocksView(View):
    def get(self, request):
        update_blocks(date='')
        blocks_list = Block.objects.all().order_by('-height')
        today = datetime.now().strftime('%Y-%m-%d')
        paginator = Paginator(blocks_list, 50)
        page = request.GET.get('page')
        try:
            blocks = paginator.page(page)
        except PageNotAnInteger:
            blocks = paginator.page(1)
        except EmptyPage:
            blocks = paginator.page(paginator.num_pages)
        return render(request, 'blocks/all_blocks.html', {'blocks': blocks, 'today': today})

    def post(self, request):
        date_for_blocks = request.POST['date-for-blocks']
        date = datetime.strptime(date_for_blocks, '%Y-%m-%d')
        return redirect(f"/{date.year}-{date.month}-{date.day}")


class DayBlocksView(View):
    def get(self, request, date):
        try:
            date_dt = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return HttpResponse('Неверный формат даты!')
        update_blocks(date=date_dt)
        blocks_list = Block.objects.filter(date=date_dt).order_by('-height')
        today = date_dt.strftime('%Y-%m-%d')
        paginator = Paginator(blocks_list, 50)
        page = request.GET.get('page')
        try:
            blocks = paginator.page(page)
        except PageNotAnInteger:
            blocks = paginator.page(1)
        except EmptyPage:
            blocks = paginator.page(paginator.num_pages)
        return render(request, 'blocks/all_blocks.html', {'blocks': blocks, 'today': today})

    def post(self, request, date):
        date_for_blocks = request.POST['date-for-blocks']
        date = datetime.strptime(date_for_blocks, '%Y-%m-%d')
        return redirect(f"/{date.year}-{date.month}-{date.day}")


class BlockDetailView(View):
    def get(self, request, block_height):
        if Block.objects.filter(height=block_height).exists():
            block = Block.objects.get(height=block_height)
        elif get_block(block_height):
            block_info = get_block(block_height)
            context = {
                'hash': block_info['hash'],
                'timestamp': block_info['timestamp'],
                'miner': block_info['miner'],
                'transactions_count': len(block_info["transactions"]),
                'height': block_info['height']
            }
            block = Block.objects.create(**context)
        else:
            return HttpResponse(f'Блок высотой {block_height} не найден!')
        return render(request, 'blocks/block_detail.html', {'block': block})
