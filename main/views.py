from django.shortcuts import render, redirect
from datetime import date
import sqlite3

from .models import Books, Author, Genre, Customers

fl1, fl2 = False, False


def main_page(request):
    return render(request, 'main.html')


def redirect_to_main_page(request):
    global fl1, fl2
    if fl1:
        author = Author.objects.all()
        genre = Genre.objects.all()
        context = {
            'author': author,
            'genre': genre
        }
        books = Books.objects.create(title_russian=request.POST.get('title_russian'),
                                     title_foreign=request.POST.get('title_foreign'),
                                     description=request.POST.get('description'),
                                     price=request.POST.get('price'),
                                     cost_daily=request.POST.get('cost_daily'),
                                     amount_ex=request.POST.get('amount_ex'),
                                     available_ex=request.POST.get('amount_ex'),
                                     date_registration=request.POST.get('date_registration'),
                                     number_of_pages=request.POST.get('number_of_pages'),
                                     year_of_publication=request.POST.get('year_of_publication'),
                                     pubdate=request.POST.get('pubdate'))
        genr = request.POST.getlist('genre')
        auth = request.POST.getlist('author')
        for i in genre:
            for j in genr:
                if j == i.name:
                    books.genre.add(Genre.objects.get(name=j))

        for i in author:
            for j in auth:
                if j == i.surname:
                    books.author.add(Author.objects.get(surname=j))
    fl1 = False
    if fl2:
        Customers.objects.create(surname=request.POST.get('surname'),
                                 name=request.POST.get('name'),
                                 second_name=request.POST.get('second_name'),
                                 email=request.POST.get('email'),
                                 date_of_birthday=request.POST.get('date_of_birthday'),
                                 ages=request.POST.get('ages'),
                                 sex=request.POST.get('sex'),
                                 number_of_passport=request.POST.get('number_of_passport'),
                                 place=request.POST.get('place'))
    fl2 = False
    return redirect('main:main_page')


def book_reg(request):
    global fl1
    fl1 = True
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {
        'author': author,
        'genre': genre
    }
    return render(request, 'book_reg.html', context)


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Сортировка книг
sorted_pub_year = False
sorted_amount_ex = False
sorted_genres = False
sorted_title = True
books = []
for i in Books.objects.all():
    books.append(i)
print(books)
first_num_book_list, second_num_book_list = 0, 20
b = books[first_num_book_list:second_num_book_list]


def sort_title(request):
    global b, sorted_title, first_num_book_list, second_num_book_list, books, sorted_pub_year, sorted_amount_ex, sorted_genres
    if sorted_title:
        b = b[::-1]
    elif not sorted_title:
        b = books[first_num_book_list:second_num_book_list]
        sorted_title = True
    sorted_pub_year = False
    sorted_amount_ex = False
    sorted_genres = False
    return redirect('main:book_list')


def sort_book_pub_year(request):
    global b, sorted_pub_year, sorted_title, sorted_amount_ex, sorted_genres
    if not sorted_pub_year:
        for i in b:
            for index, value in enumerate(b):
                if index < len(b) - 1 and value.year_of_publication.year > b[
                    index + 1].year_of_publication.year:
                    b[index], b[index + 1] = b[index + 1], b[index]
            sorted_pub_year = True
    elif sorted_pub_year:
        b = b[::-1]
        sorted_pub_year = False
    sorted_title = False
    sorted_amount_ex = False
    sorted_genres = False
    return redirect('main:book_list')


def sort_book_ex(request):
    global b, sorted_amount_ex, sorted_title, sorted_pub_year, sorted_genres
    if not sorted_amount_ex:
        for i in b:
            for index, value in enumerate(b):
                if index < len(b) - 1 and value.amount_ex > b[
                    index + 1].amount_ex:
                    b[index], b[index + 1] = b[index + 1], b[index]
            sorted_amount_ex = True
    elif sorted_amount_ex:
        b = b[::-1]
        sorted_amount_ex = False
    sorted_title = False
    sorted_pub_year = False
    sorted_genres = False
    return redirect('main:book_list')


# def sort_reader_name(request):
#     global reader, sorted_name, sorted_surname, sorted_date_of_birthday, sorted_address, sorted_email
#     if not sorted_name:
#         for i in reader:
#             for index, value in enumerate(reader):
#                 if index < len(reader) - 1 and value.name > reader[
#                     index + 1].name:
#                     reader[index], reader[index + 1] = reader[index + 1], reader[index]
#             sorted_name = True
#     elif sorted_name:
#         reader = reader[::-1]
#         sorted_name = False
#     sorted_surname = False
#     sorted_date_of_birthday = False
#     sorted_address = False
#     sorted_email = False
#     return redirect('main:reader_list')

def sort_books_genre(request):
    global b, sorted_amount_ex, sorted_title, sorted_pub_year, sorted_genres, books, first_num_book_list, second_num_book_list
    if not sorted_genres:
        helicopter = []
        for i in Books.objects.order_by('genre__name'):
            helicopter.append(i)
        book = helicopter[first_num_book_list: second_num_book_list]
        print(book)
        for i, f in enumerate(book):
            print(f)
            for j, m in enumerate(book):
                print(m)
                if j <= i:
                    continue
                if f == m and j != i:
                    book = book[:j] + book[j + 1:]
                    print(book, 'thi is books')
        print(book)
        b = book
        sorted_genres = True
    else:
        b = b[::-1]
        sorted_genres = False
    sorted_title = False
    sorted_pub_year = False
    sorted_amount_ex = False
    return redirect('main:book_list')


def next_book_list(request):
    global b, books, first_num_book_list, second_num_book_list, sorted_amount_ex, sorted_title, sorted_pub_year, sorted_genres
    sorted_pub_year = False
    sorted_amount_ex = False
    sorted_genres = False
    sorted_title = True
    first_num_book_list += 20
    second_num_book_list += 20
    b = books[first_num_book_list:second_num_book_list]
    if b == []:
        first_num_book_list -= 20
        second_num_book_list -= 20
        b = books[first_num_book_list:second_num_book_list]
    print(b)
    return redirect('main:book_list')


def back_book_list(request):
    global b, first_num_book_list, second_num_book_list, sorted_amount_ex, sorted_title, sorted_pub_year, sorted_genres
    sorted_pub_year = False
    sorted_amount_ex = False
    sorted_genres = False
    sorted_title = True
    first_num_book_list -= 20
    second_num_book_list -= 20
    b = books[first_num_book_list:second_num_book_list]
    if b == []:
        first_num_book_list += 20
        second_num_book_list += 20
        b = books[first_num_book_list:second_num_book_list]
    return redirect('main:book_list')


def book_list(request):
    global b
    context = {
        'b': b,
    }
    return render(request, 'book_list.html', context)


# ____________________________________________________________________________________________________
# ____________________________________________________________________________________________________
# Сортировка чытатэлей
sorted_name = True
sorted_date_of_birthday = False
sorted_address = False
sorted_email = False
sorted_surname = False
customers = []
for i in Customers.objects.all():
    customers.append(i)
print(customers)
first_num_reader_list, second_num_reader_list = 0, 20
reader = customers[first_num_reader_list:second_num_reader_list]


def sort_reader_name(request):
    global reader, sorted_surname, first_num_reader_list, second_num_reader_list, customers, sorted_name, sorted_date_of_birthday, sorted_address, sorted_email
    if sorted_name:
        reader = reader[::-1]
    elif not sorted_name:
        reader = customers[first_num_reader_list:second_num_reader_list]
        sorted_name = True
    sorted_surname = False
    sorted_date_of_birthday = False
    sorted_address = False
    sorted_email = False
    return redirect('main:reader_list')


def sort_reader_surname(request):
    global reader, sorted_name, sorted_surname, sorted_date_of_birthday, sorted_address, sorted_email
    if not sorted_surname:
        for i in reader:
            for index, value in enumerate(reader):
                if index < len(reader) - 1 and value.surname > reader[
                    index + 1].surname:
                    reader[index], reader[index + 1] = reader[index + 1], reader[index]
            sorted_surname = True
    elif sorted_surname:
        reader = reader[::-1]
        sorted_surname = False
    sorted_name = False
    sorted_date_of_birthday = False
    sorted_address = False
    sorted_email = False
    return redirect('main:reader_list')


def sort_reader_date_of_birthday(request):
    global reader, sorted_date_of_birthday, sorted_surname, sorted_name, sorted_address, sorted_email
    if not sorted_date_of_birthday:
        for i in reader:
            for index, value in enumerate(reader):
                if index < len(reader) - 1 and value.date_of_birthday > reader[
                    index + 1].date_of_birthday:
                    reader[index], reader[index + 1] = reader[index + 1], reader[index]
            sorted_date_of_birthday = True
    elif sorted_date_of_birthday:
        reader = reader[::-1]
        sorted_date_of_birthday = False
    sorted_surname = False
    sorted_name = False
    sorted_address = False
    sorted_email = False
    return redirect('main:reader_list')


def sort_reader_address(request):
    global reader, sorted_date_of_birthday, sorted_surname, sorted_name, sorted_address, sorted_email
    if not sorted_address:
        for i in reader:
            for index, value in enumerate(reader):
                if index < len(reader) - 1 and value.place > reader[
                    index + 1].place:
                    reader[index], reader[index + 1] = reader[index + 1], reader[index]
            sorted_address = True
    elif sorted_address:
        reader = reader[::-1]
        sorted_address = False
    sorted_name = False
    sorted_date_of_birthday = False
    sorted_surname = False
    sorted_email = False
    return redirect('main:reader_list')


def sort_reader_email(request):
    global reader, sorted_date_of_birthday, sorted_surname, sorted_name, sorted_address, sorted_email
    if not sorted_email:
        for i in reader:
            for index, value in enumerate(reader):
                if index < len(reader) - 1 and value.email > reader[
                    index + 1].email:
                    reader[index], reader[index + 1] = reader[index + 1], reader[index]
            sorted_email = True
    elif sorted_email:
        reader = reader[::-1]
        sorted_email = False
    sorted_name = False
    sorted_date_of_birthday = False
    sorted_address = False
    sorted_surname = False
    return redirect('main:reader_list')


def next_reader_list(request):
    global reader, customers, first_num_reader_list, second_num_reader_list, sorted_date_of_birthday, sorted_surname, sorted_name, sorted_address, sorted_email
    sorted_name = False
    sorted_date_of_birthday = False
    sorted_address = False
    sorted_email = False
    sorted_surname = True
    first_num_reader_list += 20
    second_num_reader_list += 20
    reader = customers[first_num_reader_list:second_num_reader_list]
    if reader == []:
        first_num_reader_list -= 20
        second_num_reader_list -= 20
        reader = customers[first_num_reader_list:second_num_reader_list]
    print(reader)
    return redirect('main:reader_list')


def back_reader_list(request):
    global reader, first_num_reader_list, second_num_reader_list, sorted_date_of_birthday, sorted_surname, sorted_name, sorted_address, sorted_email
    sorted_name = False
    sorted_date_of_birthday = False
    sorted_address = False
    sorted_email = False
    sorted_surname = True
    first_num_reader_list -= 20
    second_num_reader_list -= 20
    reader = customers[first_num_reader_list:second_num_reader_list]
    if reader == []:
        first_num_reader_list += 20
        second_num_reader_list += 20
        reader = customers[first_num_reader_list:second_num_reader_list]
    return redirect('main:reader_list')


def reader_list(request):
    global reader
    context = {
        'reader': reader,
    }
    return render(request, 'reader_list.html', context)


def reader_reg(request):
    global fl2
    fl2 = True
    sex = [Customers.option[0][1], Customers.option[1][1]]
    context = {
        'sex': sex,
    }
    return render(request, 'reader_reg.html', context)


def books_lending(request):
    return render(request, 'books_lending.html')


name = ''
surname = ''


def books_lending_check(request):
    global name, surname
    customers = Customers.objects.all()
    books = Books.objects.all()
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    arr = []
    cust = ''
    for i in Customers.objects.all():
        if i.name == name and i.surname == surname:
            cust = i
            print(cust)
    for j in Books.objects.all():
        for i in j.customers_books.all():
            if name == i.name and surname == i.surname:
                arr.append(j.title_russian)
    print(arr)
    time = date.today()
    time = str(time)
    context = {
        'name': name,
        'surname': surname,
        'arr': arr,
        'books': books,
        'cust': cust,
        'time': time
    }
    for i in customers:
        print(i.name, i.surname, name, surname)
        if i.name == name and i.surname == surname:
            if not arr:
                return render(request, 'books_lending_final.html', context)
            else:
                return render(request, 'books_lending_status.html', context)
    return redirect('main:reader_reg')


def books_lending_final(request):
    global name, surname
    customers_books = request.POST.getlist('books_name')
    date_lend = request.POST.get('date_lend')
    print(type(date_lend))
    # date_lend=str(date_lend)
    try:
        connect = sqlite3.connect('db.sqlite3')
        cursor = connect.cursor()
        for i in customers_books:
            cursor.execute(
                f"""INSERT INTO Main_book_data(name,surname,book_title,date_lend) VALUES("{name}","{surname}","{i}","{date_lend}");""")
        print(cursor.fetchall())
        cursor.close()
        connect.commit()
    except:
        print('Ошибка')
    print(customers_books)
    for i in Books.objects.all():
        for j in customers_books:
            if j == i.title_russian:
                i.customers_books.add(Customers.objects.get(name=name, surname=surname))
                i.available_ex -= 1
                i.save()
    return redirect('main:main_page')


def books_reciving(request):
    return render(request, 'books_reciving.html')


def books_reciving_check(request):
    global name, surname
    customers = Customers.objects.all()
    books = Books.objects.all()
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    arr = []
    cust = ''
    for i in Customers.objects.all():
        if i.name == name and i.surname == surname:
            cust = i
            print(cust)
    for j in Books.objects.all():
        for i in j.customers_books.all():
            if name == i.name and surname == i.surname:
                arr.append(j.title_russian)
    print(arr)
    context = {
        'name': name,
        'surname': surname,
        'arr': arr,
        'books': books,
        'cust': cust
    }
    for i in customers:
        print(i.name, i.surname, name, surname)
        if i.name == name and i.surname == surname:
            if not arr:
                return render(request, 'books_reciving_status.html', context)
            else:
                return render(request, 'books_reciving_choice.html', context)
    return render(request, 'custer_does_not_exist.html')


book_to_recive = ''


def books_reciving_explore(request):
    global book_to_recive
    book_name = request.POST.get('books_choice')
    time = date.today()
    time = str(time)
    for i in Books.objects.all():
        if book_name == i.title_russian:
            book_to_recive = i
    context = {
        'book_to_recive': book_to_recive,
        'time': time
    }
    print(book_name, '!!!!!!!!!!')
    return render(request, 'books_reciving_explore.html', context)


def books_reciveng_final_cost(request):
    global name, surname, book_to_recive, id
    date_rec = request.POST.get('date_rec')
    print(date_rec)
    year = date_rec[0:4]
    month = date_rec[5:7]
    day = date_rec[8:10]
    print(type(date_rec))
    print(book_to_recive.title_russian)

    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM main_book_data;""")
    a = cursor.fetchall()
    print(name, surname, book_to_recive.title_russian)
    for i in a:
        for f, j in enumerate(i):
            print(j, i[f + 1], i[f + 2])
            if j == name and i[f + 1] == surname and i[f + 2] == book_to_recive.title_russian:
                date_lend = i[f + 3]
            else:
                break
    cursor.close()
    connect.commit()

    year_lend = date_lend[0:4]
    month_lend = date_lend[5:7]
    day_lend = date_lend[8:10]

    date_rec = date(int(year), int(month), int(day))
    date_lend = date(int(year_lend), int(month_lend), int(day_lend))
    b = date_rec - date_lend
    print(date_rec)
    print(type(date_rec))
    b = str(b)
    b = b[0:-14]
    print(b)

    b = int(b)
    if b > 30:
        b -= 30
        prosrochka = b * book_to_recive.cost_daily
    else:
        prosrochka = 0
    print(request.POST.getlist('mistake'))
    if len(request.POST.getlist('mistake')) == 0:
        mis = 0
    else:
        mis = len(request.POST.getlist('mistake'))
    print(prosrochka)
    prosrochka = float(prosrochka)
    final_cost = prosrochka + (float(book_to_recive.price) * 0.05) * mis + float(book_to_recive.price)
    print(final_cost)
    b_name = book_to_recive.title_russian
    context = {
        'b_name': b_name,
        'final_cost': final_cost
    }
    return render(request, 'books_reciveng_final_cost.html', context)


def end_arenda(request):
    global name, surname, book_to_recive, id
    name_of_delete_book = book_to_recive.title_russian
    name_of_delete_book = str(name_of_delete_book)
    print(name_of_delete_book,
          '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute(
        f"""DELETE FROM main_book_data WHERE name = '{name}' AND surname = '{surname}' AND book_title = '{name_of_delete_book}';""")
    cursor.close()
    connect.commit()
    custom = ''
    for i in Customers.objects.all():
        if i.name == name and i.surname == surname:
            custom = i

    custom.books_set.remove(book_to_recive)

    book_to_recive.available_ex += 1
    book_to_recive.save()
    return redirect('main:main_page')


def off_books(request):
    pass


def profit(request):
    pass
