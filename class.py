import MySQLdb
import socket


class Person:
    def __init__(self, name, age, height, weight):
        self.name = name 
        self.age = age
        self.height = height  # cm
        self.weight = weight  # kg
    
    def bmi(self):
        hight_m =  self.height/100.0      # 身長をメートル単位に修正
        return self.weight / hight_m**2.0 # BMIを計算

class SQL:
    def __init__(self, name):
        self.name = name

        print(name)
    
    def sql(self):
        conn = MySQLdb.connect(
        user='test',
        passwd='test',
        host='127.0.0.1',
        db='forge')

        cur = conn.cursor()
        sql = "select * from new_table"
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close
        conn.close
        
  
def service_name(port, protocol_name):
    print('Port:', port)
    print('protocolname:', protocol_name)
    print('Service name:', socket.getservbyport(port, protocol_name))
    print('--------------------')


taro = Person("太郎", 23, 170, 60)
jiro = Person("二郎", 18, 168, 73)

taro_bmi = taro.bmi()
jiro_bmi = jiro.bmi()


print(taro.name)
print(jiro.name)

print("太郎のBMI：", taro_bmi )
print("二郎のBMI：", jiro_bmi )


aoi = SQL("aoi")


aoi.sql()



host = socket.gethostname()
print(host) # ホスト名

ip = socket.gethostbyname(host)
print(ip) # 192.168.○○○.○○○


service_name(port=80, protocol_name='tcp')
service_name(port=25, protocol_name='tcp')