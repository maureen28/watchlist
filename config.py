 import os # Interaction with our os
 
class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://www.themoviedb.org/3/movie/popular?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY ')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
Config_options = { #Dict
    'development': DevConfig
    'production': ProdConfig
} 