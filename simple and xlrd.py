import requests
from utils.requests_db import query,commit_morning
import xlrd

"""
用例1：测试登录接口，登录成功
"""

# userinfo={
#     'user.loginName':'819626117@qq.com',
#     'user.loginPassword':'tudan123'
#     }
# res=requests.post(url='http://127.0.0.1:8080/morning/user/userLogin',data=userinfo)
# print(res.json())
# assert res.status_code==200
# assert res.json()['success']==True
# sql='select * from tb_account where email="%s";'%userinfo['user.loginName']
# result=query(sql)
# print(result)
# print(type(result))
# assert len(result)==1
# print('测试通过')

"""
用例2：数据驱动，更新tb_account表

"""
#获取文件对象
file_test=xlrd.open_workbook(filename=r'C:\Users\eagle\Desktop\test.xls')

#获取标签页
sheet=file_test.sheet_by_name('Sheet1')
result=[]
for i in range(0,sheet.nrows):
    rows=sheet.row_values(i)
    sql='update tb_goods set goods_price=%s where goods_id=%s'%(rows[1],str(rows[0])[:1])
    commit_morning(sql)
print('执行成功')    
