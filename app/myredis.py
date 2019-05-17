from .structure import *


class MyRedis():
    """
    classe que implementa o mini redis
    """

    def __init__(self):
        self.storage = ThreadSafeDict()
        self.timer = ThreadSafeDict()

    def set_value(self, key, value, extime=None):
        """
            define uma chave e um valor na variável storage
            :param self: 
            :param key: chave
            :param value: valor
            :param extime=None: exit time
        """
        if extime:
            self.timer[key] = threading.Timer(
                int(extime), self.delete_task, args=[key])
            self.timer[key].start()
            self.timer[key].join()
        self.storage[key] = value
        return ReturnValue.OK_

    def get_value(self, key):
        """
        Retorna o valor da chave informada
            :param self: 
            :param key: chave
        """
        value = self.storage.get(key)
        if value != None:
            return value
        return ReturnValue.NIL_

    def delete_value(self, keys):
        """
        Remove um ou mais valor baseado na chave informada
            :param self: 
            :param *args: chaves 
        """
        if not keys:
            return ReturnValue.ERROR_NUMBER_OF_ARGUMENTS
        deleted = 0
        for key in keys:
            if self.get_value(key) != 'nil':
                self.storage.pop(key)
                deleted += 1
        return deleted

    def delete_task(self, key):
        self.timer.pop(key)

    def dbSize(self):
        """
        Retorna um inteiro informando o tamanho da variável storage
            :param self: 
        """
        return len(self.storage)

    def incr(self, key):
        """
        Incrementa em uma unidade o valor da chave informada
            :param self: 
            :param key: chave a ser incrementada
        """
        value = self.storage.get(key)
        if type(value) is not int:
            return ReturnValue.ERROR_TYPE_DATA
        if value == ReturnValue.NIL_:
            return ReturnValue.ZERO
        self.set_value(key, int(value)+1)
        return self.get_value(key)

    def zadd(self, key, args):
        """
        Insere um ou mais valores na chave informada
            :param self: 
            :param key: chave
            :param args: valores a serem inseridos na chave
            return quantidade de chaves novas inseridas
        """
        index = self.storage.get(key)
        new_one = 0
        if not index:
            index = dict()
        for arg in args:
            if index.get(arg) == None:
                new_one += 1
            index[arg] = args[arg]
            self.storage[key] = index
        return new_one

    def zcard(self, key):
        """
        Retorna o número de elementos da chave indicada
            :param self: 
            :param key: chave
        """
        index = self.storage.get(key)
        if not index:
            return ReturnValue.ZERO
        else:
            return len(index)

    def zrank(self, key, member):
        """
        Retorna o rank do elemento informado na variável member
            :param self: 
            :param key: chave
            :param member: valor
        """
        index = self.storage.get(key)
        if not index:
            return ReturnValue.NIL_
        if type(index) == str:
            if index == member:
                return 0
            else:
                return ReturnValue.NIL_
        dict_2_list = index.items()
        rank = 0
        for item in dict_2_list:
            if item[0] == member:
                return rank
            rank += 1
        return ReturnValue.NIL_

    def zrange(self, key, start, stop):
        """
        docstring here
            :param self: 
            :param key: 
            :param start: 
            :param stop: 
        """
        index = self.storage.get(key)
        if not index:
            return "nil"
        if type(index) == int:
            return index
        list_of_items = [item for item, _ in index.items()]

        if start < 0:
            start += len(index)
        if stop < 0:
            stop += len(index)

        return list_of_items[start:stop]


if __name__ == "__main__":
    redis = MyRedis()
    # print(redis.zadd('bulbasaur', 'pokedex_number', '001'))
    # print(redis.zadd('pokemon_type', 1, 'grass', 2, 'poison'))
    # print(redis.set('zero', 0, 2))
    # print(redis.set('um', 1, 2))
    # print(redis.set('dois', 2, 2))
    # print(redis.set('tres', 3, 2))
    # print(redis.set('quatro', 4, 2))
    # print(redis.set('cinco', 5, 2))
    # print(redis.set('seis', 6, 2))
    # print(redis.set('sete', 7, 2))
    # print(redis.set('oito', 8, 2))
    # print(redis.set('nove', 9, 2))
    # print(redis.incr('nove'))
    # print(redis.set('pokemon_name', 'Bulbasaur'))
    # print(redis.zadd('pokemon_type', 1, 'grass', 2, 'poison'))
    # print(redis.zadd('pokemon_base_stats', 'hp', 45, 'attack',	49, 'defense', 49, 'speed',	45))
    # print(redis.set('idade', 32))
    # print(redis.set('mais um teste', 30))
    # print(redis.dbSize())
    # print(redis.storage)
    # print(redis.delete('tres', 'cinco', 'nove'))
    # print(redis.storage)
    # print(redis.timer)
    # redis.incr('idade')
    # print(redis.get('tres'))
    # # print(redis.zadd('superpowers', 'fly', 111, 'super jump', 110, 'eita', 100))
    # print(redis.zadd('superpowers', 'zero', 0, 'um', 1, 'dois', 2, 'tres', 3, 'quatro', 4, 'cinco', 5, 'seis', 6, 'sete', 7, 'oito', 8, 'nove', 9))
    print(
        redis.zadd(
            'superpowers', 'zero', 1, 'um', 2, 'dois', 3, 'tres', 3, 'quatro',
            4, 'cinco', 5, 'seis', 6, 'sete', 7, 'oito', 8, 'nove', 9, 'dez',
            10))
    print(redis.set_value('teste', 1))

    # print("Len of superpowers is %s" % redis.zcard('superpowers'))
    print("match %s" % redis.zcard('superpowers'))

    # print(redis.zrank('superpowers', 'dois'))

    # print(redis.zrange('superpowers', 2, 6))

    # print(redis.dbSize())
    # # redis.delete('mais um teste')
    # print(redis.storage)
