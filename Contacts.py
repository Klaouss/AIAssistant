import face_recognition

class Contact:
    import face_recognition

    def __init__(self,name,first_part,last_part,face_encoding):
        self.name = name
        self.first_part = first_part
        self.last_part = last_part
        self.face_encoding = face_encoding

Panos = Contact(name='Panos',first_part='pyannakopoulos',last_part='uniwa.gr')
Dad = Contact(name='Dad',first_part='cklaouda',last_part='otenet.gr')
Mom = Contact(name='Mom',first_part='christinaklaoudatou',last_part='yahoo.de')
Stavros = Contact(name='Stavros',first_part='stavrosklaoudatos1',last_part='gmail.com',face_encoding=face_recognition.face_encodings(face_recognition.load_image_file('stavros.jpg')))
Leo = Contact(name='Leo',first_part='leo.vournas',last_part='gmail.com')
Elias = Contact(name='Elias',first_part='elias.bourlas', last_part='gmail.com')
AntonisMag = Contact(name='AntonisMag',first_part='antonismagriotis',last_part='gmail.com',face_encoding=face_recognition.face_encodings(face_recognition.load_image_file('Mag.jpg')))
Markos = Contact(name='Markos',first_part='mlemos',last_part='gmail.com',face_encoding=face_recognition.face_encodings(face_recognition.load_image_file('Mark.jpg')))