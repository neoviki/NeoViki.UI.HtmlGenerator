import sys
sys.path.append('../../src')
from neoviki_html_generator import *

BEGIN("out.html", "demo")

obj = checkbox()
#obj.value = "input"
obj.width = 200
obj.height = 50
obj.gotoxy(120, 100)
#obj.disable()
#obj.enable()

END()

