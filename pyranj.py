# from logging import Logger

class PyRanj () :
    def __init__(self , *args , **kwargs):
        print('[EXCEPTION] :: Ranj')
    def wrapper(self , *args , **kwargs):
        print('[EXCEPTION] :: Ranj')



if __name__=="__main__":
    from pyranj import PyRanj as pyranj

    @pyranj
    def f():
        raise Exception('Ranj')

    

