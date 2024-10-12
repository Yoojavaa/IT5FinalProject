import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()

    def register(self, name, username, password):
        sql = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, username, password))
        self.db.commit()

    def login(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(sql, (username, password))
        user = self.cursor.fetchone()
        return user
    def rent_car(self, customer_name, contact_number, car_type, date_rented):
        sql = "INSERT INTO rent (customer_name, contact_number, car_type, date_rented) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (customer_name, contact_number, car_type, date_rented))
        self.db.commit()

    def fetch_rentals(self):
        sql = "SELECT * FROM rent"
        self.cursor.execute(sql)
        rentals = self.cursor.fetchall()
        return rentals

    def update_rental(self, rental_id, customer_name, contact_number, car_type, date_rented, date_returned):
        sql = """UPDATE rent
                 SET customer_name = %s, contact_number = %s, car_type = %s, date_rented = %s, date_returned = %s
                 WHERE id = %s"""
        self.cursor.execute(sql, (customer_name, contact_number, car_type, date_rented, date_returned, rental_id))
        self.db.commit()

    def delete_rental(self, rental_id):
        sql = "DELETE FROM rent WHERE id = %s"
        self.cursor.execute(sql, (rental_id,))
        self.db.commit()

    def logout(self):
        pass
