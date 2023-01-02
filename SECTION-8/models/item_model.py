from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'                       # Telling db the table name which it has to access.
    id = db.Column(db.Integer,primary_key=True)   #  Telling db the column name the inetger type and telling it that it is the primary key(means unique, indexed based on this)
    name = db.Column(db.String(80))          # telling it this is a string and should not be more than 80 chactrs
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #lets say that in items table there is a mention of which store is it refering to like a colum of store_id which is representing a store in stores table 
                                                                # so the store_id lets say 2 is primery key in stores table for a store but a forign key for items table which link the items and stores in which they are
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):

        return{'name':self.name,'price': self.price}

    @classmethod                                  # we create a class method so that this function can be accessed by both get and post function
    def find_by_name(cls, name):                  # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first()     #query.filter_by is bulit in sqlacamy

    def save_to_db(self):
    #def insert(self):
        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()

        #query = "INSERT INTO items VALUES (?,?)"
        #cursor.execute(query,(self.name,self.price))

        #connection.commit()
        #connection.close()          
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query,(self.price,self.item))
    #     connection.commit()
    #     connection.close()
        db.session.delete(self)
        db.session.commit()


