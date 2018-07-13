from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from administrator.forms import UserCreationForm2
from django.http import HttpResponse

def register(request):
	if request.method == 'POST':
		form = UserCreationForm2(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_staff = True
			user.save()
			return redirect('/admin/login')
		else:
			args = {'form': form}
			return render(request, 'administrator/reg_form.html', args)
	else:
		form = UserCreationForm2()
		args = {'form': form}
		return render(request, 'administrator/reg_form.html', args)

def login(request):
	return redirect('/admin/login')

#
# def add_to_calendar(sender, **kwargs):
#     print("hello")
#     e = kwargs['instance']
#     start_datetime = datetime.datetime.combine(e.event_start_date,e.event_start_time)
#     end_datetime = datetime.datetime.combine(e.event_end_date,e.event_end_time)
#     SCOPES = 'https://www.googleapis.com/auth/calendar'
#     store = file.Storage('credentials.json')
#     creds = store.get()
#     if not creds or creds.invalid:
#         flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
#         creds = tools.run_flow(flow, store)
#     service = build('calendar', 'v3', http=creds.authorize(Http()))
#     event = {
#       'summary': e.event_title,
#       'location': e.event_location,
#       'description': e.event_description,
#       'start': {
#         'dateTime': start_datetime,
#         'timeZone': 'Indian/Reunion',
#       },
#       'end': {
#         'dateTime': end_datetime,
#         'timeZone': 'Indian/Reunion',
#       },
#       'recurrence': [
#       ],
#       'attendees': [
#       ],
#       'reminders': {
#         'useDefault': False,
#         'overrides': [
#           {'method': 'email', 'minutes': 24 * 60},
#           {'method': 'popup', 'minutes': 10},
#         ],
#       },
#     }
#
#     event = service.events().insert(calendarId='primary', body=event).execute()
#     print('Event created: %s' % (event.get('htmlLink')))
#
# post_save.connect(add_to_calendar ,sender=Event)
