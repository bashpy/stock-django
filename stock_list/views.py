from django.shortcuts import render
from stock_list.models import moneycontrol
# Create your views here.
def list(request):
    datas=moneycontrol.objects.order_by("COMPANY")
    return render(request, 'money_control.html', {'datas': datas})