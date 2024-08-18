from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
 
def book_list_view(request):
    books = Book.objects.all()   
    book_list = [(book.title, book.author.name) for book in books]  
    return render(request, 'relationship_app/list_books.html', {'book_list': book_list})   
 
class LibraryDetailView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'books' 
    def get_queryset(self):
        library_id = self.kwargs['library_id']  
        return Book.objects.filter(library__id=library_id)   
    
    class CustomLoginView(LoginView):
    
        template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    
    form_class= UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})