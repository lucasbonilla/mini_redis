import unittest
import threading
from .myredis import *
from .structure import *

class TestMyRedis(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.redis = MyRedis()
        self.responses = ReturnValue()

    def test_set(self):
        input_ = 12
        key_ = 'teste'
        try_ = self.redis.set_value(key_, input_)
        self.assertEqual(try_, self.responses.OK_)
    
    def test_set_extime(self):
        input_ = 12
        key_ = 'teste'
        extime_ = 2
        try_ = self.redis.set_value(key_, input_, extime_)
        self.assertEqual(try_, self.responses.OK_)

    def test_set_extime_threads(self):
        threads = []
        key_ = 'test'
        for i in range(5):
            new_thread = threading.Thread(name="input_number_"+str(i), target=self.redis.set_value, args=(key_ + ' ' + str(i), i, i+3))
            threads.append(new_thread)
        for i in range(5):
            threads[i].start()
        for i in range(5):
            threads[i].join()
        for i in range(5):
            try_ = self.redis.get_value('test '+str(i))
            self.assertEqual(try_, i)
            

    @unittest.expectedFailure
    def test_get_with_error(self):
        key_ = 'test 1'
        self.redis.set_value('test 0', 12)
        try_ = self.redis.get_value(key_)
        self.assertEqual(try_, 12)

    def test_delete(self):
        self.redis.set_value('test 0', 12)
        try_ = self.redis.delete_value('test 0')
        self.assertEqual(try_, 1)

    @unittest.expectedFailure
    def test_delete_with_error(self):
        self.redis.set_value('test 0', 12)
        try_ = self.redis.delete_value(None)
        self.assertEqual(try_, 1)

    def test_delete_many(self):
        for i in range(10):
            self.redis.set_value('test '+str(i), i+10)
        try_ = self.redis.delete_value('test 0', 'test 4', 'test 8')
        self.assertEqual(try_, 3)

    def test_dbsize(self):
        for i in range(10):
            self.redis.set_value('test '+str(i), i+10)
        try_ = self.redis.dbSize()
        self.assertGreaterEqual(try_, 0)

    def test_incr(self):
        self.redis.set_value('test 0', 12)
        was = self.redis.get_value('test 0')
        try_ = self.redis.incr('test 0')
        self.assertEqual(try_, was + 1)

    def test_zadd(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4)
        try_ = self.redis.zadd('test 0', 'value 1', 2, 'value 2', 3, 'value 3', 4, 'value 4', 5, 'value 5', 5)
        self.assertEqual(try_, 1)

    def test_zcard_1(self):
        self.redis.set_value('test 0', 12)
        try_ = self.redis.zcard('test 0')
        self.assertEqual(try_, 1)

    def test_zcard_2(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4)
        try_ = self.redis.zcard('test 0')
        self.assertEqual(try_, 4)

    def test_zcard_3(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4)
        try_ = self.redis.zcard('test 0', 'value 1', 1, 'value 2', 2)
        self.assertEqual(try_, 2)

    def test_zrank_1(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4)
        try_ = self.redis.zrank('test 0', 'value 3')
        self.assertEqual(try_, 2)

    def test_zrank_2(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4)
        try_ = self.redis.zrank('test 0', 'value 10')
        self.assertEqual(try_, self.responses.NIL_)

    def test_zrange(self):
        self.redis.zadd('test 0', 'value 1', 1, 'value 2', 2, 'value 3', 3, 'value 4', 4, 'value 5', 5, 'value 6', 6, 'value 7', 7, 'value 8', 8)
        try_ = self.redis.zrange('test 0', 2, 5)
        self.assertEqual(len(try_), 3)

    


if __name__ == '__main__':
    unittest.main()