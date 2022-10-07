from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Uzsakymas, Automobilis
from django.views import generic
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    kontekstas = {
        'paslaugu_kiekis': Paslauga.objects.all().count(),
        'atliktu_uzsakymu_kiekis': Uzsakymas.objects.filter(statusas__exact='i').count(),
        'automobiliu_kiekis': Automobilis.objects.all().count(),
    }
    return render(request, 'index.html', context=kontekstas)


def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all(), 3)
    page_number = request.GET.get('page')
    puslapiuoti_automobiliai = paginator.get_page(page_number)
    kontekstas = {
        'automobiliai': puslapiuoti_automobiliai,
    }
    return render(request, 'automobiliai.html', context=kontekstas)


def automobilis(request, automobilis_id):
    kontekstas = {
        'automobilis': get_object_or_404(Automobilis, pk=automobilis_id)
    }
    return render(request, 'automobilis.html', context=kontekstas)


class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 4


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
