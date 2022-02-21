
callback_id = 0

class font:
    def __init__(self):
        self.size = 10
        self.name = 'consolas'
        self.bold = False
        self.italic = False

class color:
    def __init__(self):
        self.fg = 'black'
        self.bg = 'white'

class border:
    def __init__(self):
        self.color = 'black'
        self.thickness = 10

def g_update_callback():
    global callback_id
    global __func_callbacks
    callback_id = callback_id + 1
    __func_callbacks += "function callback_" + str(callback_id) + "(){ alert(\"callback_" + str(callback_id) + "\"); }"

def g_update_main(code):
    global __func_main_body
    __func_main_body += code

class UI_COMMON:
    def __init__(self):
        self.title  = "demo"
        self.color  = color()
        self.border = border()
        self.font   = font()
        self.width  = 200
        self.height = 200
        self.value = "Button"
        self.code = ""

    def dimension(self, width, height):
        self.width = width
        self.height = height

    def disable(self):
        return

    def enable(self):
        return

    def write(self, val):
        return

    def read(self):
        return

    def gotoxy(self, x, y):
        return

class button(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        g_update_callback()
        self.code = "object = document.createElement('BUTTON');"

    def __generate_common(self):
        global callback_id
        self.code +="object.appendChild(document.createTextNode("
        self.code +="\"" + str(self.value) + "\""
        self.code +="));"
        self.code +="object.style.position = \"absolute\";"
        self.code +="object.style.background = \"" + self.color.bg + "\";"
        self.code +="object.style.color = \"" + self.color.fg + "\";"
        __callback__ = "callback_" + str(callback_id)
        self.code +="object.onclick = " + __callback__ + ";"

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.__generate_common()
        self.code +="object.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="object.style.top =" + "\"" + str(self.y) + "px" + "\";"
        self.code +="page.appendChild(object);"
        g_update_main(self.code)

def BEGIN(page_name, page_title):
    global __func_callbacks
    global callback_id
    global __button_id
    global __text_id
    global __paragraph_id
    global __radio_id
    global __checkbox_id
    global __scrollbar_id
    global __label_id
    global __html_head
    global __html_body
    global __html_tail
    global __file_name
    global __func_main_body
    global __func_main_tail
    global __func_main_head
    global __func_main_body
    global __func_main_tail
    global __html_head
    global __html_tail

    __func_callbacks = ""
    __file_name = page_name
    callback_id = 0
    __button_id = 0
    __text_id = 0
    __paragraph_id = 0
    __radio_id =  0
    __checkbox_id = 0
    __scrollbar_id = 0
    __label_id = 0
    __html_head = ""
    __html_body = ""
    __html_tail = ""
    __func_main_body = ""
    __func_main_tail = ""

    __func_main_head="function MAIN() {"
    __func_main_body = "page = document.getElementById(\"container\");"
    __func_main_tail="}MAIN();"

    __html_head="<!DOCTYPE html><html><title>"+page_title+"</title><body><div id=\"container\"></div><script>"
    __html_tail="</script></body></html>"


def END():
    global __html_head, __html_body, __html_tail
    global __file_name, __func_callbacks, __func_main_head, __func_main_body, __func_main_tail

    __html_body=__func_callbacks + __func_main_head + __func_main_body + __func_main_tail

    html_data=__html_head +  __html_body  + __html_tail
    f = open(__file_name, "w")
    f.write(html_data)
    f.close()

page_name = "out1.html"
BEGIN(page_name, "demo")
b = button()
b.gotoxy(10,10)
END()
