
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
    __func_callbacks += "\n\nfunction callback_" + str(callback_id) + "(){\n\t alert(\"callback_" + str(callback_id) + "\"); \n}"

def g_update_main(code):
    global __func_main_body
    __func_main_body += code

def get_button_name():
    global button_id
    button_id += 1
    return ("Button_" + str(button_id))

def get_label_name():
    global label_id
    label_id += 1
    return ("Label_" + str(button_id))

def get_input_name():
    global input_id
    input_id += 1
    return ("Input_" + str(input_id))

def get_radio_name():
    global radio_id
    radio_id += 1
    return ("Radio_" + str(radio_id))


def get_checkbox_name():
    global checkbox_id
    checkbox_id += 1
    return ("CheckBox_" + str(checkbox_id))


class UI_COMMON:
    def __init__(self):
        self.title  = "demo"
        self.color  = color()
        self.border = border()
        self.font   = font()
        self.width  = 200
        self.height = 200
        self.value = "Object"
        self.code = ""
        #"left", "right", "center"
        self.align = "center"

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

    def generate_common(self):
        global callback_id
        self.code +="\n\tobject.style.position = \"absolute\";"
        self.code +="\n\tobject.style.background = \""  + self.color.bg + "\";"
        self.code +="\n\tobject.style.color = \""       + self.color.fg + "\";"
        self.code +="\n\tobject.style.width ="          + "\"" + str(self.width)    + "px" + "\";"
        self.code +="\n\tobject.style.height ="         + "\"" + str(self.height)   + "px" + "\";"
        self.code +="\n\tobject.style.fontSize ="       + "\"" + str(self.font.size)   + "px" + "\";"
        self.code +="\n\tobject.style.justifyContent =" + "\"" + self.align  + "\";"
        self.code +="\n\tobject.style.textAlign      =" + "\"" + self.align  + "\";"
        self.code +="\n\tobject.style.verticalAlign  =" + "\"" + "middle"  + "\";"

class input(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.code = "\n\tobject = document.createElement('INPUT');"
        self.value = get_input_name()
        self.password = False

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.generate_common()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"

        if self.password == False:
            self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"text\");"
        else:
            self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"password\");"

        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        g_update_main(self.code)


class checkbox(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.code = "\n\tobject = document.createElement('INPUT');"
        self.value = get_checkbox_name()

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.generate_common()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"checkbox\");"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(	object);"
        g_update_main(self.code)

class radio(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.code = "\n\tobject = document.createElement('INPUT');"
        self.value = get_checkbox_name()

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.generate_common()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"radio\");"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        g_update_main(self.code)

class label(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.code = "\n\tobject = document.createElement('LABEL');"
        self.value = get_label_name()
        self.color.bg = 'black'
        self.color.fg = 'white'

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.generate_common()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tpage.appendChild(object);"
        g_update_main(self.code)


class button(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        g_update_callback()
        self.code = "\n\tobject = document.createElement('BUTTON');"
        self.value = get_button_name()
        self.color.bg = 'black'
        self.color.fg = 'white'

    def set_callback(self):
        __callback__ = "callback_" + str(callback_id)
        self.code +="\n\tobject.onclick = " + __callback__ + ";"

    def gotoxy(self, x, y):
        global __func_main_body
        self.x = x
        self.y = y
        self.generate_common()
        self.set_callback()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top =" + "\""  + str(self.y) + "px" + "\";"
        self.code +="\n\tpage.appendChild(object);"
        g_update_main(self.code)

def BEGIN(page_name, page_title):
    global __func_callbacks
    global callback_id
    global button_id
    global text_id
    global paragraph_id
    global radio_id
    global checkbox_id
    global scrollbar_id
    global label_id
    global input_id
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
    button_id = 0
    text_id = 0
    paragraph_id = 0
    radio_id =  0
    checkbox_id = 0
    scrollbar_id = 0
    label_id = 0
    input_id = 0
    __html_head = ""
    __html_body = ""
    __html_tail = ""
    __func_main_body = ""
    __func_main_tail = ""

    __func_main_head="\n\nfunction MAIN() {"
    __func_main_body = "\n\tpage = document.getElementById(\"container\");"
    __func_main_tail="\n}\n\nMAIN();"

    __html_head="<!DOCTYPE html>\n\n<!-- Machine Generated Code ( NeoViki_HtmlGenerator ) -->\n\n<html>\n<title>"+page_title+"</title>\n<body>\n\t<div id=\"container\">\n\t</div>\n\n<script>"
    __html_tail="\n\n</script>\n\n</body>\n</html>"


def END():
    global __html_head, __html_body, __html_tail
    global __file_name, __func_callbacks, __func_main_head, __func_main_body, __func_main_tail

    __html_body=__func_callbacks + __func_main_head + __func_main_body + __func_main_tail

    html_data=__html_head +  __html_body  + __html_tail
    f = open(__file_name, "w")
    f.write(html_data)
    f.close()


