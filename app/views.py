from __future__ import print_function
from django.shortcuts import render, redirect
from Easycom import settings

# Create your views here.

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import pickle
import os.path
import pandas as pd



from django.core.files.storage import FileSystemStorage
from .forms import (
	DocumentForm,
  SalesDataForm,
  EasycomForm,
	)
from .models import (
	Document,
	SalesData,
  EasycomData,
	)
from openpyxl import load_workbook
import csv,  io

Scope = ['https://www.googleapis.com/auth/calendar.readonly']

def index(request):
	name = 'hemanth'
	return render(request, 'pages/index.html',{'name':name})


def googlecal_auth(request):
  credentials = None;
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      credentials = pickle.load(token)
  if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
      credentials.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(settings.jsondata ,Scope)
      credentials = flow.run_local_server()

    with open('token.pickle', 'wb') as token:
      pickle.dump(credentials,token)

  service = build('calendar','v3',credentials=credentials)
  now = datetime.datetime.utcnow().isoformat()+'Z'
  event_result =service.events().list(
    calendarId='primary', timeMin=now,
    maxResults=100, singleEvents=True,
    orderBy='startTime'
    ).execute()

  events = event_result.get('items',[])

  return render(request,'pages/calendar.html',{'events':events})


def fileupload(request):
    if request.method == 'POST':
        
        csv_file=request.FILES['file']
        if not csv_file.name.endswith('.csv'):
          print("not a csv file ")
        data_set =csv_file.read().decode('utf-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for col in csv.reader(io_string,delimiter=',', quotechar="|"):
          _, created = SalesData.objects.update_or_create(
           ordernum = col[0],
           sales_amount = col[1],
           cost_price = col[2],
           Trans_amount = col[3],
           Commission = col[4],
           Payment_charge = col[5],
           pickpack_fee = col[6]
           )
        
    return render(request, 'pages/fileupload.html', {
        
    })
	
def display_upload_data(request):

  s_data= SalesData.objects.all()
  for data in s_data:
    sp=data.sales_amount
    cp =data.cost_price
    c = data.Commission
    pa = data.Payment_charge
    ppf = data.pickpack_fee
    res = c+pa+ppf
    p_l = sp-(cp+res)

    result = EasycomForm().save(commit=False)
    result.ordernum = data.ordernum
    result.profit_loss_per = p_l
    result.Transferred_amount = data.Trans_amount
    result.Total_Mc = res
    result.save()
  final_result = EasycomData.objects.all()
  context = {'final_result':final_result}
  return render(request, "pages/display.html", context)

