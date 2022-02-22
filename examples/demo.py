import sys
sys.path.append('../src')
from NeoViki_HtmlGenerator import *

BEGIN("out.html", "demo")

obj = input()
obj.value = "Enter Your Input"
obj.width = 200
obj.height = 50
obj.gotoxy(100, 100)

obj = button()
obj.value = "Update Input"
obj.width = 200
obj.height = 50
obj.gotoxy(350, 100)

obj = input()
obj.password = True
obj.value = "Dummy Password"
obj.width = 200
obj.height = 50
obj.gotoxy(100, 200)

obj = button()
obj.value = "Update Password"
obj.width = 200
obj.height = 50
obj.gotoxy(350, 200)

obj = label()
obj.value = "CheckBox Label"
obj.width = 200
obj.height = 50
obj.gotoxy(100, 300)

obj = checkbox()
obj.width = 200
obj.height = 50
obj.gotoxy(350, 300)

obj = label()
obj.value = "Radio Label"
obj.width = 200
obj.height = 50
obj.gotoxy(100, 400)

obj = radio()
obj.value = "radio"
obj.width = 200
obj.height = 50
obj.gotoxy(350, 400)

END()

