import psycopg2

db_name = "farmerspg"
db_user = ""
db_password = ""
db_host = "localhost"
db_port = "5432"

# Connect to database.
try:
	conn = psycopg2.connect(database = db_name, user = db = db_user, password = db_password, 
		host = db_host, port = db_port)
	print("Database connected.")

except:
	print("Error. Could not connect to database.")
