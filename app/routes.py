from flask import jsonify, request
from app import app
from app.models.models import session, Student, EnglishWord
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/list_of_students", methods=['GET'])
@jwt_required()
def get_list_of_student():
    """for getting all students"""
    students = Student.query.all()
    serialized = []
    for student in students:
        serialized.append({
            'id': student.user_id,
            'name': student.user_name,
            'surname': student.user_surname,
            'email': student.email
        })
    return jsonify(serialized)

#                       testing in command line
# from app import app, test_client
# res = test_client.get('/list_of_students', headers = {'Authorization': 'valid token'})
# res.get_json()


@app.route("/registration", methods=['POST'])
def student_registration():
    """function for registration student"""
    params = request.json
    new_student = Student(**params)
    session.add(new_student)
    session.commit()
    token = new_student.get_token()
    return {'access token: ': token}


@app.route("/add_new_word", methods=['POST'])
@jwt_required()
def adding_new_word():
    """function for adding new word"""
    params = request.json
    id_student = get_jwt_identity()
    new_word = EnglishWord(user_id=id_student, **params)

    session.add(new_word)
    session.commit()
    return {'word: ': 'added'}


@app.route('/login', methods=['POST'])
def login_student():
    params = request.json
    user = Student.authenticate(**params)
    token = user.get_token()
    return {'access token: ': token}

# res = test_client.post('/registration',
# json= {'name':'practise in terminal', 'description':'run test client'})
# res = test_client.get('/list_of_student')
# res.status_code


@app.route("/personal_information/<int:student_id>", methods=['PUT'])
@jwt_required()
def update_tutorial(student_id):
    """for editing information about student"""
    student_id_token = get_jwt_identity()
    student = Student.query.filter(Student.user_id == student_id, Student.user_id == student_id).first()
    params = request.json
    if not student:
        return {'message': 'This student did not registered in db'}, 400
    for key, value in params.items():
        setattr(student, key, value)
    session.commit()
    serialized = {
        'id': student.user_id,
        'name': student.user_name,
        'surname': student.user_surname,
        'email': student.email
    }
    return jsonify(serialized)

# from app import test_client
# res = test_client.put('/personal_information/2', json = {......})
# res.status_code


@app.route('/personal_information/<int:student_id>', methods=['DELETE'])
@jwt_required()
def delete_tutorial(student_id):
    """for deleting student"""
    student_id_token = get_jwt_identity()
    student = Student.query.filter(Student.user_id == student_id, Student.user_id == student_id_token).first()
    if not student:
        return {'message': 'This student did not registered in db'}, 400
    session.delete(student)
    session.commit()
    return '', 204
# from app import test_client
# res = test_client.delete('/personal_information/1')
# res.status_code


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
