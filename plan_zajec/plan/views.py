from django.shortcuts import render, get_object_or_404, redirect
from .models import Plan
from .forms import PlanForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import RedirectView

def view_plan(request):
    plan_list = Plan.objects.all()
    return render(request, 'plan/view_plan.html', {'plan_list': plan_list})

def edit_plan(request, entry_id=None):
    entry = get_object_or_404(Plan, pk=entry_id) if entry_id else None
    form = PlanForm(request.POST or None, instance=entry)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('view_plan')

    return render(request, 'plan/edit_plan.html', {'form': form, 'entry': entry})


class CustomLoginView(LoginView):
    template_name = 'plan/login.html'
    redirect_authenticated_user = True

class RedirectToPlanView(RedirectView):
    url = reverse_lazy('view_plan')