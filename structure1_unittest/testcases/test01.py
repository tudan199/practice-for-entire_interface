import requests
import sys
import xlrd
sys.path.append('c:\\Users\\eagle\\Desktop\\practise\\practice for entire_interface\\structure1_unittest')
from utils.requests_db import commit_morning,query
import unittest

class TryUnittestRequest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('\nthis is test01 setupclass')
    # @classmethod
    # def tearDownClass(cls):
    #     print('\nthis is teardownclass')
    
    # def setUp(self):
    #     print('\nthis is setup')
    # def tearDown(self):
    #     print('\nthis is tearDown  git')
    def test_request01(self):
        userinfo={
            'user.loginName':'819626117@qq.com',
            'user.loginPassword':'tudan123'
            }
        res=requests.post(url='http://127.0.0.1:8080/morning/user/userLogin',data=userinfo)
        print(res.json())
        assert res.status_code==200
        assert res.json()['success']==True
        sql='select * from tb_account where email="%s";'%userinfo['user.loginName']
        result=query(sql)
 
        assert len(result)==1
        print('test01测试通过')
