import logging

class PyRanj () :
    
    def wrapper(self , *args , **kwargs):
        # logging.Logger('[EXCEPTION]' , )
        logging.log([Exception], *args)


if __name__=="__main__":
    @PyRanj
    def f():
        raise Exception('Ranj')

