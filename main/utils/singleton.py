

class SingletonPattern():    

    @staticmethod
    def singleton(cls):
        instances = dict()
        def wrapper(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        return wrapper