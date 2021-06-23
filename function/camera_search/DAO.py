import cx_Oracle
from DTO import CameraDTO
import json
import collections

class CameraDAO:
    def allCams(self,brand,category,test_level):
        cam_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                aa = {'brand':brand,'category':category,'test_level':test_level}
                if list(aa.values()).count(' ') == 3:
                    cur.execute("select * from cameras")
                if list(aa.values()).count(' ') == 2:
                    if aa['brand'] != ' ':
                        cur.execute("select * from cameras where brand=:brand order by price asc", brand = brand)
                    elif aa['category'] != ' ':
                        cur.execute("select * from cameras where category=:category order by price asc", category = category)
                    else:
                        cur.execute("select * from cameras where test_level=:test_level order by price asc", test_level = test_level)
                
                if list(aa.values()).count(' ') == 1:
                    if aa['brand'] == ' ':
                        cur.execute("select * from cameras where category=:category and test_level=:test_level order by price asc", category = category,test_level = test_level)
                    if aa['category'] == ' ':
                        cur.execute("select * from cameras where brand=:brand and test_level=:test_level order by price asc", brand = brand,test_level = test_level)
                    if aa['test_level'] == ' ':
                        cur.execute("select * from cameras where brand=:brand and category=:category order by price asc", brand = brand,category = category)

                if list(aa.values()).count(' ') == 0:
                    cur.execute("select * from cameras where brand=:brand and category=:category and test_level=:test_level order by price asc",brand = brand,category = category,test_level = test_level)

                rows = cur.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['brand'] = row[0]
                    d['model'] = row[1]
                    d['price'] = row[2]
                    d['category'] = row[3]
                    d['shutter'] = row[4]
                    d['exposure'] = row[5]
                    d['level'] = row[6]
                    v.append(d)
                print(v)
                cam_data = json.dumps(v,ensure_ascii=False)
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return cam_data 

    def addCams(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("insert into camera values (:brand, :model, :price, :format)",
                            brand=dto.getBrand(), model=dto.getModel(), price=dto.getPrice(), format=dto.getFormat())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def delCams(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("delete from camera where brand=:brand and model=:model",
                            brand=dto.getBrand(), model=dto.getModel())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    def showall(self): 

        cam_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from camera")
                rows = cur.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['brand'] = row[0]
                    d['model'] = row[1]
                    d['price'] = row[2]
                    d['format'] = row[3]
                    v.append(d)
                cam_data = json.dumps(v,ensure_ascii=False)

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

        return cam_data


if __name__ == "__main__":
    cam = CameraDAO()
    cam.allCams("NIKON"," "," ")
    


# cam_data = '{"brand":"' + row[0] + '", "model":"' + row[1] + '", "price":' + str(row[2]) + '", "format":' + str(row[3]) + '}'
