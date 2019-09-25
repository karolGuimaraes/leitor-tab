from django.shortcuts import render
from .models import Sale
from pandas import read_csv
from decimal import Decimal

def index(request):
    return render(request, 'index.html', {})

def importar_arquivo(request):
    file_upload = request.FILES.get('file_upload', False)
    revenue = 0
    if file_upload:
        try:
            file = read_csv(str(file_upload), delimiter='\t')
            for sale in file.values:
                Sale.objects.create(purchaser_name = sale[0], 
                                    item_description = sale[1], 
                                    item_price = sale[2], 
                                    purchase_count = sale[3], 
                                    merchant_address = sale[4], 
                                    merchant_name = sale[5])

                revenue += int(sale[3]) * Decimal(sale[2])
                
            return render(request, 'retorno.html', {'acao': 0, 'revenue': revenue, 'menssage':'ok', 'status': 200 })
        except Exception as error:
           return render(request, 'retorno.html', {'acao': -1, 'menssage': error, 'status': 500 })
    else:
        return render(request, 'retorno.html', {'acao': -1, 'menssage':'Nenhum arquivo selecionado.', 'status': 400})
