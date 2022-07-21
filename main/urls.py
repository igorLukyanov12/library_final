from django.urls import path
from .views import main_page, book_reg, book_list, reader_list, books_lending, books_reciving, off_books, \
    profit, redirect_to_main_page, sort_title, sort_book_pub_year, sort_book_ex, back_book_list, next_book_list, \
    reader_reg, sort_reader_surname, sort_reader_name, sort_reader_date_of_birthday, sort_reader_address, \
    sort_reader_email, back_reader_list, next_reader_list, sort_books_genre, books_lending_check, books_lending_final, \
    books_reciving_check, books_reciving_explore, books_reciveng_final_cost, end_arenda

app_name = 'main'
urlpatterns = [
    path('', main_page, name="main_page"),
    path('book_reg/', book_reg, name="book_reg"),
    path('book_list/', book_list, name="book_list"),
    path('reader_list/', reader_list, name="reader_list"),
    path('reader_reg/', reader_reg, name="reader_reg"),
    path('books_lending/', books_lending, name="books_lending"),
    path('books_reciving/', books_reciving, name="books_reciving"),
    path('off_books/', off_books, name="off_books"),
    path('profit/', profit, name="profit"),
    path('redirect_to_main_page/', redirect_to_main_page, name="redirect_to_main_page"),
    path('sort_title/', sort_title, name="sort_title"),
    path('sort_book_pub_year/', sort_book_pub_year, name="sort_book_pub_year"),
    path('sort_book_ex/', sort_book_ex, name="sort_book_ex"),
    path('next_book_list/', next_book_list, name="next_book_list"),
    path('back_book_list/', back_book_list, name="back_book_list"),
    path('reader_reg/', reader_reg, name="reader_reg"),
    path('sort_reader_surname/', sort_reader_surname, name="sort_reader_surname"),
    path('sort_reader_name/', sort_reader_name, name="sort_reader_name"),
    path('sort_reader_date_of_birthday/', sort_reader_date_of_birthday, name="sort_reader_date_of_birthday"),
    path('sort_reader_address/', sort_reader_address, name="sort_reader_address"),
    path('sort_reader_email/', sort_reader_email, name="sort_reader_email"),
    path('back_reader_list/', back_reader_list, name="back_reader_list"),
    path('next_reader_list/', next_reader_list, name="next_reader_list"),
    path('sort_books_genre/', sort_books_genre, name="sort_books_genre"),
    path('books_lending/', books_lending, name = "books_lending"),
    path('books_lending_check/', books_lending_check, name = "books_lending_check"),
    path('books_lending_final/', books_lending_final, name = "books_lending_final"),
    path('books_reciving_check/', books_reciving_check, name = "books_reciving_check"),
    path('books_reciving_explore/', books_reciving_explore, name = 'books_reciving_explore'),
    path('books_reciveng_final_cost/', books_reciveng_final_cost, name = 'books_reciveng_final_cost'),
    path('end_arenda/', end_arenda, name = 'end_arenda')
]
