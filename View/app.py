import Controller.appio as appio
import Controller.tokenize as tokenize

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QRadioButton, QMessageBox
from PyQt5.QtGui import QFont

class Window(QWidget):
	ARIAL_TITLE = QFont("Arial", 24)
	ARIAL_BUTTON = QFont("Arial", 12, 1)
	keywordType = 1

	def __init__(self):
		super().__init__()
		self.title = "CSGO Lexical Analysis"
		self.left = 720
		self.top = 300
		self.width = 500
		self.height = 300
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.layout = QVBoxLayout()

		self.label = QLabel("CSGO Lexical Analysis")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setFont(self.ARIAL_TITLE)

		self.choose_file_button = QPushButton("Choose CSGO file")
		self.choose_file_button.setFont(self.ARIAL_BUTTON)
		self.choose_file_button.clicked.connect(self.click_handler)

		self.radio_button1 = QRadioButton("Keyword Type 1")
		self.radio_button1.setChecked(True)
		self.radio_button1.toggled.connect(lambda:self.btnstate(self.radio_button1))
		
		self.radio_button2 = QRadioButton("Keyword Type 2")
		self.radio_button2.setChecked(False)
		self.radio_button2.toggled.connect(lambda:self.btnstate(self.radio_button2))

		self.layout.addWidget(self.label)
		self.layout.addWidget(self.radio_button1)
		self.layout.addWidget(self.radio_button2)
		self.layout.addWidget(self.choose_file_button)

		self.setLayout(self.layout)
		self.show()

	def click_handler(self):
		self.path, _ = QFileDialog.getOpenFileName(None, "Choose CSGO file", "", "CSGO Files (*.csgo);;All Files (*)")
		if self.path:
			self.process()

	def process(self):
		filecontent = appio.read(self.path)
		allTokenTypes = []
		for line in filecontent:
			if tokenize.isComment(line):
				continue
			tokens = tokenize.tokenize(line)
			tokenTypes = tokenize.type_classify(tokens, self.keywordType)
			allTokenTypes += tokenTypes
		output = appio.formatOutput(allTokenTypes)
		self.popup_message(output)

	def popup_message(self, msg):
		msg_box = QMessageBox()
		msg_box.setWindowTitle("Output")
		msg_box.setText(msg)
		msg_box.exec_()

	def btnstate(self, b):
		if b.text() == "Keyword Type 1":
			if b.isChecked() == True:
				self.keywordType = 1
		if b.text() == "Keyword Type 2":
			if b.isChecked() == True:
				self.keywordType = 2