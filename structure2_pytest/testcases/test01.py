import pytest
import requests
from utils.requests_db import query,commit_morning
def test_01():
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
def test_02():
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
    print('test02测试通过')


