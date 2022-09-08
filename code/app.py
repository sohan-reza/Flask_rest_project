from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

##App Model

tasks= [
    {
        'id':1,
        'title': 'Write the code',
        'description': 'Code the todo app and push this to github',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn about REST',
        'description': 'Read all the bookmarked REST tutorial',
        'done': False
    }
]



##App Controller
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def index():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id']==task_id]
    if len(task)==0:
        abort(404)
    return jsonify({'task':task[0]})

## Error Handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)




if __name__=='__main__':
    app.run(debug=True)
