import mysql.connector


class MysqlSubmissions(object):
    def __init__(self):
        self.db = None

    def connect(self, host, database, user, password):
        self.db = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def create_table(self, table_name):
        db_cursor = self.db.cursor()
        create_table_query = f" \
            CREATE TABLE IF NOT EXISTS {table_name} \
            (   sub_id VARCHAR(120) UNIQUE NOT NULL,\
                sub_creation_time DATETIME NOT NULL,\
                is_posted BOOL DEFAULT 0,\
                PRIMARY KEY (sub_id)\
            );"

        db_cursor.execute(create_table_query)
        db_cursor.close()

    def insert(self, data):
        db_cursor = self.db.cursor()
        insert_query = "INSERT IGNORE INTO life_pro_tips (sub_id, sub_creation_time) \
                        VALUES (%s, %s)"
        db_cursor.executemany(insert_query, data)
        self.db.commit()

        db_cursor.close()

    def get_new_post(self):
        db_cursor = self.db.cursor()
        select_query = "SELECT sub_id, sub_creation_time, is_posted FROM life_pro_tips \
                        INNER JOIN(SELECT is_posted AS isposted, MIN(sub_creation_time) \
                        AS maxtime FROM life_pro_tips WHERE is_posted = 0) mingroup \
                        ON life_pro_tips.sub_creation_time = mingroup.maxtime"

        db_cursor.execute(select_query)
        results = db_cursor.fetchall()
        db_cursor.close()

        return results

    def get_pending_posts(self):
        db_cursor = self.db.cursor()
        select_query = "SELECT sub_id FROM life_pro_tips WHERE is_posted = 0"
        db_cursor.execute(select_query)
        results = db_cursor.fetchall()
        db_cursor.close()
        return results

    def set_posted(self, sub_id, is_posted=1):
        db_cursor = self.db.cursor()
        update_query = f"UPDATE life_pro_tips set is_posted = 1 WHERE sub_id = '{sub_id}'"
        db_cursor.execute(update_query)
        self.db.commit()
        db_cursor.close()

    def close(self):
        self.db.close()



