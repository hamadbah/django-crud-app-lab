from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Hero, Enemy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WeaponForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HeroCreate(LoginRequiredMixin, CreateView):
    model = Hero
    fields = ['name', 'breed', 'description', 'age','image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user #form.instance.user mean user field in cat model
        return super().form_valid(form)
    
class HeroUpdate(LoginRequiredMixin, UpdateView):
    model = Hero
    fields = ['name', 'breed', 'description', 'age']
    
class HeroDelete(LoginRequiredMixin, DeleteView):
    model = Hero
    success_url = '/superhero/' 
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

@login_required
def hero_index(request):
    heros = Hero.objects.all() # equal to select * from main_app_cat;
    return render(request,'superhero/index.html', {'heros':heros})

@login_required
def hero_detail(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    enemies_hero_doesnt_have = Enemy.objects.exclude(id__in = hero.enemies.all().values_list('id'))
    weapon_form = WeaponForm()
    return render(request,'superhero/detail.html', {'hero' : hero, 'weapon_form': weapon_form, 'enemies': enemies_hero_doesnt_have})

@login_required
def add_weapon(request, hero_id):
    form = WeaponForm(request.POST)
    if form.is_valid():
        new_waepon = form.save(commit=False)
        new_waepon.hero_id = hero_id
        new_waepon.save()
    return redirect('detail', hero_id = hero_id)

class EnemyList(LoginRequiredMixin, ListView):
    model = Enemy
    
class EnemyDetail(LoginRequiredMixin, DetailView):
    model = Enemy
    
class EnemyCreate(LoginRequiredMixin, CreateView):
    model = Enemy
    fields = ['name','attack_power','speed']
    # fileds = '__all__' # Mean all the Fields
    
class EnemyUpdate(LoginRequiredMixin, UpdateView):
    model = Enemy
    fields = ['name','attack_power','speed']

class EnemyDelete(LoginRequiredMixin, DeleteView):
    model = Enemy
    success_url = '/enemies/'

@login_required
def assoc_enemy(request, hero_id, enemy_id):
    Hero.objects.get(id=hero_id).enemies.add(enemy_id)
    return redirect('detail', hero_id=hero_id)

@login_required
def unassoc_enemy(request, hero_id, enemy_id):
    Hero.objects.get(id=hero_id).enemies.remove(enemy_id)
    return redirect('detail', hero_id=hero_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup - Please try again later'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)