import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def book_name(self):
        name = "Гарри Поттер"
        return name

    @pytest.mark.parametrize("name",
                             [
                                 "К",
                                 "Книга",
                                 "Книга с тридцатью девятью символами 39",
                                 "Книга с сорока символами книга книга кни",
                             ])
    def test_add_new_book_positive_len(self, name):
        bc = BooksCollector()
        bc.add_new_book(name)
        assert name in bc.get_books_genre()

    @pytest.mark.parametrize("name",
                             ["",
                              "Книга, где сорок один символ, символ, сим",
                              "Книга, где сорок один символ, символ, симв"])
    def test_add_new_book_negative_len(self, name):
        bc = BooksCollector()
        bc.add_new_book(name)
        assert name not in bc.get_books_genre()

    def test_add_new_book_already_existing_book(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.add_new_book(book_name)
        assert bc.get_books_genre() == {book_name: ""}



    def test_set_books_genre_if_genre_and_book_true(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.set_book_genre(book_name, "Фантастика")
        assert bc.get_book_genre(book_name) == "Фантастика"

    def test_set_books_genre_if_book_true_genre_false(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.set_book_genre(book_name, "Биография")
        assert bc.get_book_genre(book_name) != "Биография"

    def test_set_books_genre_if_book_false(self):
        bc = BooksCollector()
        bc.set_book_genre("Молчание ягнят", "Фантастика")
        assert "Молчание ягнят" not in bc.get_books_genre()

    def test_get_book_genre_if_book_true(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.set_book_genre(book_name, "Фантастика")
        assert bc.get_book_genre(book_name) == "Фантастика"

    def test_get_book_genre_if_book_not_exist(self):
        bc = BooksCollector()
        assert bc.get_book_genre("Молчание ягнят") is None

    def test_get_books_with_specific_genre_true(self):
        bc = BooksCollector()
        bc.add_new_book("Гарри Поттер")
        bc.set_book_genre("Гарри Поттер", "Фантастика")
        bc.add_new_book("Молчание ягнят")
        bc.set_book_genre("Молчание ягнят", "Ужасы")
        bc.add_new_book("Программирование на Python")
        bc.set_book_genre("Программирование на Python", "Фантастика")
        assert bc.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер", "Программирование на Python"]


    def test_get_books_with_specific_genre_false(self):
        bc = BooksCollector()
        bc.set_book_genre("Гарри Поттер", "Биография")
        bc.set_book_genre("Молчание ягнят", "Развлечения")
        bc.set_book_genre("Программирование на Python", "Биография")
        assert bc.get_books_with_specific_genre("Биография") != ["Гарри Поттер", "Программирование на Python"]

    def test_get_books_genre_with_two_books(self):
        bc = BooksCollector()

        bc.add_new_book('Гордость и предубеждение и зомби')
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(bc.get_books_genre()) == 2

    def test_get_books_for_children(self):
        bc = BooksCollector()
        bc.add_new_book("Гарри Поттер")
        bc.set_book_genre("Гарри Поттер", "Мультфильмы")
        bc.add_new_book("Молчание ягнят")
        bc.set_book_genre("Молчание ягнят", "Ужасы")
        bc.add_new_book("Программирование на Python")
        bc.set_book_genre("Программирование на Python", "Комедии")
        assert bc.get_books_for_children() == ["Гарри Поттер", "Программирование на Python"]

    def test_add_book_in_favorite_unique(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.add_book_in_favorites(book_name)
        assert book_name in bc.get_list_of_favorites_books()

    def test_add_book_in_favorite_same_book_not_in_list(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.add_book_in_favorites(book_name)
        bc.add_book_in_favorites(book_name)
        assert len(bc.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_true(self, book_name):
        bc = BooksCollector()
        bc.add_new_book(book_name)
        bc.add_book_in_favorites(book_name)
        bc.delete_book_from_favorites(book_name)
        assert book_name not in bc.get_list_of_favorites_books()


    def test_get_list_of_favorite_books_list(self):
        bc = BooksCollector()
        bc.add_new_book("Гарри Поттер")
        bc.add_new_book("Молчание ягнят")
        bc.add_book_in_favorites("Гарри Поттер")
        bc.add_book_in_favorites("Молчание ягнят")
        assert len(bc.get_list_of_favorites_books()) == 2