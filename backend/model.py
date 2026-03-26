from config import db

class Contact(db.Model):
    id = db.Column(db.Integer ,  primary_key = True)
    #while taking str input max length must be provided . try one with out length
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    
    #when we work with JSON we use camel case (cap letter diffrentiate the newWord)
    #when we use java we use snake case ( new_word)
    
    def to_json(self):
        return{
            "id": self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email,
        }

