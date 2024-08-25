from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
from .forms import ExampleForm

# Function-Based View for Editing a Book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

# Function-Based View for Deleting a Book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

# Class-Based View for Creating a Book
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/add_book.html'
    permission_required = 'bookshelf.can_add'
    raise_exception = True

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

# Class-Based View for Editing a Book
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/edit_book.html'
    permission_required = 'bookshelf.can_edit'
    raise_exception = True

# Class-Based View for Deleting a Book
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookshelf/confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_delete'
    raise_exception = True

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_create', raise_exception=True)
def book_list(request):
    return HttpResponse

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    return HttpResponse