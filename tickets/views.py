from django.shortcuts import render

from .models import Ticket 
from .forms import TicketForm
# Create your views here.

def ticket_create_view(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TicketForm()

    context = {
        'form': form
    }
    return render(request, "ticket/ticket_create.html", context)

def ticket_detail_view(request):
    obj = Ticket.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description, 
    #     'priority': obj.priority
    # }
    context = {
        'object': obj
    }
    return render(request, "ticket/ticket_detail.html", context)

    # def ticket_create_view (request):
#     my_ticket_form = RawTicketForm()
#     if request.method == 'POST':
#         my_ticket_form = RawTicketForm(request.POST)
#         if my_ticket_form.is_valid:
#             print(my_ticket_form.cleaned_data)
#             Ticket.objects.create(**my_ticket_form.cleaned_data)
#         else:
#             print(my_ticket_form.errors)
#     context = {
#         "form": my_ticket_form
#     }
#     return render(request, "ticket/ticket_create.html", context)