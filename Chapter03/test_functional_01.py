# Chapter03
# test_functional_01.py
import unittest
import json
import sys
sys.path.append('../Chapter02')

class TestApp(unittest.TestCase):
    def setUp(self):
        from flask_basic import app as _app
        self.app = _app
    def test_help(self):
        # app과 연동하기 위해 FlaskClient 인스턴스를 생성한다.
        app = self.app.test_client()

        # /api 엔드포인트를 호출한다.
        hello = app.get('/api')

        # 응답을 검사한다.
        body = json.loads(str(hello.data, 'utf8'))
        self.assertEqual(body['Hello'], 'World!')


if __name__ == '__main__':
    unittest.main()