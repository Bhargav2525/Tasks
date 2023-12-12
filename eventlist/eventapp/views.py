from django.shortcuts import redirect,render
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow,InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from django.http import HttpResponse



def index(request):
    return render(request, "eventapp/index.html") 

def auth(request):
    scopes=['https://www.googleapis.com/auth/calendar.events']
    flow  = InstalledAppFlow.from_client_secrets_file("client_secret.json",scopes = scopes)
    flow.run_local_server(success_message= " Authorization Susccessful. You can close this tab now.")
    flow.redirect_uri = 'http://localhost:8080/'
    # Building a service to use Calendar API with the login Credentials.
    service = build('calendar', 'v3', credentials = flow.credentials)
    # Getting the list of events from the service which was built.
    events_list = service.events().list(calendarId='primary').execute()
    # creating a dictionary to store only summaries in order.
    d = dict()
    for i,event in enumerate(events_list.get('items', [])):
        event_description = event.get('summary')
        d[i+1] = event_description
    return render(request, "eventapp/callback.html", {"events" : d})
    

    



