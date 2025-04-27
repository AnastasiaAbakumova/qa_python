class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']
    
    def add_new_book(self, name):
        name = name.strip()
        if name and len(name) < 41 and name not in self.books_genre:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre):
        return [name for name, book_genre in self.books_genre.items() 
                if book_genre == genre and genre in self.genre]

    def get_books_genre(self):
        return self.books_genre.copy()

    def get_books_for_children(self):
        return [name for name, genre in self.books_genre.items()
                if genre not in self.genre_age_rating and genre in self.genre]

    def add_book_in_favorites(self, name):
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites.copy()