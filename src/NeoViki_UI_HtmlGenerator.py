'''
    HTML Generator Library ( NeoViki_UI Format )

    Author: Viki (a) Vignesh Natarajan
'''

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
        self.thickness = 0

def generate_callback(callback_name):
    global __func_callbacks
    __func_callbacks += "\n\nfunction " + callback_name + "(){\n\t alert(\"" + callback_name +  "\"); \n}"

def update_main(code):
    global __func_main_body
    __func_main_body += code

def get_button_id():
    global button_id
    button_id += 1
    return button_id

def get_label_id():
    global label_id
    label_id += 1
    return button_id

def get_input_id():
    global input_id
    input_id += 1
    return input_id

def get_paragraph_id():
    global paragraph_id
    paragraph_id += 1
    return paragraph_id

def get_text_id():
    global text_id
    text_id += 1
    return text_id

def get_image_id():
    global image_id
    image_id += 1
    return image_id

def get_audio_id():
    global audio_id
    audio_id += 1
    return audio_id

def get_video_id():
    global video_id
    video_id += 1
    return video_id

def get_radio_id():
    global radio_id
    radio_id += 1
    return radio_id

def get_checkbox_id():
    global checkbox_id
    checkbox_id += 1
    return checkbox_id

class UI_COMMON:
    def __init__(self):
        self.title  = "demo"
        self.color  = color()
        self.border = border()
        self.radius =  7;
        self.font   = font()
        self.width  = 200
        self.height = 200
        self.value = "Object"
        self.code = ""
        #"left", "right", "center", "justify"
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

    def generate(self):
        self.code +="\n\tobject.style.position = \"absolute\";"
        #self.code += "\n\tobject.id = " + "\"" + str(self.id) + "\"" + ";"
        self.code += "\n\tobject.name = " + "\"" + str(self.name) + "\"" + ";"
        self.code +="\n\tobject.style.background = \""  + self.color.bg + "\";"
        self.code +="\n\tobject.style.color = \""       + self.color.fg + "\";"
        self.code +="\n\tobject.style.width ="          + "\"" + str(self.width)    + "px" + "\";"
        self.code +="\n\tobject.style.height ="         + "\"" + str(self.height)   + "px" + "\";"
        self.code +="\n\tobject.style.fontSize ="       + "\"" + str(self.font.size)   + "px" + "\";"

        if self.radius !=0 :
            self.code +="\n\tobject.style.borderRadius ="       + "\"" + str(self.radius)   + "px" + "\";"

        if self.border.thickness != 0:
            self.code +="\n\tobject.style.borderWidth = \""  + str(self.border.thickness) + "px" + "\";"
            self.code +="\n\tobject.style.borderColor = \""  + self.border.color + "\";"
            self.code +="\n\tobject.style.borderStyle = \""  + "solid" + "\";"

        if self.font.bold == True:
            self.code +="\n\tobject.style.fontWeight = \""  + "bold" + "\";"

        if self.font.italic == True:
            self.code +="\n\tobject.style.fontStyle = \""  + "italic" + "\";"

        if self.font.name != "":
            self.code +="\n\tobject.style.fontFamily = \""  + self.font.name + "\";"

        #self.code +="\n\tobject.style.justifyContent =" + "\"" + self.align  + "\";"
        self.code +="\n\tobject.style.textAlign      =" + "\"" + self.align  + "\";"
        self.code +="\n\tobject.style.verticalAlign  =" + "\"" + "middle"  + "\";"

class image(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_image_id()
        self.name = "Image_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('IMG');"
        self.src = "test.png"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()

        self.code +="\n\tobject.src =" + "\"" + str(self.src) + "\";"
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)


class paragraph(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_paragraph_id()
        self.name = "Paragraph_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('P');"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.innerHTML =  " + "\"" + self.value + "\"" + ";"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)

class text(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_text_id()
        self.name = "Text_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('DIV');"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.innerHTML =  " + "\"" + self.value + "\"" + ";"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)

class audio(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_audio_id()
        self.name = "Audio_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('AUDIO');"
        self.autoplay = False
        self.src = "test.mp3"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()

        self.code +="\n\tobject.src =" + "\"" + str(self.src) + "\";"

        if self.autoplay == True:
            self.code +="\n\tobject.autoplay =" + "true" + ";"
        else:
            self.code +="\n\tobject.setAttribute(\"controls\", \"controls\");"

        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)


class video(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_video_id()
        self.name = "Video_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('VIDEO');"
        self.autoplay = False
        self.src = "test.ogg"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()

        self.code +="\n\tobject.src =" + "\"" + str(self.src) + "\";"

        if self.autoplay == True:
            self.code +="\n\tobject.autoplay =" + "true" + ";"
        else:
            self.code +="\n\tobject.setAttribute(\"controls\", \"controls\");"

        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)

class input(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_input_id()
        self.name = "Input_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('INPUT');"
        self.password = False

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"

        if self.password == False:
            self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"text\");"
        else:
            self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"password\");"

        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)


class checkbox(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_checkbox_id()
        self.name = "Checkbox_" + str(self.id)
        self.value = self.name
        self.width = 15
        self.height = 15
        self.code = "\n\tobject = document.createElement('INPUT');"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"checkbox\");"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(	object);"
        update_main(self.code)

class radio(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_radio_id()
        self.width = 15
        self.height =15
        self.name = "Radio_" + str(self.id)
        self.value = self.name
        self.code = "\n\tobject = document.createElement('INPUT');"

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.setAttribute("  + "\"" + "type" + "\"," + "\"radio\");"
        self.code +="\n\tobject.setAttribute("  + "\"" + "value" + "\"," + "\"" + self.value + "\");"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)

class label(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_label_id()
        self.name = "Label_" + str(self.id)
        self.value = self.name
        #self.code = "\n\tobject = document.createElement('LABEL');"
        #Using disabled button as label, as label text is not aligning to the middle
        self.code = "\n\tobject = document.createElement('BUTTON');"
        self.color.bg = 'black'
        self.color.fg = 'white'

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top ="  + "\"" + str(self.y) + "px" + "\";"
        self.code +="\n\tobject.disabled ="  + "\"" + "true" + "\";"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)


class button(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = get_button_id()
        self.name = "Button_" + str(self.id)
        self.value = self.name
        self.callback_name = "callback_Button_" + str(self.id)
        self.code = "\n\tobject = document.createElement('BUTTON');"
        self.color.bg = 'black'
        self.color.fg = 'white'

    def set_callback(self):
        self.code +="\n\tobject.onclick = " + self.callback_name + ";"
        generate_callback(self.callback_name)

    def gotoxy(self, x, y):
        self.x = x
        self.y = y
        self.generate()
        self.set_callback()
        self.code +="\n\tobject.appendChild(document.createTextNode(" + "\"" + str(self.value) + "\"" + "));"
        self.code +="\n\tobject.style.left =" + "\"" + str(self.x) + "px" + "\";"
        self.code +="\n\tobject.style.top =" + "\""  + str(self.y) + "px" + "\";"
        self.code +="\n\tpage.appendChild(object);"
        update_main(self.code)

class PAGE(UI_COMMON):
    def __init__(self):
        UI_COMMON.__init__(self)
        self.id = 0
        self.name = "Page_" + str(self.id)
        self.value = self.name
        self.title = ""
        self.head = ""
        self.tail = ""
        self.body = ""
        self.bg_image = ""
        self.generate()

    def generate(self):

        tag1 = "\n\tbackground: " + self.color.bg + ";"
        tag2 = ""
        if self.bg_image != "":
            tag2 = "\n\tbackground-image: url(" + "\'" + self.bg_image + "\'" + ");"

        self.style = "\n<style>\n\tbody \n{" + tag1 + tag2 + "\n}\n</style>"
        new_title = "\n<title>"+self.title+"</title>\n</head><body>\n\t<div id=\"container\">\n\t</div>\n\n<script>"

        self.head = "<!DOCTYPE html>\n\n<!-- Machine Generated Code ( NeoViki_HtmlGenerator ) -->\n\n<html>\n<head>" + self.style + new_title
        self.tail = "\n\n</script>\n\n</body>\n</html>"



def BEGIN(page_name):
    global __func_callbacks
    global button_id
    global text_id
    global radio_id
    global checkbox_id
    global scrollbar_id
    global label_id
    global input_id
    global video_id
    global audio_id
    global image_id
    global paragraph_id
    global __file_name
    global __func_main_body
    global __func_main_tail
    global __func_main_head
    global __func_main_tail
    global page

    __func_callbacks = ""
    __file_name = page_name
    button_id = 0
    text_id = 0
    paragraph_id = 0
    radio_id =  0
    checkbox_id = 0
    scrollbar_id = 0
    label_id = 0
    input_id = 0
    video_id = 0
    audio_id = 0
    image_id = 0
    paragraph_id = 0
    __func_main_body = ""
    __func_main_tail = ""

    __func_main_head="\n\nfunction MAIN() {"
    __func_main_body = "\n\tpage = document.getElementById(\"container\");"
    __func_main_tail="\n}\n\nMAIN();"


    page = PAGE()
    return page

def END():
    global page
    global __file_name, __func_callbacks, __func_main_head, __func_main_body, __func_main_tail

    page.body =__func_callbacks + __func_main_head + __func_main_body + __func_main_tail
    page.generate()
    html_data=page.head +  page.body  + page.tail
    f = open(__file_name, "w")
    f.write(html_data)
    f.close()


