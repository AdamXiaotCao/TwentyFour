from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.core import serializers

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required
# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from mimetypes import guess_type
from django.db import IntegrityError

from models import *
from forms import *
# from py_expression_eval import Parser
import cardGeneration
import re

@transaction.atomic
@login_required
def home(request):
    context = {}
    myuser = request.user
    print myuser.first_name
    context['myuser'] = get_object_or_404(User,id = myuser.id)
    context['records'] = Record.objects.filter(player=myuser.player)
    context['player'] = myuser.player
    return render(request, 'home.html',context)


@transaction.atomic
@login_required
def single_game(request):
    context = {}
    card_img=["cards/1.png", "cards/2.png", "cards/3.png",
              "cards/4.png", "cards/5.png", "cards/6.png",
              "cards/7.png", "cards/8.png", "cards/9.png",
              "cards/10.png"]
    myuser = request.user
    context['myuser'] = myuser

    newcardset = cardGeneration.generateSet()
    context['newset'] = newcardset

    context['newset1']= card_img[newcardset[0]-1]
    context['newset2']= card_img[newcardset[1]-1]
    context['newset3']= card_img[newcardset[2]-1]
    context['newset4']= card_img[newcardset[3]-1]

    context['num1'] = newcardset[0]
    context['num2'] = newcardset[1]
    context['num3'] = newcardset[2]
    context['num4'] = newcardset[3]

    return render(request, 'game_screen.html',context)

@login_required
@transaction.atomic
def determine_result(request):
    # p = Parser()
    context = {}
    card_img=["cards/1.png", "cards/2.png", "cards/3.png",
              "cards/4.png", "cards/5.png", "cards/6.png",
              "cards/7.png", "cards/8.png", "cards/9.png",
              "cards/10.png"]
    # output = p.evaluate(request.POST['input'],{})
    output = eval(request.POST['input'],{})

    input_text = request.POST['input'].encode('ascii')

    str_input = re.findall('\d+', input_text)
    int_input = [int(i) for i in str_input]

    context['myuser'] =request.user
    newcardset = cardGeneration.generateSet()
    context['newset'] = newcardset
    context['newset1']= card_img[newcardset[0]-1]
    context['newset2']= card_img[newcardset[1]-1]
    context['newset3']= card_img[newcardset[2]-1]
    context['newset4']= card_img[newcardset[3]-1]


    context['player']=request.user.player
    cardnum = []

    n1 = int(request.POST['n1'])
    n2 = int(request.POST['n2'])
    n3 = int(request.POST['n3'])
    n4 = int(request.POST['n4'])

    cardnum.append(n1)
    cardnum.append(n2)
    cardnum.append(n3)
    cardnum.append(n4)

    print int_input
    print cardnum

    context['num1'] = newcardset[0]
    context['num2'] = newcardset[1]
    context['num3'] = newcardset[2]
    context['num4'] = newcardset[3]


    context['result'] = False
    context['output'] = output
    context['feedback'] = ''
    player = request.user.player
    playerstate= PlayerState.objects.get(player=player)
    game = playerstate.gamestate.game
    context['game_status'] =game.status
    game_id = game.id
    context['game'] =game
    context['game_id']=game_id
    load = 'game_screen.html'
    if request.POST['page'] == 'many':
        load = 'many_player_game.html'
    if ((set(int_input) == set(cardnum)) and output == 24.0):
        context['result'] = True
        context['feedback'] = 'You got it right! +3 Points!'
        playerstate.point += 3
        playerstate.save()

    else:
        context['feedback'] = 'You got it wrong!!! -2 Point'
        playerstate.point -= 2
        playerstate.save()
    playerstate.progress += 1
    playerstate.save()
    return render(request,load,context)


@transaction.atomic
def register(request):
    # Just display the registration form if this is a GET request
    context = {}
    if request.method =='GET':
            # context['login_form'] = LoginForm()
            context['registration_form'] = RegistrationForm()
            return render(request, 'register.html',context)
    errors = []
    context['errors'] = errors
    form = RegistrationForm(request.POST, request.FILES)
    print (request.POST)
    if 'form' in request.POST:
        if request.POST['form']=="login":
            print("here")
            login_form = LoginForm(request.POST)
            if not login_form.is_valid():
                context['login_form'] = LoginForm()
                context['registration_form'] = RegistrationForm()
                return render(request, 'login.html',context)
        elif request.POST['form']=="register":
            if not form.is_valid():
                context ['registration_form'] = RegistrationForm()
                context ['login_form']=LoginForm()
                return render(request, 'register.html',context)
    if not form.is_valid():
        return render(request, 'register.html', context)
    # Creates the new user from the valid form data

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'],email=form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'])
    # new_user.is_active=False
    new_user.save()
    new_user = authenticate(username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
    new_person = Player(user=new_user, picture=form.cleaned_data['picture'])
    new_person.save()
    login(request, new_user)
    return redirect(reverse('home'))


def get_photo(request, id):
    player = get_object_or_404(Player, id=id)
    if not player.picture:
        raise Http404
    print player.picture
    content_type = guess_type(player.picture.name)
    return HttpResponse(player.picture, content_type=content_type)

@transaction.atomic
@login_required
def lobby(request):
    context = {}
    games = Game.objects.filter(status=True)
    context['games'] = games
    context['user'] = request.user
    return render(request, 'lobby.html', context)

@transaction.atomic
@login_required
def create_multigame(request):
    owner = request.user
    card_sets = []
    new_game = Game(status = 'WAIT')
    new_game.save()
    new_game.participants.add(owner.player)
    x = 0

    context = {}
    context['game']=new_game
    context['user']=owner
    context['player']= owner.player
    errors = []

    newcardset=cardGeneration.generateSet()
    new_card_set = Cardset()
    new_card_set.save()
    for value in newcardset:
        new_card = Card(value=value)
        new_card.save()
        new_card_set.cards.add(new_card)
        new_card_set.save()

    new_game.card_sets.add(new_card_set)
    new_game.save()

    context['image']="cards/1.png"

    context['newset'] = newcardset

    context['num1'] = newcardset[0]
    context['num2'] = newcardset[1]
    context['num3'] = newcardset[2]
    context['num4'] = newcardset[3]

    context['errors'] = errors

    context['game_status'] = new_game.status

    context['game_id'] = new_game.id

    participants = new_game.participants.all()
    context['participants'] = participants
    context['owner'] =participants[0]
    return render(request,'many_player_game.html',context)


@login_required
def get_players(request,id):
    #this method is used for responding jQuery request
    #it should send back all players in the
    game_id = id
    game = Game.objects.get(id=game_id)
    participants = game.participants.all()
    participants_text = serializers.serialize("json",participants)
    return HttpResponse(participants_text, content_type = "application/json") #content type?

@login_required
def check_game(request,id):
    game_id = id
    game = Game.objects.get(id=game_id)

    status_text = serializers.serialize("json",[game])
    return HttpResponse(status_text,content_type = "application/json")


@transaction.atomic
@login_required
def get_progress(request,id):
    #this method is used for responding jQuery request
    #it should send back httpresponse
    #it is for player to see other players' progress
    #the front end needs to collect other players progress
    game_id = id
    game = Game.objects.get(id =game_id)
    participants = game.participants.all()
    states = []
    for p in participants:
        state = PlayerState.objects.get(player=p)
        states.append(state)
    states_text = serializers.serialize("json",states)
    return HttpResponse(states_text,content_type="application/json")

@transaction.atomic
@login_required
def get_games(request):
    #this method responds to jQuery request
    #it is for updating the lobby to display
    #newly created game
    games = Game.objects.filter(status = 'WAIT')
    games_text = serializers.serialize("json",games)

    return HttpResponse(games_text,content_type = "application/json")

@login_required
def start_multigame(request):
    context = {}
    game_id = request.GET['game_id']

    newcardset = request.GET['newset']

    print newcardset

    game = Game.objects.get(id=game_id)
    game.status='ONGOING'
    context['game_status'] = 'ONGOING'
    game.save()
    gamestate= GameState(game=game)
    gamestate.save()
    participants= game.participants.all()
    context['game_id']=game_id

    card_img=["cards/1.png", "cards/2.png", "cards/3.png",
              "cards/4.png", "cards/5.png", "cards/6.png",
              "cards/7.png", "cards/8.png", "cards/9.png",
              "cards/10.png"]

    context['newset1']= card_img[int(request.GET['num1'])-1]
    context['newset2']= card_img[int(request.GET['num2'])-1]
    context['newset3']= card_img[int(request.GET['num3'])-1]
    context['newset4']= card_img[int(request.GET['num4'])-1]

    context['num1'] = request.GET['num1']
    context['num2'] = request.GET['num2']
    context['num3'] = request.GET['num3']
    context['num4'] = request.GET['num4']
    player_states = []
    for p in participants:
        try:
            player_states.append(PlayerState(player=p,gamestate=gamestate).save())
        except IntegrityError as e:
            ps = PlayerState.objects.get(player=p)
            ps.delete()
            player_states.append(PlayerState(player=p,gamestate=gamestate).save())
    context['game']=game
    context['user'] = request.user
    return render(request,'many_player_game.html',context)

@transaction.atomic
@login_required
def update_multigame(request):
    #whenever a player submits an answer, it will call this action, which will update game state
    game_id = request.GET['game_id']
    game = Game.objects.filter(id= game_id)
    output = eval(request.POST['input'],{})
    point = 0
    context={}
    context['user'] = request.user
    if output == 24.0:
        point = 1
        context['result'] = True
        context['feedback'] = 'You got it right!'
    else:
        context['feedback'] = 'You got it wrong!!!'
    context['point']=point
    game_state = game.gamestate
    player_state = PlayerState.objects.filter(player=request.user.player)
    player_state.point+=point
    player_state.save()
    context['player_state']=player_state
    return render(request,'many_player_game.html',context)

@transaction.atomic
@login_required
def end_game(request,id):
    context ={}
    game_id = id
    game = Game.objects.get(id= game_id)
    game.status = 'END'
    player = request.user.player
    participants = game.participants.all()
    gs = game.gamestate
    ps = PlayerState.objects.filter(gamestate=gs).all()
    context['game_state'] = gs
    context['player_state'] = ps
    context['participants'] = participants
    context['player'] = player
    player_names = []
    player_points = []
    context['player_states'] = ps
    winnerid=ps[0].player.id
    winnerpoint = 0
    for p in ps:
        player_names.append(p.player.user.first_name)
        player_points.append(p.point)
        if p.point > winnerpoint:
            winnerid = p.player.id
        p.player.total_points += p.point
        p.player.save()
        p.player.total_games_played += 1
        p.player.save()
    winner = Player.objects.get(id=winnerid)
    winner.total_games_won += 1
    winner.save()
    context['winner']=winner
    context['winner_point'] = winnerpoint

    context['player_total_points'] = player.total_points
    context['player_total_games'] = player.total_games_played
    print participants
    return render(request,'game_end.html',context)
@transaction.atomic
@login_required
def join_multigame(request,id):
    context= {}
    errors =[]
    new_user = request.user
    context['player'] = request.user.player

    card_img=["cards/1.png", "cards/2.png", "cards/3.png",
              "cards/4.png", "cards/5.png", "cards/6.png",
              "cards/7.png", "cards/8.png", "cards/9.png",
              "cards/10.png"]

    context['user']=new_user
    game_id = id
    game = Game.objects.get(id = game_id)
    game.participants.add(new_user.player)
    game.save()
    card_set = game.card_sets.all()[0]
    cards = card_set.cards.all()
    context['newset1']= card_img[int(cards[0].value)-1]
    context['newset2']= card_img[int(cards[1].value)-1]
    context['newset3']= card_img[int(cards[2].value)-1]
    context['newset4']= card_img[int(cards[3].value)-1]

    context['num1'] = cards[0].value
    context['num2'] = cards[1].value
    context['num3'] = cards[2].value
    context['num4'] = cards[3].value
    context['image']="cards/1.png"




    gamestate=GameState.objects.filter(game=game)
    context['game']=game
    context['game_status']=game.status
    context['game_id'] = game.id
    participants = game.participants.all()
    context['participants'] = participants
    context['owner'] =participants[0]
    context['errors'] = errors
    player_states = PlayerState.objects.filter(gamestate=gamestate).all()
    context['player_states']=player_states
    return render(request,'many_player_game.html',context)











