#Capsil Ganzo
import kivy
#kivy.require('1.8.0')

from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty,StringProperty
from kivy.lang import Builder

Builder.load_file('login.kv')

class Loginview (Widget):
	def validate(self, username, password):
		if username == password:
			print username, password
			self.clear_widgets()
		else:
			self.status.text = "Login failed"
class afterLogin (widget):
	def dumb(self):
		b = Boxlayout(cols = "2")
		b.add_widget(btn)
		print "flag"
class mainClass(App):
	def build(self):
		return Loginview()

if __name__ == '__main__':
	mainClass().run()

