# Create TABLES
def create_tables():

# Queries for the tables that will be created
	create_table_product = """
		CREATE TABLE product (
			id INT NOT NULL,
			name TEXT NOT NULL,
			description VARCHAR NULL,
			category_id INT NOT NULL,
			CONSTRAINT product_pk PRIMARY KEY(id),
			CONSTRAINT product_category_fk FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE
		)
		"""

	create_table_category = """
		CREATE TABLE category (
			id INT NOT NULL,
			name TEXT NOT NULL,
			description VARCHAR NULL,
			product_id INT NOT NULL,
			CONSTRAINT category_pk PRIMARY KEY (id)
		)
		"""

	# Create the tables
	cur = conn.cursor()
	cur.execute(create_table_product)
	cur.execute(create_table_category)

	# Commit changes
	# Close connection to database
	conn.commit()
	print("Tables created.")
	conn.close()