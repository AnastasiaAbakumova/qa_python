import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name', [
        'Война и мир',
        'Гарри Поттер'
    ])
    def test_add_new_book_valid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        '',
        'a' * 41,
    ])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name', [
        '   ',
        '\n',
        ' \n\t'
    ])
    def test_add_new_book_whitespace_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', [
        ('Мгла', 'Ужасы'),
        ('Шерлок Холмс', 'Детективы'),
        ('Король Лев', 'Мультфильмы')
    ])
    def test_set_book_genre_valid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Несуществующий жанр')
        assert collector.get_book_genre('Шерлок Холмс') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2
        assert 'Марсианин' in collector.get_books_with_specific_genre('Фантастика')
        assert 'Гарри Поттер' in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Король Лев')
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Мальчик в полосатой пижаме')
        collector.set_book_genre('Мальчик в полосатой пижаме', 'Драма')
        children_books = collector.get_books_for_children()
        assert 'Король Лев' in children_books
        assert 'Оно' not in children_books
        assert 'Мальчик в полосатой пижаме' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('451° по Фаренгейту')
        collector.add_book_in_favorites('451° по Фаренгейту')
        collector.add_book_in_favorites('451° по Фаренгейту')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цветы для Элджернона')
        collector.add_book_in_favorites('Цветы для Элджернона')
        assert 'Цветы для Элджернона' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Цветы для Элджернона')
        assert 'Цветы для Элджернона' not in collector.get_list_of_favorites_books()

    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []