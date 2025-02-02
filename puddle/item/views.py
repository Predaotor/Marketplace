from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import NewItemform, EditItemform
from django.db.models import Q
# Create your views here.

# ✅ Create the browse view to search for items 
def browse(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category', None)

    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')

    # ✅ Only filter by category if it's a valid number
    if category_id and category_id.isdigit():
        category_id = int(category_id)
        if Category.objects.filter(id=category_id).exists():  # ✅ Check if category exists
            items = items.filter(category_id=category_id)
            print(f"Filtered items count: {items.count()}")  # ✅ Debugging
        else:
            print(f"Invalid category_id: {category_id}, not found in database.")

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/browse.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': category_id if isinstance(category_id, int) else None,  
    })



# ✅ Create the detail view to show the details of an item
def detail(request, pk):
    item=get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    can_edit=request.user==item.created_by
    
    return render(request, "item/detail.html", {
        "item":item,
        "related_items":related_items,
        "can_edit":can_edit
    })

# ✅ Create the new view to create a new item
@login_required
def new(request):
    if request.method=="POST":
        form=NewItemform(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user 
            item.save()

            return redirect('item:detail', pk=item.id)
            
    else:
        form=NewItemform()

    return render(request, "item/form.html", { 
        "form":form,
        "title":"New item",
    }
    )

# ✅ Create the delete view to delete an item
@login_required 
def delete(request, pk):
    item=get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

# ✅ Create the edit view to edit an item
@login_required 
def edit(request, pk):
    item=get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=="POST":
        form=EditItemform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
            
    else:
        form=EditItemform(instance=item)

    return render(request, "item/form.html", { 
        "form":form,
        "title":"Edit item",
    }
    )