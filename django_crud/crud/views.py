from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django_tables2 import tables, SingleTableView, TemplateColumn
from .models import User


def index(request):
    return render(request, 'crud/index.html' )

class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ("id ", "name", "favorite_quote")
    update = TemplateColumn(verbose_name=('Action'),
                                    template_name='crud/update.html',
                                    orderable=False) # orderable not sortable

class UserListView(SingleTableView):
    model = User
    table_class = UserTable
    template_name = 'crud/listing.html'

def update(request):
    users = User.objects.order_by('date_created')[:5]
    template = loader.get_template('crud/update.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    # template = loader.get_template('crud/create.html')
    return render(request, 'crud/create.html')