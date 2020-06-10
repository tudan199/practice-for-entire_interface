import pymysql
def connect_morning():
    dbinfo={
    'host':'127.0.0.1',
    'password':'123456',
    'user':'root',
    'db':'db_morning'
    }
    db=pymysql.connect(**dbinfo)
    cur=db.cursor()
    return cur,db
def query(sql):
    cur=connect_morning()[0]
    cur.execute(sql)
    result=cur.fetchall()
    connect_morning()[1].close()
    return result


def commit_morning(sql):
    dbinfo={
    'host':'127.0.0.1',
    'password':'123456',
    'user':'root',
    'db':'db_morning'
    }
    db=pymysql.connect(**dbinfo)
    cur=db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        db.close()
        return '执行成功'
    except:
        return '执行失败'
if __name__=='__main__':
    sql2='select * from tb_account limit 1;'
    print(query(sql2))
    print('test')
    sql3='update tb_goods set goods_price="540" where goods_id="1";'
    print(commit_morning(sql3))
    
