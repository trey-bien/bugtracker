from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bugapp.models import Ticket, MyUser
from bugapp.forms import LoginForm, NewTicketForm

@login_required
def index_view(request):
    new_tickets = Ticket.objects.filter(ticket_status="N")
    completed_tickets = Ticket.objects.filter(ticket_status="C")
    invalid_tickets = Ticket.objects.filter(ticket_status="I")
    in_progress_tickets = Ticket.objects.filter(ticket_status="P")
    return render(request, "index.html", {
            "new_tickets": new_tickets, 
            "completed_tickets": completed_tickets,
            "invalid_tickets": invalid_tickets,
            "in_progress_tickets": in_progress_tickets,
        })

@login_required
def new_ticket_view(request):
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                filed_by=request.user,
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = NewTicketForm()
    return render(request, "generic_form.html", {"form":form})

@login_required
def edit_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("homepage"))
    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    form = NewTicketForm(initial=data)
    return render(request, "generic_form.html", {"form":form})      

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "generic_form.html", {"form":form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("homepage"))

def ticket_detail_view(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, "ticket_detail.html", {"ticket":ticket})

def user_detail_view(request, user_id):
    user = MyUser.objects.get(id=user_id)
    tickets_assigned = Ticket.objects.filter(assigned_to=user)
    tickets_filed = Ticket.objects.filter(filed_by=user)
    tickets_completed = Ticket.objects.filter(completed_by=user)
    return render(request, "user_detail.html", {"user": user, "tickets_assigned": tickets_assigned, "tickets_filed": tickets_filed, "tickets_completed": tickets_completed})

def in_progress_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'P'
    ticket.completed_by = None
    ticket.assigned_to = request.user
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))

def completed_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'C'
    ticket.completed_by = request.user
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))

def invalid_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = 'I'
    ticket.completed_by = None
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse("homepage"))

