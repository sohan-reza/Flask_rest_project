from flask import Flask, jsonify

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
@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
def index():
    return jsonify({'tasks': tasks})

if __name__=='__main__':
    app.run(debug=True)
