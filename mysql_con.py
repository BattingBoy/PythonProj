import pymysql


class data_dto(object):
    def __init__(self, data_list):
        self.date = data_list[0]
        self.number = data_list[1]
        self.red_1 = data_list[2]
        self.red_2 = data_list[3]
        self.red_3 = data_list[4]
        self.red_4 = data_list[5]
        self.red_5 = data_list[6]
        self.red_6 = data_list[7]
        self.blue = data_list[8]


class mysql_con(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root199304', db='test')
        self.cursor = self.conn.cursor()

    def insert(self, data):
        inser_sql = """INSERT INTO data_set (date,number,red_1,red_2,red_3,red_4,red_5,red_6,blue)
                        VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')
        """ % (
        data.date, data.number, data.red_1, data.red_2, data.red_3, data.red_4, data.red_5, data.red_6, data.blue)
        try:
            self.cursor.execute(inser_sql)
            self.conn.commit()
        except:
            self.conn.rollback()

        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    data = ["2012","10",1,2,3,4,5,6,7]
    data_dto = data_dto(data)
    con = mysql_con()
    con.insert(data_dto)
