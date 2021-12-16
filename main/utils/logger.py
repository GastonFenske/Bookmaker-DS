import datetime as dt
from colorama import init, Fore
from abc import ABC, abstractmethod

init(autoreset=True)

class Logger(ABC):

    @abstractmethod
    def info(self, mensaje, objeto):
        pass

    @abstractmethod
    def warning(self, mensaje, objeto):
        pass

    @abstractmethod
    def error(self, mensaje, objeto):
        pass

    @abstractmethod
    def debug(self, mensaje, objeto):
        pass

class LoggerFactory(ABC):
    @abstractmethod
    def getLogger(self, tipo):
        pass

class LoggerFactoryImpl(LoggerFactory):
    def getLogger(self, tipo):
        dic = {
            'c': LoggerConsola(),
            'f': LoggerFile(),
            'e': LoggerEmail()
        }
        return dic[tipo]

class LoggerConsola(Logger):
    def info(self, mensaje, objeto):
        print(f'{dt.datetime.now()} {Fore.BLUE} [INFO] {mensaje}, {objeto}')

    def warning(self, mensaje, objeto):
        print(f'{dt.datetime.now()} {Fore.YELLOW} [WARN] {mensaje}, {objeto}')

    def error(self, mensaje, objeto):
        print(f'{dt.datetime.now()} {Fore.RED} [ERROR] {mensaje}, {objeto}')

    def debug(self, mensaje, objeto):
        print(f'{dt.datetime.now()} {Fore.MAGENTA} [DEB] {mensaje}, {objeto}')

log_file = 'file.log'
class LoggerFile(Logger):
    def info(self, mensaje, objeto):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [INFO] {mensaje} {str(objeto)} \n'
            file.writelines(data)

    def warning(self, mensaje, objeto):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [WARN] {mensaje} {str(objeto)} \n'
            file.writelines(data)

    def error(self, mensaje, objeto):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [ERROR] {mensaje} {str(objeto)} \n'
            file.writelines(data)

    def debug(self, mensaje, objeto):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [DEB] {mensaje} {str(objeto)} \n'
            file.writelines(data)

class LoggerEmail(Logger):

    def info(self, mensaje, objeto):
        print('Enviando email')

    def warning(self, mensaje, objeto):
        print('Ha aparecido un warning')

    def error(self, mensaje, objeto):
        print('Ha habido un error al enviar el email')

    def info(self, mensaje, objeto):
        print('Debug')

if __name__ == '__main__':
    type_log = str(input("""
[c] Para salida por consola
[f] Para el archivo
[e] Para el email
>>>: """))
    logger = LoggerFactoryImpl().getLogger(tipo=type_log)
    logger.info('Valor de la variable', 123)
    logger.warning('Valor de la varaible', 456)
    logger.error('Valor de la variable', 789)
    logger.debug('Valor de la variable', 1011)
