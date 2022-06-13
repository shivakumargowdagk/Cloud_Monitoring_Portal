"""
we are added session and logout tab for my website
"""
# --------------------
# Create App (Object) for our website
# --------------------

import flask
from flask_session import Session
from flask import session

my_cloud_monitoring_app = flask.Flask("MycloudMonitoringApp")

my_cloud_monitoring_app.secret_key = "My Secrete paswword"
my_cloud_monitoring_app.config["SESSION_TYPE"] = "filesystem"

Session(my_cloud_monitoring_app)
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@my_cloud_monitoring_app.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@my_cloud_monitoring_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
    # --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@my_cloud_monitoring_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@my_cloud_monitoring_app.route('/validate', methods=['POST'])
def my_validate_page():
    # Task - 1 : Get user name & pass word entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    entered_username = entered_username.lower()
    # Connect to user_db.sqlite, check whether entered username and password
    # present. If not present then return login failed
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect(r'users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute(f"SELECT NAME, PASSWORD FROM USERS_TABLE WHERE NAME='{entered_username}' AND PASSWORD = '{entered_password}'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")
    # if we get record then username & password correct else wrong

    # This work is done, so close db connection
    my_db_connection.close()

    if len(my_db_result) > 0:
        session['username'] = entered_username
     #   return "login succesfully"
        return flask.redirect('/')
    else:
        return "Login Failed. Invalid Credentials <br><br> <a href='/login'>Go Back To Login</a>"

# ----------------
# POINTS - 1
# ----------------
# - We are sending data inside python object to html file
# - If we need to display python variable in html then we need to
#   write python code inside html
# - We can write python code inside html file using below syntax
#   1) Use this {{variable_name}} to display any python variable value
#   2) Use this {% to write any python code %}
#   3) Use this {% if condn%}  for any block like if, for etc
#               {% endif %}
# ----------------
# --------------------

# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@my_cloud_monitoring_app.route('/newuser')
def my_newuser_page():
    return flask.render_template('newuser.html')
# --------------------

# --------------------
# END POINT - 6 : http://127.0.0.1:5000/register URL MAPPED to '/register'
# --------------------
@my_cloud_monitoring_app.route('/register', methods=['POST'])
def my_register_page():

    # Get all data
    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')
    entered_username = entered_username.lower()
    # Check whether both the passwords are matching
    if entered_password_1 != entered_password_2:
        return "Both Passwords Are Not Matching. <br><br><a href='/login'>Go Back To Registration</a>"

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''CREATE TABLE IF NOT EXISTS users_table(
    NAME    VARCHAR(100),
    PASSWORD    VARCHAR(100),
    EMAIL   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------

    # verify whether user already exists in the database
    # How? select from table where username = entered_username
    # if we get records then we decide found
    # if we get 0 records the we can decide not found
    my_query = f"SELECT * FROM users_table WHERE name='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    if len(my_db_result) > 0:
        return "User Already Exists. <br><br><a href='/login'>Go Back To Registration</a>"

    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "User Created Successfully. <a href='/login'>Click Here To Login</a>"
# --------------------


# --------------------
# END POINT - 7 : http://127.0.0.1:5000/feedback URL MAPPED to '/feedback'
# --------------------
@my_cloud_monitoring_app.route('/feedback', methods=['POST'])
def my_feedback_page():

    # Get all data
    entered_username = flask.request.form.get('uname')
    entered_email = flask.request.form.get('email')
    entered_message = flask.request.form.get('mesg')



    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table ")
    my_query = '''CREATE TABLE IF NOT EXISTS feedback_table(
    NAME    VARCHAR(100),
    EMAIL   VARCHAR(100),
    MESSAGE VARCHAR(200)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------


    #  add new record to database and return account created successfully
    my_query = f"INSERT INTO FEEDBACK_TABLE VALUES('{entered_username}', '{entered_email}', '{entered_message}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "We Received your form. We will get back to you very soon, thank you <a href='/about'>Click Here To fill your qureirs</a>"
# -----------------

# --------------------
# END POINT - 8 : http://127.0.0.1:5000/new_instance URL MAPPED to '/new_instance'
# --------------------
@my_cloud_monitoring_app.route('/new_instance')
def my_new_instance_page():
    return flask.render_template('new_instance.html')

# --------------------

# END POINT - 9 : http://127.0.0.1:5000/newinstancedata URL MAPPED to '/feedback'
# --------------------
@my_cloud_monitoring_app.route('/newintancedata', methods=['POST'])
def my_newintancedata_page():

    # Get all data
    entered_instancename = flask.request.form.get('instname')
    entered_datacentercountry = flask.request.form.get('country')
    entered_datacenterloaction = flask.request.form.get('loc')
    entered_ip = flask.request.form.get('ip')
    entered_port = flask.request.form.get('port')
    entered_user = flask.request.form.get('user')
    entered_password = flask.request.form.get('passw')
    entered_servicetype = flask.request.form.get('servtype')
    entered_command = flask.request.form.get('cmnd')
    entered_expetedoutput = flask.request.form.get('expout')




    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table ")
    my_query = '''CREATE TABLE IF NOT EXISTS New_instance_table(
    INSTANCENAME VARCHAR(100),
    INSTANCEID INTEGER PRIMARY KEY AUTOINCREMENT,
    DATACENTERCOUNTRY   VARCHAR(100),
    DATACENTERLOCTION   VARCHAR(100),
    IP  VARCHAR(100),
    PORT    INTEGER,
    USER    VARCHAR(100),
    PASSWORD    VARCHAR(100),
    SERVICETYPE    VARCHAR(100),
    COMMAND     VARCHAR(100),
    EXPECTEDOUTPUT    VARCHAR(100),
    RECEIVEDOUTPUT VARCHAR(100),
    LOGPATH VARCHAR(100),
    SERVICESTATUS VARCHAR(100)
    
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------
    log_path = 'NA'

    #  add new record to database and return account created successfully
    my_query = f"INSERT INTO NEW_INSTANCE_TABLE(INSTANCENAME,DATACENTERCOUNTRY,DATACENTERLOCTION,IP,PORT,USER,PASSWORD,SERVICETYPE,COMMAND,EXPECTEDOUTPUT) VALUES('{entered_instancename}', '{entered_datacentercountry}', '{entered_datacenterloaction}','{entered_ip}', '{entered_port}', '{entered_user}', '{entered_password}','{entered_servicetype}', '{entered_command}', '{entered_expetedoutput}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "We Received your form.  <a href='/'>Click Here To fill your qureirs</a>"

# --------------------
@my_cloud_monitoring_app.route('/view_instance', methods=['GET'])
def my_view_instance_page():

    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect(r'users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute('SELECT * FROM NEW_INSTANCE_TABLE')
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")

    # All the data is in my_db_result
    return flask.render_template('view_instance.html', my_data=my_db_result)

# --------------------

# END POINT - 10 : http://127.0.0.1:5000/new_instance URL MAPPED to '/new_instance'
# --------------------
@my_cloud_monitoring_app.route('/logout')
def my_logout_page():
    session['username'] = None
    return flask.render_template('logout.html')
# --------------------
# Run the server
# --------------------
my_cloud_monitoring_app.run()
# --------------------
