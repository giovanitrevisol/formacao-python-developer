from flask import Flask, jsonify, request
import json

app = Flask(__name__)

list_tasks = [
    {
        'id': '0',
        'responsible': 'Giovani Trevisol',
        'task': 'Study Python every day!',
        'status': 'ACTIVE'
    }
]


@app.route('/task/<int:id>', methods=['GET', 'PUT'])
def task(id):
    if request.method == 'GET':
        try:
            response = list_tasks[id]
        except IndexError:
            response = {'status': 'error', 'message': 'task not found!'}
        except Exception:
            response = {'status': 'error', 'message': 'internal error!'}
        return jsonify(response)
    elif request.method == 'PUT':
        try:
            task = list_tasks[id]
            new_status = json.loads(request.data)
            task['status'] = new_status["status"]
            response = {'status': 'Success', 'message': 'task is updated with success!'}
        except IndexError:
            response = {'status': 'error', 'message': 'task not found!'}
        except Exception:
            response = {'status': 'error', 'message': 'internal error!'}
        return jsonify(response)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        return jsonify(list_tasks)

    elif request.method == 'POST':
        data = json.loads(request.data)
        new_id = len(list_tasks)
        data['id'] = new_id
        list_tasks.append(data)
        return jsonify({'message': 'Task add success!!! Id: {}'.format(new_id)})


if __name__ == '__main__':
    app.run(debug=True)
