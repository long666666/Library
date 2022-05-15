from django.shortcuts import render, redirect, HttpResponse
from books01 import models
from django.urls import reverse


def books_list(request):
    books_list = models.book.objects.all()
    return render(request, "books_list.html", locals())


def delete_book(request, bid):
    models.book.objects.get(id=bid).delete()
    return redirect(reverse("books_list"))


def edit_book(request, bid):
    books_obj = models.book.objects.get(id=bid)
    if request.method == 'POST':
        title = request.POST.get("title")
        publisher_id = request.POST.get("publisher")
        author_id = request.POST.get("author_id")
        price = request.POST.get("price")
        publisher_day = request.POST.get("publisher_day")
        introduce = request.POST.get("introduce")

        # print(title, publisher_id, author_id, price, publisher_day, introduce)
        # 更新数据
        books_obj.title = title
        books_obj.publisher_id = publisher_id
        books_obj.price = price
        books_obj.publisher_day = publisher_day
        books_obj.introduction = introduce

        # 多对多修改：先删除再添加
        books_obj.author_set.clear()
        books_obj.author_set.add(author_id)

        books_obj.save()

        return redirect(reverse("books_list"))

    book_info = models.book.objects.get(id=bid)
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "edit_book.html", locals())


def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        publisher = request.POST.get("publisher")
        author_id = request.POST.get("author_id")
        price = request.POST.get("price")
        publisher_day = request.POST.get("publisher_day")
        introduce = request.POST.get("introduce")
        print(title, publisher, author_id, price, publisher_day, introduce)

        models.book.objects.create(title=title, price=price,
                                   publisher_day=publisher_day,
                                   publisher_id=publisher,
                                   introduction=introduce,
                                   )

        # 多对多添加，先获得对象，再使用 .add() 添加
        book_obj = models.book.objects.get(title=title)
        book_obj.author_set.add(author_id)

        return redirect(reverse("books_list"))

    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, "add_book.html", locals())


def search(request):
    if request.method == "POST":
        books_name = request.POST.get("book_name")
        books_list = models.book.objects.filter(title__contains=books_name)
        print(books_list)
        return render(request, "books_list.html", locals())

    books_list = models.book.objects.all()
    return render(request, "books_list.html", locals())


def details(request, arg):
    book_info = models.book.objects.get(id=arg)
    author_introduce = models.book.objects.get(id=arg).author_set.values().last()["introduce"]
    book_introduce = models.book.objects.get(id=arg).introduction
    return render(request, "details.html", locals())
