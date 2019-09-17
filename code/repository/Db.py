# import sqlite3
#
# dbname = 'my.db';
#
# class Db:
#     connect (self):
#         self.connection = sqlite3.connect(dbname)
#
#     def query (self, query, params)
#         cursor = self.connection.cursor()
#         return cursor.execute(query, params)
#
#     def nonQuery(self, query, params)
#         cursor = self.connection.cursor()
#         cursor.execute(query, params)
#
#     def fetch(self, cursor):
#         return cursor.fetchone()
#
#     def commit (self)
#         self.connection.commit()
#
#     def close(self):
#         self.connection.close()
