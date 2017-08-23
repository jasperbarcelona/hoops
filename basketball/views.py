from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.template import loader, Context
from basketball.models import User, Team, UserTeam, Game, Court
from django.views.decorators.csrf import csrf_exempt 
from django.forms.models import model_to_dict
import validators as validate
import pyping
import json

@csrf_exempt
@validate.form_data(params=['user_name', 'email', 'msisdn', 'city', 'region',
	'country', 'height'])
def create_user(request):
	data = request.POST.dict()
	user = User(
		user_name=data['user_name'],
		email=data['email'],
		msisdn=data['msisdn'],
		city=data['city'],
		region=data['region'],
		country=data['country'],
		height=data['height']
		)
	user.save()
	return JsonResponse({
		'status': 'success',
		'user': model_to_dict(user)
		}, status=201)

# validate data
# validate user_exist
@csrf_exempt
def get_user(request):
	data = request.GET.dict()
	user = User.objects.filter(id=data['id']).first()
	if not user:
		return JsonResponse({
			'status': 'failed',
			'message': 'User not found.'
			}, status=404)
	return JsonResponse({
		'status': 'success',
		'user': model_to_dict(user)
		}, status=200)

@csrf_exempt
def create_game(request):
	data = request.POST.dict()
	new_game = Game(
		status=data['status'],
		court_id=data['court_id'],
		court_name=data['court_name'],
		date=data['date'],
		time=data['time'],
		created_by_user_id=data['created_by_user_id'],
		created_by_user_name=data['created_by_user_name'],
		game_type=data['game_type']
	)
	new_game.save()
	return JsonResponse({
		'status': 'success',
		'game': model_to_dict(new_game)
		}, status=201)

