from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from .models import Chart
import json
from django.shortcuts import render  # Corrected typo here
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'  # Update with the correct path to your login template

    def form_valid(self, form):
        # Call the base class form_valid to perform the actual login
        super().form_valid(form)
        # Check if the logged-in user is a staff member
        if self.request.user.is_staff:
            # Redirect to the charts view if user is staff
            return HttpResponseRedirect(reverse('charts'))  # Replace with your charts URL name
        else:
            # Redirect non-admin users to a different page
            return HttpResponseRedirect(reverse('index'))  # Replace with the URL name for non-admin users
 
class ChartChartView(LoginRequiredMixin, TemplateView):
    template_name = 'charts/charts.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        charts = Chart.objects.all().order_by('meal')
        labels = [chart.meal for chart in charts]
        values = [chart.rating_amount for chart in charts]
        backgroundColors = [f'rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.7)' for _ in values]

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": 'Bar Chart',
                "data": values,
                "backgroundColor": backgroundColors,
                "borderWidth": 1,
            }]
        }

        context['chart_data'] = json.dumps(chart_data)
        return context

# These should be outside the ChartChartView class
def pie_chart(request):
    charts = Chart.objects.all().order_by('meal')
    labels = [chart.meal for chart in charts]
    values = [chart.rating_amount for chart in charts]

    # Generate a random color for each meal
    colors = [f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for _ in charts]

    # Pass the data and colors to the template
    context = {
        'chart_data': json.dumps({
            'labels': labels,
            'data': values,
            'backgroundColor': colors,
        })
    }
    return render(request, 'charts/pie_chart.html', context)

def line_chart(request):
    charts = Chart.objects.all().order_by('meal')  # Assuming 'meal' has a sequential order for demonstration
    labels = [chart.meal for chart in charts]
    values = [chart.rating_amount for chart in charts]
    
    # Generate a random border color for the chart
    border_color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'

    # Convert data to JSON because we will pass it in the context
    chart_data = json.dumps({
        "labels": labels,
        "values": values,
        "borderColor": border_color,
        "fill": False,
        "tension": 0.1
    })

    return render(request, 'charts/line_chart.html', {'chart_data': chart_data})

def doughnut_chart(request):
    # Fetching data from the database
    charts = Chart.objects.all().order_by('meal')
    labels = [chart.meal for chart in charts]
    values = [chart.rating_amount for chart in charts]

    # Generating a random color for each data point
    backgroundColors = [f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for _ in values]

    chart_data = json.dumps({
        "labels": labels,
        "datasets": [{
            "label": "value",
            "data": values,
            "backgroundColor": backgroundColors,
            "hoverOffset": 4
        }]
    })

    return render(request, 'charts/doughnut_chart.html', {'chart_data': chart_data})

def polar_area_chart(request):
    charts = Chart.objects.all().order_by('meal')  # Assuming 'meal' represents categories
    labels = [chart.meal for chart in charts]
    values = [chart.rating_amount for chart in charts]

    # Generating random colors for each segment
    backgroundColors = [f'rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)' for _ in values]

    chart_data = json.dumps({
        "labels": labels,
        "datasets": [{
            "label": "My First Dataset",
            "data": values,
            "backgroundColor": backgroundColors,
        }]
    })

    return render(request, 'charts/polar_area_chart.html', {'chart_data': chart_data})
