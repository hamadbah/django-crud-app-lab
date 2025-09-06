from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Hero, Enemy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WeaponForm

class HeroCreate(CreateView):
    model = Hero
    fields = ['name', 'breed', 'description', 'age','image']
    
class HeroUpdate(UpdateView):
    model = Hero
    fields = ['name', 'breed', 'description', 'age']
    
class HeroDelete(DeleteView):
    model = Hero
    success_url = '/superhero/' 
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def hero_index(request):
    heros = Hero.objects.all() # equal to select * from main_app_cat;
    return render(request,'superhero/index.html', {'heros':heros})

def hero_detail(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    enemies_hero_doesnt_have = Enemy.objects.exclude(id__in = hero.enemies.all().values_list('id'))
    weapon_form = WeaponForm()
    return render(request,'superhero/detail.html', {'hero' : hero, 'weapon_form': weapon_form, 'enemies': enemies_hero_doesnt_have})

def add_weapon(request, hero_id):
    form = WeaponForm(request.POST)
    if form.is_valid():
        new_waepon = form.save(commit=False)
        new_waepon.hero_id = hero_id
        new_waepon.save()
    return redirect('detail', hero_id = hero_id)

class EnemyList(ListView):
    model = Enemy
    
class EnemyDetail(DetailView):
    model = Enemy
    
class EnemyCreate(CreateView):
    model = Enemy
    fields = ['name','attack_power','speed']
    # fileds = '__all__' # Mean all the Fields
    
class EnemyUpdate(UpdateView):
    model = Enemy
    fields = ['name','attack_power','speed']

class EnemyDelete(DeleteView):
    model = Enemy
    success_url = '/enemies/'

def assoc_enemy(request, hero_id, enemy_id):
    Hero.objects.get(id=hero_id).enemies.add(enemy_id)
    return redirect('detail', hero_id=hero_id)

def unassoc_enemy(request, hero_id, enemy_id):
    Hero.objects.get(id=hero_id).enemies.remove(enemy_id)
    return redirect('detail', hero_id=hero_id)