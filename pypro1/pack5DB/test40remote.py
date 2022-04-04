# 원격(remote) 데이터베이스 연동 rdbms
import MySQLdb

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) #딕트타입이여서 *이 2개
    cursor = conn.cursor()

    """    <- 한번 넣고나면 주석 처리 해야한다. (pritmary키 때문에 이미 있다고 판단)
    print('insert ---') # insert는 성공하면 1, 실패하면 0 을 반환한다.
    #isql = "insert into sangdata(code,sang,su,dan) values(10, '신상',5,5000)"
    #isql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)"
    isql = "insert into sangdata values(%s,%s,%s,%s)"
    sql_data = (10, '신상',5,5000) # 가독성이 더 좋다.
    #sql_data = 10, '신상',5,5000
    cursor.execute(isql, sql_data)
    conn.commit()
    """

    """
    print('update ---')
    usql = "update sangdata set sang=%s,su=%s where code=%s"
    sql_data = ('얼죽아',30,10)
    cou = cursor.execute(usql, sql_data)
    print('cou :' ,cou)
    conn.commit()
    """
    
    """
    print('delete ---')
    input_code = '10'
    #dsql = "delete from sangdata where code=" + input_code # secure coding 가이드라인에 위배
    
    #dsql = "delete from sangdata where code=%s"
    #cou = cursor.execute(dsql, (input_code,))
    
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    cou = cursor.execute(dsql)
    conn.commit()
    if cou > 0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    """
    
    print('select ---')
    sql = "select code,sang,su,dan from sangdata" # *(all) 보다는 구체적 작성해주는게 더 빠르다.
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)
        print(' %s %s %s %s'%data)
    """
    print()
    for data in cursor:
        print(data[0], data[1], data[2], data[3])

    print()
    for (code, sang, su, dan) in cursor: # 가독성이 좋아 이걸 더 선호
        print(code, sang, su, dan)

    print()
    for (a, kbs, mbc, dan) in cursor: #변수명으로도 출력이 가능하다. 가독성이 좋지않다.
        print(a, kbs, mbc, dan)
    """

except Exception as e:
    print('err : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()