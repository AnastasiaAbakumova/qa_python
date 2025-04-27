import pytest
from books_collector import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name', [
        'Война и мир',
        '1984',
        'a' * 40
    ])
    def test_add_new_book_valid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        '',
        'a' * 41,
        '   '
    ])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name.strip() not in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', [
        ('Мгла', 'Ужасы'),
        ('Марсианин', 'Фантастика'),
        ('Шерлок Холмс', 'Детективы')
    ])
    def test_set_book_genre_valid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

   