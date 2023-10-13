from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User	# the regex module

class Appointment:
    db_name = "examen_2"
    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['users_id']
        self.user = data.get('user', None)

    
    @classmethod
    def obtener_todo(cls):
        query = "SELECT * FROM appointments;"
        results = connectToMySQL(cls.db_name).query_db(query)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments

    @classmethod
    def save(cls, data):
        query = "INSERT INTO appointments (task, date, status, users_id) VALUES (%(task)s, %(date)s, %(status)s, %(users_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def obtener_con_id(cls, user_id):
        query = "SELECT * FROM appointments WHERE users_id = %(user_id)s;"
        data = {'user_id': user_id}
        results = connectToMySQL(cls.db_name).query_db(query, data)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments
    
    @classmethod
    def destroy(cls, appointment_id):
        query = "DELETE FROM appointments WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, {"id": appointment_id})
    
    @classmethod
    def get_by_id(cls, appointment_id):
        query = "SELECT * FROM appointments WHERE id = %(id)s;"
        data = {'id': appointment_id}
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def update(cls, data):
        query = "UPDATE appointments SET task = %(task)s, date = %(date)s, status = %(status)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_completed_tasks(cls):
        query = "SELECT * FROM appointments WHERE status = 'Completada';"
        results = connectToMySQL(cls.db_name).query_db(query)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments
    
    @classmethod
    def get_incomplete_tasks(cls):
        query = "SELECT * FROM appointments WHERE status = 'incompleta';"
        results = connectToMySQL(cls.db_name).query_db(query)
        appointments = []
        for row in results:
            appointments.append(cls(row))
        return appointments