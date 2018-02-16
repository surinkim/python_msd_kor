# Chapter03
# test_webtest_01.py
import unittest
import sys
sys.path.append('../Chapter02')
from flask_basic import app as _app

class TestMyApp(unittest.TestCase):
    def setUp(self):
        from webtest import TestApp
        # app과 연동하기 위한 클라이언트를 생성한다.
        self.app = TestApp(_app)

    def test_help(self):
        # /api 엔드포인트를 호출한다.
        hello = self.app.get('/api')

        # 응답을 검사한다.
        self.assertEqual(hello.json['Hello'], 'World!')

if __name__ == '__main__':
    unittest.main()