from flask import Flask, request, jsonify
import mysql.connector
#setup
app = Flask(__name__)

db = mysql.connector.connect(
  host="host-ip", # use docker inspect for ip
  user="root",
  password="password", # I dont use these credentials ;)
  database="monopoly"
)

#get all posts
@app.route('/get-posts', methods=['GET'])
def get_posts():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    result = cursor.fetchall()
    posts = []
    for row in result:
        post = {
            'id': row[0],
            'title': row[1],
            'content': row[2],
            'created_at': str(row[3]),
            'user_id': row[4]
        }
        posts.append(post)
    return jsonify(posts)

#new post
def new_post(title, content, email):
    cursor = db.cursor()
    query = "SELECT id FROM users where email= %s"
    cursor.execute(query, (email,)) #the comma at the end is for python to recognize "email" as a tuple not a value
    result = cursor.fetchone()
    user_id = result[0]
    query = "INSERT INTO posts (title, content, user_id) VALUES (%s, %s, %s)"
    values = (title, content, user_id)
    cursor.execute(query, values)
    db.commit()


#new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']
    cursor = db.cursor()
#email check
    query = "SELECT id FROM users WHERE email= %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    if result is not None:
        return "This email already exists!", 409
#Insert user
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    db.commit()
#new post
    titel = "create user"
    content = "created the user account \"" + str(name) + "\" with the email: " + str(email)
    new_post(titel, content, email)

    return 'User created successfully'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

