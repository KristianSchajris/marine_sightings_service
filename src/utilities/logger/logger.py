import logging

def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        class_name = self.__class__.__name__
        logging.info(f"called to method: {class_name}.{method.__name__}")
        return method(self, *args, **kwargs)
    return wrapper
