from doa.movies import MoviesDAO


class MovieService:
    def __init__(self, movie_dao: MoviesDAO):
        self.movie_dao = movie_dao

    def get_movie(self, mid=None, **kwargs):
        return self.movie_dao.get(mid, **kwargs)

    def creat_movie(self, data):
        return self.movie_dao.create(data)

    def update_movie(self, movie_id, data):
        movie = self.get_movie(movie_id)

        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]
        movie.genre = data["genre"]
        movie.director = data["director"]

        self.movie_dao.update(movie)
        return movie

    def update_movie_partial(self, movie_id, data):
        movie = self.get_movie(movie_id)

        if 'title' in data:
            movie.title = data['title']
        elif 'description' in data:
            movie.description = data['description']
        elif 'trailer' in data:
            movie.trailer = data['trailer']
        elif 'year' in data:
            movie.year = data['year']
        elif 'rating' in data:
            movie.rating = data['rating']
        elif 'genre_id' in data:
            movie.genre_id = data['genre_id']
        elif 'director_id' in data:
            movie.director_id = data['director_id']

        self.movie_dao.update(movie)
        return movie

    def delete(self, mid):
        self.movie_dao.delete(mid)

    # def filter_genre_id(self, genre_id):
    #     movies = self.get_movie()
    #     resalt = []
    #
    #     for movie in movies:
    #         if movie.genre_id == int(genre_id):
    #             resalt.append(movie)
    #     return resalt