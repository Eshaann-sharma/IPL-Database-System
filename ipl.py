from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database connection details
DB_HOST = 'database-1.cbkqiu4ymfx5.us-east-1.rds.amazonaws.com'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = '12345678'
DB_DATABASE = 'ipl'

# Connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        return conn
    except Exception as e:
        print("Unable to connect to the database:", e)
        return None

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for teams page
@app.route('/teams', methods=['GET', 'POST'])
def teams():
    conn = connect_to_database()
    if conn:
        cur = conn.cursor()
        if request.method == 'POST':
            # If a search query is submitted
            search_query = request.form.get('search')
            search_column = request.form.get('column')
            if search_query and search_column:
                cur.execute(f"SELECT * FROM Teams WHERE {search_column} LIKE %s", ('%' + search_query + '%',))
            else:
                cur.execute("SELECT * FROM Teams")
        else:
            cur.execute("SELECT * FROM Teams")
        teams_data = cur.fetchall()
        conn.close()
        return render_template('teams.html', teams=teams_data)
    else:
        return "Unable to fetch data from database"


# Route for Players page
@app.route('/players', methods=['GET', 'POST'])
def players():
    conn = connect_to_database()
    if conn:
        cur = conn.cursor()
        if request.method == 'POST':
            # If a search query is submitted
            search_query = request.form.get('search')
            search_column = request.form.get('column')
            if search_query and search_column:
                cur.execute(f"SELECT * FROM Players WHERE {search_column} LIKE %s", ('%' + search_query + '%',))
            else:
                cur.execute("SELECT * FROM Players")
        else:
            cur.execute("SELECT * FROM Players")
        players_data = cur.fetchall()
        conn.close()
        return render_template('players.html', players=players_data)
    else:
        return "Unable to fetch data from database"

# Route for matches page
@app.route('/matches', methods=['GET', 'POST'])
def matches():
    conn = connect_to_database()
    if conn:
        cur = conn.cursor()
        if request.method == 'POST':
            # If a search query is submitted
            search_query = request.form.get('search')
            search_column = request.form.get('column')
            if search_query and search_column:
                cur.execute(f"SELECT * FROM Matches WHERE {search_column} LIKE %s", ('%' + search_query + '%',))
            else:
                cur.execute("SELECT * FROM Matches")
        else:
            cur.execute("SELECT * FROM Matches")
        matches_data = cur.fetchall()
        conn.close()
        return render_template('matches.html', matches=matches_data)
    else:
        return "Unable to fetch data from database"


# Route for Stadium page
@app.route('/Stadium', methods=['GET', 'POST'])
def stadiums():
    conn = connect_to_database()
    if conn:
        cur = conn.cursor()
        if request.method == 'POST':
            # If a search query is submitted
            search_query = request.form.get('search')
            search_column = request.form.get('column')
            if search_query and search_column:
                cur.execute(f"SELECT * FROM Stadium WHERE {search_column} LIKE %s", ('%' + search_query + '%',))
            else:
                cur.execute("SELECT * FROM Stadium")
        else:
            cur.execute("SELECT * FROM Stadium")
        stadiums_data = cur.fetchall()
        conn.close()
        return render_template('Stadium.html', stadiums=stadiums_data)
    else:
        return "Unable to fetch data from database"


# Route for TeamDetails page
@app.route('/teamdetails', methods=['GET', 'POST'])
def team_details():
    conn = connect_to_database()
    if conn:
        cur = conn.cursor()
        if request.method == 'POST':
            # If a search query is submitted
            search_query = request.form.get('search')
            search_column = request.form.get('column')
            if search_query and search_column:
                cur.execute(f"SELECT * FROM TeamDetails WHERE {search_column} LIKE %s", ('%' + search_query + '%',))
            else:
                cur.execute("SELECT * FROM TeamDetails")
        else:
            cur.execute("SELECT * FROM TeamDetails")
        team_details_data = cur.fetchall()
        conn.close()
        return render_template('teamdetails.html', team_details=team_details_data)
    else:
        return "Unable to fetch data from database"



if __name__ == '__main__':
    app.run(debug=True)
