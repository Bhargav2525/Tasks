from django.shortcuts import redirect,render
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow,InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from django.http import HttpResponse
'''def callback(request):
    state = request.session.get('state')
    flow = Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar.events'],
        state=state
    )
    flow.redirect_uri = 'http://localhost:8000/callback'  # Your redirect URL
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials

    # Use the obtained credentials to interact with the Google Calendar API
    service = build('calendar', 'v3', credentials=credentials)
    events_result = service.events().list(calendarId='primary', maxResults=15).execute()
    events = events_result.get('items', [])

    # Process fetched events as needed
    for event in events:
        print(event['summary'])

    return render(request, 'callback.html', {'events': events})
# This view initiates the OAuth 2.0 flow'''

'''def index(request):
    return render(request, "eventapp/index.html") '''

def auth(request):
    scopes=['https://www.googleapis.com/auth/calendar.events']
    flow  = InstalledAppFlow.from_client_secrets_file("client_secret.json",scopes = scopes)
    flow.run_local_server(success_message= " Authorization Susccessful. You can close this tab now.")
    flow.redirect_uri = 'http://localhost:8080/'
    
    service = build('calendar', 'v3', credentials = flow.credentials)
    events_list = service.events().list(calendarId='primary').execute()
    d = dict()
    for i,event in enumerate(events_list.get('items', [])):
        event_description = event.get('summary')
        d[i+1] = event_description
    return render(request, "eventapp/callback.html", {"events" : d})
    

    



