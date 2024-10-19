from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect

from bookie.models import SubProfile


@login_required
def home(request):
    return render(request, 'bookie/main.html')


@login_required
def downline_listing(request):
    bookie = request.user.sub_user_profile.all().first().bookie
    total_balance = SubProfile.objects.filter(bookie=bookie).aggregate(Sum('balance'))['balance__sum'] or 0
    total_deposit = SubProfile.objects.filter(bookie=bookie).aggregate(Sum('exposure_limit'))[
                        'exposure_limit__sum'] or 0
    print(total_deposit)
    return render(request, "bookie/downline_listing.html",
                  context={"total_balance": total_balance, "total_deposit": total_deposit,
                           "profiles": bookie.sub_profile.all()})


@login_required
def create_subprofile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        balance = request.POST['balance']
        exposure_limit = request.POST['exposure_limit']
        is_active = request.POST.get('is_active') == 'true'
        is_suspended = request.POST.get('is_suspended') == 'true'
        is_locked = request.POST.get('is_locked') == 'true'

        # Create user first
        if not User.objects.filter(username=username).exists():
            user = User.objects.create(
                username=username,
                password=make_password(password)  # Encrypt the password
            )

            # Create SubProfile linked to the user
            bookie = request.user.sub_user_profile.first().bookie  # Assuming current user is linked to a bookie
            sub_profile = SubProfile.objects.create(
                user=user,
                bookie=bookie,
                nickname=nickname,
                balance=balance,
                exposure_limit=exposure_limit,
                is_active=is_active,
                is_suspended=is_suspended,
                is_locked=is_locked
            )

            messages.success(request, "SubProfile created successfully!")
            return redirect('/')  # Replace 'success_url' with the actual URL you want to redirect to


@login_required
def downline_search(request):
    return render(request, 'bookie/downline_search.html')


@login_required
def risk_management(request):
    return render(request, 'bookie/risk_management.html')


@login_required
def banking(request):
    return render(request, 'bookie/banking.html')


@login_required
def report_by_player(request):
    return render(request, 'bookie/report_by_player.html')


@login_required
def bet_list(request):
    return render(request, 'bookie/bet_list.html')


@login_required
def bet_list_live(request):
    return render(request, 'bookie/bet_list_live.html')


@login_required
def my_account(request):
    return render(request, 'bookie/my_account.html')


@login_required
def player_battle(request):
    return render(request, 'bookie/player_battle.html')
