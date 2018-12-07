from django.shortcuts import render
from .models import ItemRequest

# Create your views here.
from chartit import DataPool, Chart

def item_requests_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    itemsdata = \
        DataPool(
           series=
            [{'options': {
               'source': ItemRequest.objects.all()},
              'terms': [
                'month',
                ]}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = itemsdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'Item Requests'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})
