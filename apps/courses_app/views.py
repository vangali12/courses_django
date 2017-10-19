# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def create(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
		return redirect('/')


def index(request):
	return render(request, 'courses_app/index.html', { "courses": Course.objects.all() })

# def create(request):
# 	Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
# 	return redirect('/')

def destroy(request, id):
	return render(request, 'courses_app/deletePage.html', { "course": Course.objects.get(id=id) })

def destroyCourse(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')