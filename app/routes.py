from flask import jsonify, request
from app import app
from app.models.models import session

tutorial = [
    {'id': 1,
     'name': 'Intro',
     'description': 'Get, Post routes'},
    {'id': 2,
     'name': 'More feature',
     'description': 'Put, Delete routes'}
]


@app.route("/tutorial", methods=['GET'])
def get_tutorial():
    return jsonify(tutorial)
# from app import app, test_client
# res = test_client.get('/tutorial')
# res.get_json()


@app.route("/tutorial", methods=['POST'])
def add_tutorial():
    """function for adding tutorial"""
    new_tutorial = request.json
    tutorial.append(new_tutorial)
    return jsonify(tutorial)

# res = test_client.post('/tutorial',
# json= {'name':'practise in terminal', 'description':'run test client'})
# res = test_client.get('/tutorial')
# res.status_code


@app.route("/tutorial/<int:tutorial_id>", methods=['PUT'])
def update_tutorial(tutorial_id):
    """for updating data in tutorial"""
    item = next((x for x in tutorial if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)
    return item

# from app import test_client
# res = test_client.put('/tutorial/2', json = {'description': 'Put route'})
# res.status_code


@app.route('/tutorial/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    """for deleting tutorial"""
    idx, _ = next((x for x in enumerate(tutorial) if x[1]['id'] == tutorial_id), (None, None))
    tutorial.pop(idx)
    return '', 204
# from app import test_client
# res = test_client.delete('/tutorial/1')
# res.status_code


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
