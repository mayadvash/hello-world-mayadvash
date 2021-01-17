from flask import Flask, redirect, url_for, render_template, request
from flask import request
from flask import session
from flask import Blueprint, render_template
import mysql.connector
import os


Assigment10 = Blueprint('Assigment10', __name__,
                        static_folder='static',
                        static_url_path='/Assignment10',
                        template_folder='templates')

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # use for insert /update/delete
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # use for select statement
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
 # ------------------------------------------------------ #





@Assigment10.route('/Assignment10_users')
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('Assignment10_users.html', users=query_result)

@Assigment10.route('/Assignment10', methods=['GET', 'POST'])
def insert_user():
    message=''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
        interact_db(query, query_type='commit')
        message="the new user was insert successfully!"
        query = "SELECT * FROM users"
        query_result = interact_db(query, query_type='fetch')
        return render_template('/Assignment10_users.html', insert_message=message, users=query_result)
    message = 'There was a problem. Please try again.'
    return render_template('/Assignment10.html', insert_message=message)

@Assigment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    message_delete = ''
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s'" % user_id
        interact_db(query, query_type='commit')
        delete_message = f'user with id {user_id} is deleted'
        query = "SELECT * FROM users"
        query_result_all = interact_db(query, query_type='fetch')
    return render_template('/Assignment10_users.html', delete_message=delete_message, users=query_result_all)


@Assigment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    message_update = ''
    if request.method == 'GET':
        user_id = request.args['id']
        user_name = request.args['name']
        query = "UPDATE users SET name = '%s'"" WHERE id='%s'"  % (user_name ,user_id )
        interact_db(query, query_type='commit')
        return redirect('/Assignment10_users')
    return 'updated user'

