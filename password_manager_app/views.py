from django.shortcuts import render
from .models import PasswordEntry
from cryptography.fernet import Fernet
from decouple import config


key = config('FERNET_KEY')
print(key)
fernet = Fernet(key)


def password_list(request):
    passwords = PasswordEntry.objects.all()
    return render(request, 'password_list.html', {'passwords': passwords})


def add_password(request):
    if request.method == 'POST':
        website = request.POST['website']
        username = request.POST['username']
        password = request.POST['password']
        encrypted_password = fernet.encrypt(password.encode()).decode()
        PasswordEntry.objects.create(website=website, username=username, password=encrypted_password)
    return render(request, 'add_password.html')


def get_password(request):
    decrypted_password = None
    if request.method == 'POST':
        website = request.POST['website']
        username = request.POST['username']
        try:
            password_entry = PasswordEntry.objects.get(website=website, username=username)
            password = password_entry.password
            decrypted_password = fernet.decrypt(password.encode()).decode()
        except PasswordEntry.DoesNotExist:
            decrypted_password = 'Password not found!'

    return render(request, 'get_password.html', {'password': decrypted_password})
