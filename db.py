import sqlite3

class EnglCourseDB:
	"""
	EnglCourseDB class for working with DB
	"""
	def __init__(self):
		self.conn = sqlite3.connect("db.db")	# connection with db file
		self.cursor = self.conn.cursor()		# cursor for execute queries
		self.courses = ["Upacademy", "Update", "StudyLink", "Interpress", "ILA", "Miss Akzharkyn", "Bolashaq", "StudyIN", "KursANT"] 	# courses(*tables) in DB

		for course in self.courses:
			self.cursor.execute(f"""
				CREATE TABLE IF NOT EXISTS '{course}' (
					ID					INTEGER PRIMARY KEY,
					fullname			TEXT,
					date_when_came		DATE,
					date_when_left		DATE,
					level_when_came		TEXT,
					level_when_left		TEXT,
					current_level		TEXT,
					on_studying			BOOLEAN
				)
			""")

	def find(self, fullname: str, course = None):
		"""
		the function finds data from the DB(*table)
		"""
		if course:
			self.cursor.execute(f"SELECT ID FROM '{course}' WHERE fullname = '{fullname}'")
			fetched_data = self.cursor.fetchone()

			if not fetched_data:
				return False
			else:
				return True


		data = []
		for course in self.courses:
			self.cursor.execute(f"SELECT * FROM '{course}' WHERE fullname = '{fullname}'")	# Select * (all/everything) from table of course in DB where full name is equal to value of 'fullname' parameter
			fetched_data = self.cursor.fetchone() 											# fetch selected data using self.cursor.fetchone() function and assign returned data to variable fetched_data
		
			if not fetched_data:
				continue
			else:
				data.append([course, fetched_data])

		if not data:
			return None
		else:
			return data

	def add(self, course: str, fullname: str):
		"""
		the function adds new data to the DB(*table)
		"""
		# Insert into table of course (fullname) values (fullname parameter)
		self.cursor.execute(f"INSERT INTO '{course}' (fullname) VALUES ('{fullname}')")
		
		# save changes using self.conn.commit() function
		self.conn.commit()

	def update(self, course: str, fullname: str, item: str, value):
		"""
		the function updates data in the DB(*table)
		"""
		self.cursor.execute(f"UPDATE '{course}' SET '{item}' = '{value}' WHERE fullname = '{fullname}'")	# Update data of people in table of course where fullname is equal to fullname parameter
		self.conn.commit()																				# save changes using self.conn.commit() function

	def delete(self, fullname: str):
		"""
		the function deletes data from the DB(*table)
		"""
		for course in self.courses:
			self.cursor.execute(f"DELETE FROM '{course}' WHERE fullname = ?", (fullname, )) 	# Delete all data from table of course where fullname is equal to fullname parameter
		self.conn.commit()																		# save changes using self.conn.commit() function
