from doa.genres import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genre(self, gid=None):
        return self.genre_dao.get(gid)
