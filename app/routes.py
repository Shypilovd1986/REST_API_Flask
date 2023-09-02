from flask import jsonify, request
from app import app
from app.models.models import session, Student, EnglishWord


@app.route("/list_of_student", methods=['GET'])
def get_tutorial():
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
# res = test_client.get('/list_of_student')
# res.get_json()


@app.route("/registration", methods=['POST'])
def add_tutorial():
    """function for registration student"""
    new_student = Student(**request.json)
    session.add(new_student)
    session.commit()
    serialized = {
        'id': new_student.user_id,
        'name': new_student.user_name,
        'surname': new_student.user_surname,
        'email': new_student.email
    }
    return jsonify(serialized)

# res = test_client.post('/registration',
# json= {'name':'practise in terminal', 'description':'run test client'})
# res = test_client.get('/list_of_student')
# res.status_code


@app.route("/personal_information/<int:student_id>", methods=['PUT'])
def update_tutorial(student_id):
    """for editing information about student"""
    student = Student.query.filter(Student.user_id == student_id).first()
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
def delete_tutorial(student_id):
    """for deleting student"""
    student = Student.query.filter(Student.user_id == student_id).first()
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
