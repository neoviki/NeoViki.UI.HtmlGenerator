import sys
sys.path.append('../src')
from NeoViki_UI_HtmlGenerator import *

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

obj = video()
obj.value = "Demo Video"
obj.width = 320
obj.height = 200
obj.gotoxy(700, 100)

obj = paragraph()
obj.value = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet., comes from a line in section 1.10.32."
obj.font.bold = True;
obj.width = 200
obj.height = 50
obj.gotoxy(100, 600)


END()

