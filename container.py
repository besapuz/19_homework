from doa.movies import MoviesDAO
from doa.services.movie import MovieService
from doa.services.director import DirectorService
from doa.directors import DirectorDAO
from doa.services.genre import GenreService
from doa.genres import GenreDAO
from setup_db import db

movie_dao = MoviesDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_doa = GenreDAO(db.session)
genre_service = GenreService(genre_doa)
