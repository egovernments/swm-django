from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Poll, Voted, Choice
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context = {'events': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'polls/detail.html', {'poll': poll, 'polls':latest_poll_list})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'polls/results.html', {'poll': poll, 'polls':latest_poll_list})


@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if poll.poll_deadline >= timezone.now():
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'poll': poll,
                'error_message': "You didn't select a choice.",
            })
        else:
            user = request.user
            pid = poll.id
            uid = user.id
            cid = selected_choice.id
            try:
                x = Voted.objects.filter(user__id=uid).filter(poll__id=pid)[0]
                current_choice = x.choice
                if current_choice == selected_choice:
                    x.save()
                else:
                    current_choice.choice_count = current_choice.choice_count - 1
                    current_choice.save()
                    selected_choice.choice_count += 1
                    selected_choice.save()
                    x.choice = selected_choice
                    x.save()
                return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
            except:
                object = Voted()
                object.user = request.user
                object.poll = poll
                selected_choice.choice_count += 1
                selected_choice.save()
                object.choice = selected_choice
                object.save()
                return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
    else:
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'deadline_message': "Sorry, Deadline is over",
        })
