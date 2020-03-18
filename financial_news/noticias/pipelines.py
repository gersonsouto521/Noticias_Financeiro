import sqlite3


class NoticiasSqlitePipeline(object):

    def process_item(self, item, spider):
        self.conn.execute(
            'insert into noticias(title, href, data, image) values (:title, :href, :data, :image)',
            item
        )
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name ="noticias" '
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table noticias(id integer primary key, title text, href text, data text, image text)'
            )


    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider(self, spider):
        self.conn.close()