Very Basic and quite simple todo application based on`flask`, `REST` just for educational purpose.

## Download :
open terminal:
```
mkdir flask_rest_project
cd flask_rest_project/
git clone https://github.com/sohan-reza/Flask_rest_project.git .
```

## Run:
```
    python -m venv venv
    source venv/bin/activate
    pip install flask
    pip install flask-httpauth
    python code/app.py
```
this will run the default development server on http://127.0.0.1:5000

this api has only two route:
- /todo/api/v1.0/tasks
`POST` request on this route will create a new task. 
`GET` request on ths route will return all the remain task. but this route require a username and password just for basic authintication [username: onion, password: flask-rock]

- /todo/api/v1.0/tasks/<int:task_id>
`PUT` request on this route will update the specific task.
`DELETE` request on this route will delete the specific task.
`GET` request on this route will return the specific task.

you should use `curl` to test this api.
## Example
```
$ curl -u onion:flask-rock http://127.0.0.1:5000/todo/api/v1.0/tasks

{
  "tasks": [
    {
      "description": "Code the todo app and push this to github",
      "done": false,
      "title": "Write the code",
      "uri": "http://127.0.0.1:5000/todo/api/v1.0/tasks/1"
    },
    {
      "description": "Read all the bookmarked REST tutorial",
      "done": false,
      "title": "Learn about REST",
      "uri": "http://127.0.0.1:5000/todo/api/v1.0/tasks/2"
    }
  ]
}

```
 


