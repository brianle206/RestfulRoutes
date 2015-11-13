
from system.core.model import Model

class Restful(Model):
    def __init__(self):
        super(Restful, self).__init__()
    def get_all(self):
        query = "SELECT  name, description, price, id FROM products"
        return self.db.query_db(query)
    def get_product_by_id(self, id):
        query = "SELECT * FROM products WHERE id = %s"
        data = [id]
        return self.db.query_db(query, data)
    def update(self, info):
        query = "UPDATE products SET name = %s, description = %s, price = %s, updated_at=NOW() WHERE id =%s"
        data = [info['name'],info['description'],info['price'],info['id']]
        return self.db.query_db(query, data)

    def add(self, info):
        query = "INSERT INTO products(name, description, price, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
        data = [info['name'], info['description'], info['price']]
        return self.db.query_db(query, data)

    def destroy(self, id):
        query = "DELETE FROM products WHERE id = %s"
        data = [id]
        return self.db.query_db(query,data)