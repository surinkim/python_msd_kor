# Chapter03
# test_request_02.py
import unittest
from unittest import mock
import requests
from requests.exceptions import ConnectionError
import requests_mock
from test_request_01 import MyBugzilla

class TestBugzilla(unittest.TestCase):
    def test_bug_id(self):
        zilla = MyBugzilla('tarek@mozilla.com', server = 'http://yeah')
        link = zilla.bug_link(23)
        self.assertEqual(link, 'http://yeah/show_bug.cgi?id=23')

    @requests_mock.mock()
    def test_get_new_bugs(self, mocker):
        # 요청을 모방해서, 2개의 버그 목록을 반환한다.
        bugs = [{'id': 1184528}, {'id': 1184524}]
        mocker.get(requests_mock.ANY, json={'bugs': bugs})

        zilla = MyBugzilla('tarek@mozilla.com', server = 'http://yeah')
        bugs = list(zilla.get_new_bugs())

        self.assertEqual(bugs[0]['link'], 'http://yeah/show_bug.cgi?id=1184528')
        

    @mock.patch.object(requests, 'get', side_effect=ConnectionError('No network'))
    def test_network_error(self, mocked):
        # 서버 다운 등의 네트워크 에러 테스트
        zilla = MyBugzilla('tarek@mozilla.com', server='http://yeah')
        bugs = list(zilla.get_new_bugs())
        self.assertEqual(len(bugs), 0)

if __name__ == '__main__':
    unittest.main()