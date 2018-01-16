# Chapter03
# test_webtest_02.py
import unittest
import os
import sys
sys.path.append('../Chapter02')

class TestMyApp(unittest.TestCase):

    def setUp(self):
        # HTTP_SERVER 환경변수가 설정됐다면,
        # 그 값을 엔드포인트로 사용한다.(통합 테스트)
        http_app = os.environ.get('HTTP_SERVER')
        if http_app is not None:
            from webtest import TestApp
            self.app = TestApp(http_app)
        else:
            # WSGI 애플리케이션을 호출한다.(기능 테스트)
            from flask_basic import app
            from flask_webtest import TestApp
            self.app = TestApp(app)
    
    def test_help(self):
        # /api 엔드포인트를 호출한다.
        hello = self.app.get('/api')

        # 응답을 검사한다.
        self.assertEqual(hello.json['Hello'], 'World!')

if __name__ == '__main__':
    unittest.main()