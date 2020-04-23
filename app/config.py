class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://www.themoviedb.org/3/movie/popular?api_key={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True