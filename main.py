
import sys
import ui1
import ui2
from db import EnglCourseDB
from PySide2.QtWidgets import QWidget, QApplication, QMessageBox
from PySide2.QtCore import QCoreApplication

""" """
class EnglCourseDBApp:


	def __init__(self):


		self.db = EnglCourseDB()

		self.app = QApplication(sys.argv)

		self.ui1 = ui1.Ui_Form()
		self.Form1 = QWidget()
		self.ui1.setupUi(self.Form1)

		self.ui2 = ui2.Ui_Form()
		self.Form2 = QWidget()
		self.ui2.setupUi(self.Form2)

		self.current_found_person = "fullname"
		self.add_or_change_person_info = {
			"fullname": None,
			"course": None,
			"date": None,
			"date_when_": "",
			"lvl": None,
			"lvl_when_": "",
			"current_lvl": "",
			"on_studying": False,
		}

		self.ui1.add_or_change_btn.clicked.connect(self.open_second_window)
		self.ui1.search_btn.clicked.connect(self.find)
		self.ui1.delete_btn.clicked.connect(self.delete)

		self.ui2.date_came_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["date_when_"] = "came"', {'self':self}))
		self.ui2.date_left_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["date_when_"] = "left"', {'self':self}))
		
		self.ui2.lvl_came_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["lvl_when_"] = "came"', {'self':self}))
		self.ui2.lvl_left_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["lvl_when_"] = "left"', {'self':self}))
		
		self.ui2.on_studying_true_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["on_studying"] = True', {'self':self}))
		self.ui2.on_studying_false_btn.clicked.connect(lambda: exec('self.add_or_change_person_info["on_studying"] = False', {'self':self}))
		
		self.ui2.add_or_change_btn.clicked.connect(self.add_or_change)	
		




	def run(self):
		self.Form1.show()
		sys.exit(self.app.exec_())





	def find(self):
		information = self.db.find(self.ui1.search_line_edit.text())
		result = ""
		if not information:
			QMessageBox.about(QWidget(), "Error", "There is no such person in the database")
		else:
			for info in information:
				course = info[0]
				width = int((56-len(course))/2)
				course = course.rjust(width, "-")
				course += "-"*width
				arr = []
				[arr.append(info[1][i+2]) for i in range(len(info[1])-2)]
				result += f"{course}\nDate:\n\tcame:{arr[0]}\n\tleft:{arr[1]}\nLevel:\n\tcame:{arr[2]}\n\tleft:{arr[3]}\n\tcurrent:{arr[4]}\n\nOn studying: {arr[5]}\n\n"

		self.ui1.info_text_edit.setText(result)




	def open_second_window(self):
		self.Form2.show()





	def delete(self):
		self.db.delete(self.ui1.search_line_edit.text())
		self.ui1.info_text_edit.setText("")
		self.ui1.search_line_edit.setText("")





	def add_or_change(self):

		self.Form2.close()
		self.ui1.info_text_edit.setText("")
		self.ui1.search_line_edit.setText("")
		try: 
			available_in_db = self.db.find(self.ui2.fullname_line_edit.text(), self.ui2.course_line_edit.text())
			if not available_in_db:
				self.db.add(self.ui2.course_line_edit.text(), self.ui2.fullname_line_edit.text())
		except: 
			QMessageBox.about(QWidget(), "Error", "There is no such course in the database")
		else: 
			columns_with_data = [
				['level_when_' + self.add_or_change_person_info['lvl_when_'], self.ui2.lvl_line_edit.text()],
				['current_level', self.ui2.current_lvl_line_edit.text()],
				['on_studying', self.add_or_change_person_info['on_studying']],
				['date_when_' + self.add_or_change_person_info['date_when_'], self.ui2.date_line_edit.text()],
				["fullname", self.ui2.fullname_line_edit.text()]
			]

			for column in columns_with_data:
					self.db.update(self.ui2.course_line_edit.text(), self.ui2.fullname_line_edit.text(), column[0], column[1])
		finally:
			for i in self.add_or_change_person_info.keys():
				self.add_or_change_person_info[i] = None

			self.ui2.fullname_line_edit.setText("")
			self.ui2.course_line_edit.setText("")
			self.ui2.date_line_edit.setText("")
			self.ui2.lvl_line_edit.setText("")
			self.ui2.current_lvl_line_edit.setText("")

App = EnglCourseDBApp() 
App.run() 

