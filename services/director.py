from doa.directors import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_director(self, did=None):
        return self.director_dao.get(did)
