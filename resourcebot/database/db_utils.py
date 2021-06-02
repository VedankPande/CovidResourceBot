import sqlite3
from sqlite3 import Error

#cities = ['pune','mumbai','banglore','kochi','delhi','kolkatta','madras','ahmedabad','jaipur','nagpur','thane'] #poona
#resources = ['oxygen','ventilator','bed','icu','test','fabiflu','remdesivir','favipiravir','tocilizumab','plasma','food','ambulance','amphotericin B']
#restrict_list = ['need','needs','needed','require','required','requires','requirement','requirements']


class DatabaseHandler:
    def __init__(self,database):
        self.database = database

    @property
    def connection(self):
        try:
            conn = sqlite3.connect(self.database)
        except Error as e:
            return e
        return conn
    
    @property
    def cursor(self):
        try:
            cursor = self.connection.cursor()
        except Exception as e:
            return e
        return cursor
    
    def show_tables(self):
        res = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(res.fetchall())
        self.connection.close()

    def get_all(self,table):
        try:
            res = self.cursor.execute(f"SELECT * FROM {table}")
        except Error as e:
            return e
        self.cursor.close()
        self.connection.close()
        return [value[0] for value in res.fetchall()]


    # def insert(self,table,value):
    #     try:
    #         self.cursor.execute(f"INSERT INTO {table} VALUES (?);",[value])
    #     except Error as e:
    #         return e
    #     self.connection.commit()
    #     self.cursor.close()
    #     self.connection.close()



    # def delete(self,table,value,all = False):
    #     if not all:
    #         try:
    #             self.cursor.execute(f'DELETE FROM {table} WHERE name = (?)',[value])
    #         except Error as e:
    #             return e
    #     else:
    #         try:
    #             self.cursor.execute(f'DELETE FROM {table}')
    #         except Error as e:
    #             return e

    #     self.connection.commit()
    #     self.cursor.close()
    #     self.connection.close()
    #     return self.get_all(table)
    


if __name__ == "__main__":
    pass
