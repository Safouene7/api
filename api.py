from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    user='root', password='safouene', host='127.0.0.1', port="3306", database='user')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM user.tab')
users = cursor.fetchall()
connection.close()

print(users)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users["id"]:
        return {"message": "User not found"}

@app.route('/users', methods=['POST'])
def post_user():
     data = request.json
     connection = mysql.connector.connect(
       user='root', password='safouene', host='127.0.0.1', port="3306", database='user')
     cursor = connection.cursor()
     insert = 'INSERT INTO user.tab (id, name, lastname) VALUES (%s, %s, %s)'
     values = (data["id"], data["name"], data["lastname"])
     cursor.execute(insert, values)
     connection.commit()
     connection.close()

     return {"message": "User created"}


@app.route('/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    data = request.get_json()
    connection = mysql.connector.connect(
        user='root', password='safouene', host='127.0.0.1', port="3306", database='user')
    cursor = connection.cursor()
    update = 'UPDATE user.tab SET name = %s, lastname = %s WHERE id = %s'
    print(data)
    #values = (data["name"], data["lastname"], user_id)
    #cursor.execute(update, values)
    #connection.commit()
    #connection.close()
   
    return {"message": "User updated"}



@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user_id in users:
        del user_id
    return {"message":"User deleted"}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)




    



