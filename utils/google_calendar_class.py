import os.path
import datetime as dt

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

URL_SECRET ="credencials/client_secret_947001387045-oogkeol9u9q6h310tp21kh70keq69uj9.apps.googleusercontent.com.json"

ID_CALENDAR_SCANNDATA = "877e2e0c52be766e8519adf76439cf407942d34642f7e3b6324eb0ea8618a4af@group.calendar.google.com"

class GoogleCalendarManager:
    def __init__(self):
        self.service = self._authenticate()

    def _authenticate(self):
        creds = None

        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(URL_SECRET, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return build("calendar", "v3", credentials=creds)

    def list_upcoming_events(self, max_results=10):
        now = dt.datetime.now(dt.timezone.utc).isoformat()
        tomorrow = (dt.datetime.now() + dt.timedelta(days=30)).replace(hour=23, minute=59, second=0, microsecond=0).isoformat() + "Z"

        events_result = self.service.events().list(
            calendarId=ID_CALENDAR_SCANNDATA, timeMin=now, timeMax=tomorrow,
            maxResults=max_results, singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        else:
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'],event['id'])
        
        return events

    def create_event(self, summary, start_time, end_time, timezone='America/Santiago', attendees=None):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time,
                'timeZone': timezone,
            }
        }

        if attendees:
            valid_attendees = [email for email in attendees if email.strip()]
            if valid_attendees:
                event["attendees"] = [{"email": email} for email in valid_attendees]
        
        try:
            event = self.service.events().insert(calendarId=ID_CALENDAR_SCANNDATA, body=event).execute()
            print(f"Event created: {event.get('htmlLink')}")
        except HttpError as error:
            print(f"An error has occurred: {error}")

    def update_event(self, event_id, summary=None, start_time=None, end_time=None):
        event = self.service.events().get(calendarId=ID_CALENDAR_SCANNDATA, eventId=event_id).execute()

        if summary:
            event['summary'] = summary

        if start_time:
            event['start']['dateTime'] = start_time

        if end_time:
            event['end']['dateTime'] = end_time

        updated_event = self.service.events().update(
            calendarId=ID_CALENDAR_SCANNDATA, eventId=event_id, body=event).execute()
        return updated_event

    def delete_event(self, event_id):
        self.service.events().delete(calendarId=ID_CALENDAR_SCANNDATA, eventId=event_id).execute()
        return True
    

# calendar = GoogleCalendarManager()

# #calendar.list_upcoming_events()
# from datetime import datetime


# fecha_actual = datetime.now().strftime('%Y-%m-%d')
# print(fecha_actual)
# calendar.create_event(
#     summary="Hola youtube",
#     start_time=f"{fecha_actual}T12:36:00",
#     end_time=f"{fecha_actual}T13:30:00",
#     timezone="America/Santiago",
#     attendees=["acordesamarrillos555@gmail.com","pedro@gmail.com"]
# )

# calendar.list_upcoming_events()