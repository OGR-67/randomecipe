from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from recipe.models import UserFavoriteRecipe


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(
            data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # Log in, redirect to home page.
        login(request, new_user)
        return redirect('recipe:recipes')
    # Display a blank or invalid form.
    context = {
        'form': form,
        "page_title": "Randomecipe - Register"
    }
    return render(request, 'registration/register.html', context)


@login_required
def user_account(request):
    user = request.user
    recipes_list = UserFavoriteRecipe.objects.filter(user=user)
    context = {
        "number_of_favorites": len(recipes_list),
        "page_title": f"Randomecipe - {user} Account"
    }
    return render(request, 'registration/account.html', context)


@login_required
def del_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()

    return redirect("recipe:index")
