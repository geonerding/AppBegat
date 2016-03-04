# launch.py
'''
App Begat
This ttk based program will configure a web project and create a
directory with many basic libraries and styles pre-loaded into
the project based on the configurations made in the GUI.

If you want to configure the Google Maps API into your project,
make sure you add your API key in the string below.

Casey Sledge
Sept 2014
'''
from Tkinter import *
import ttk
from tkFileDialog import *
import tkMessageBox
import tkSimpleDialog
import os, shutil, sys, webbrowser

# Enter your Google Maps API Key here
googleAPIkey = "API_KEY"
root = Tk()
ico = os.path.realpath(__file__)
ico = ico.replace("launch.pyw", "icon.ico")
root.iconbitmap(default=ico)
root.wm_title("App Begat")

# CDN References--------------------------------------
libraries={
'angular' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.23/angular.min.js"></script>\n'},
'dojo' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/dojo/1.10.0/dojo/dojo.js"></script>\n', 'style' : '<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/dojo/1.8/dijit/themes/claro/claro.css"/>\n'}, # claro Theme
'ExtCore' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/ext-core/3.1.0/ext-core.js"></script>\n'},
'jQuery' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>\n'},
'jQueryMobile' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/jquerymobile/1.4.3/jquery.mobile.min.js"></script>\n', 'style' : '<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jquerymobile/1.4.3/jquery.mobile.min.css" />\n'},
'jQueryUI' : {'script' : '<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.1/jquery-ui.min.js"></script>\n', 'style' : '<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.1/themes/smoothness/jquery-ui.css" />\n'},
'MooTools' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/mootools/1.5.0/mootools-yui-compressed.js"></script>\n'},
'Prototype' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/prototype/1.7.2.0/prototype.js"></script>\n'},
'three' : {'script':'<script src="//ajax.googleapis.com/ajax/libs/threejs/r67/three.min.js"></script>\n'},
'ESRIdojo' : {'script' : '<script src="http://js.arcgis.com/3.10/"></script>\n', 'style' : '<link rel="stylesheet" href="http://js.arcgis.com/3.10/js/dojo/dijit/themes/claro/claro.css">\n<link rel="stylesheet" href="http://js.arcgis.com/3.10/js/esri/css/esri.css" />\n'}, # claro Theme
'd3' : {'script':'<script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.min.js"></script>\n'},
'googlemaps' : {'script':'<script src="https://maps.googleapis.com/maps/api/js?key=API_KEY"></script>\n'},
'kinetic' : {'script':'<script src="//cdnjs.cloudflare.com/ajax/libs/kineticjs/5.0.6/kinetic.min.js"></script>\n'},
'backbone' : {'script':'<script src="//cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min.js"></script>\n'},
'underscore' : {'script':'<script src="//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min.js"></script>\n'},
'bootstrap' : {'script':'<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>\n', 'style' : '<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" />\n'}
}

angular = StringVar()
dojo = StringVar()
ExtCore = StringVar()
jQuery = StringVar()
jQueryMobile = StringVar()
jQueryUI = StringVar()
MooTools = StringVar()
Prototype = StringVar()
three = StringVar()
ESRIdojo = StringVar()
d3 = StringVar()
googlemaps = StringVar()
kinetic = StringVar()
backbone = StringVar()
underscore = StringVar()
bootstrap = StringVar()

imgDir = IntVar()
CSSreset = IntVar()
colorsP = IntVar()
solarP = IntVar()
jsVal = IntVar()
cssVal = IntVar()

checklist = [angular,dojo,ExtCore,jQuery,jQueryMobile,jQueryUI,MooTools,Prototype,three,ESRIdojo,d3,googlemaps,kinetic,backbone,underscore,bootstrap]
for check in checklist:
    check = check.set("None")

# Functions-------------------------------------------

def browse():
    dirName = askdirectory()
    dirNameField.delete(1.0, END)
    dirNameField.insert(END, dirName)
    
def readMe(event):
    reader = os.path.realpath(__file__)
    reader = reader.replace("launch.pyw", "README.txt")
    print "working"
    webbrowser.open(reader)
    
def execute():
    try:
        # Variables
        theDir = dirNameField.get(1.0, END)
        theDir = theDir.replace("\n", "")
        proName = fileNameField.get(1.0, END)
        proName = proName.replace("\n", "")
        project = theDir + "\\" + proName
    
        
        # Create project directory and create web files/directories
        os.makedirs(project)
        htmlPage = open(project + "\\index.html", "w")

        preHTML = '<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>' + proName + '</title>\n<!--Style Libraries-->\n'
        midHTML = '<!--JS Libraries-->\n'
        postHTML = '</head>\n<body>\nYour project has been created.  Happy coding.\n</body>\n</html>'
        
        styleList = ""
        scriptList = ""
        
        for index in checklist:
            index = index.get()
            if index == "None":
                pass
            else:
                try:
                    styleList = styleList + libraries[index]['style']
                    scriptList = scriptList + libraries[index]['script']
                except:
                    scriptList = scriptList + libraries[index]['script']
        
        if imgDir.get() == 1:
            os.makedirs(project + "\\images")
            copyDir = os.path.realpath(__file__) + "\\Myimages\\"
            copyDir = copyDir.replace("\\launch.pyw", "")
            
            for file in (os.listdir(copyDir)):
                shutil.copy(copyDir + file, project + "\\images")
                
        if cssVal.get() == 1:
            customcss = ""
            os.makedirs(project + "\\CSS")
            copyDir = os.path.realpath(__file__) + "\\myCSS\\"
            copyDir = copyDir.replace("\\launch.pyw", "")
            cssPage = open(project + "\\CSS\\style.css", "w")
            
            for file in (os.listdir(copyDir)):
                shutil.copy(copyDir + file, project + "\\CSS")
                customcss = customcss + '<link href="./css/' + file + '" rel="stylesheet" />\n'
            
            styleList = styleList + customcss
            styleList = styleList + '<link href="./css/style.css" rel="stylesheet" />\n'
        else:
            cssPage = open(project + "\\style.css", "w")
            styleList = styleList + '<link href="style.css" rel="stylesheet" />\n'
            
        if jsVal.get() == 1:
            customjs = ""
            os.makedirs(project + "\\JS")
            copyDir = os.path.realpath(__file__) + "\\myJS\\"
            copyDir = copyDir.replace("\\launch.pyw", "")
            jsPage = open(project + "\\JS\\core.js", "w")
            
            for file in (os.listdir(copyDir)):
                shutil.copy(copyDir + file, project + "\\JS")
                customjs = customjs + '<script type="text/javascript" src="./js/' + file + '"></script>\n'
                
            scriptList = scriptList + customjs
            scriptList = scriptList + '<script type="text/javascript" src="./js/core.js"></script>\n'
        else:
            jsPage = open(project + "\\core.js", "w")
            scriptList = scriptList + '<script type="text/javascript" src="core.js"></script>\n'
            
        if CSSreset.get() == 1:
            cssPage.write("/* Eric Meyer's Reset CSS v2.0 - http://cssreset.com */\nhtml,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video{border:0;font-size:100%;font:inherit;vertical-align:baseline;margin:0;padding:0}article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section{display:block}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:before,blockquote:after,q:before,q:after{content:none}table{border-collapse:collapse;border-spacing:0}\n\n")
        
        if colorsP.get() == 1:
            cssPage.write('''/* Colors Palette
            navy 		: #001F3F;
            blue		: #0074D9;
            aqua		: #7FDBFF;
            teal		: #39CCCC;
            olive		: #3D9970;
            green		: #2ECC40;
            lime		: #01FF70;
            yellow		: #FFDC00;
            orange		: #FF851B;
            red			: #FF4136;
            fuchsia		: #F012BE;
            purple		: #B10DC9;
            maroon		: #85144B;
            white		: #fff;
            silver		: #ddd;
            gray		: #aaa;
            black		: #111;
            */\n\n''')
            
        if solarP.get() == 1:
            cssPage.write('''/* Solarized Palette - http://ethanschoonover.com/solarized ---------
            lightgray      : #819090;
            gray           : #708284;
            mediumgray     : #536870;
            darkgray       : #475B62;
            darkblue       : #0A2933;
            darkerblue     : #042029;
            paleryellow    : #FCF4DC;
            paleyellow     : #EAE3CB;
            yellow         : #A57706;
            orange         : #BD3613;
            red            : #D11C24;
            pink           : #C61C6F;
            purple         : #595AB7;
            blue           : #2176C7;
            cyan           : #259286;
            green          : #738A05; 
            */\n\n''')

        htmlPage.write(preHTML + styleList + midHTML + scriptList + postHTML)
    
        htmlPage.close()
        cssPage.close()
        jsPage.close()
        tkMessageBox.showinfo("Project Complete", "Directory and files successfully created.")

    except Exception, e:
        tkMessageBox.showinfo("Error", str(e))

# GUI Frames------------------------------------------
frame = Frame(root)
frame.pack(side=BOTTOM)

nameFrame = Frame(frame)
nameFrame.pack(side=BOTTOM)

pathFrame = Frame(nameFrame)
pathFrame.pack(side=BOTTOM)

sep1 = Frame(pathFrame)
sep1.pack(side=BOTTOM)

jsFrame = Frame(sep1)
jsFrame.pack(side=BOTTOM)

jsFrame2 = Frame(jsFrame)
jsFrame2.pack(side=BOTTOM)

sep2 = Frame(jsFrame2)
sep2.pack(side=BOTTOM)

comboFrame = Frame(sep2)
comboFrame.pack(side=BOTTOM)

sep3 = Frame(comboFrame)
sep3.pack(side=BOTTOM)

opFrame = Frame(sep3)
opFrame.pack(side=BOTTOM)

sep4 = Frame(opFrame)
sep4.pack(side=BOTTOM)

finFrame = Frame(sep4)
finFrame.pack(side=BOTTOM)

buttonFrame = Frame(finFrame)
buttonFrame.pack(side=BOTTOM)

# GUI Widgets-----------------------------------------
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", font=("Constantia", "26"))
'''
l1 = ttk.Label(frame, text="App Begat", style="BW.TLabel")
l1.pack(side='top', padx=10)
'''
fileNameField = Text(nameFrame, width=25, height=1, bd=3)
fileLabel = ttk.Label(nameFrame, text="Project name", font=("Arial Black", "10"))
fileLabel.pack(pady=3)
fileNameField.insert(INSERT, "")
fileNameField.pack(pady=2, padx=5)

dirNameField = Text(pathFrame, width=50, height=1, bd=3)
dirLabel = ttk.Label(pathFrame, text="Project path", font=("Arial Black", "10"))
dirLabel.pack(pady=3)
dirNameField.insert(INSERT, "")
dirNameField.pack(side=LEFT, pady=2, padx=5)

dirbtn = ttk.Button(pathFrame, text="Browse", command=browse)
dirbtn.pack(side='right', padx=6)

hr1 = Label(sep1, text="JavaScript Libraries", font=("Arial Black", "10"))
hr1.pack(pady=10, side=BOTTOM)

angChk = Checkbutton(jsFrame, text="Angular", onvalue="angular", offvalue="", variable=angular)
angChk.pack(side=LEFT)

backboneChk = Checkbutton(jsFrame, text="Backbone", onvalue="backbone", offvalue="None", variable=backbone)
backboneChk.pack(side=LEFT)

d3Chk = Checkbutton(jsFrame, text="D3", onvalue="d3", offvalue="None", variable=d3)
d3Chk.pack(side=LEFT)

ExtChk = Checkbutton(jsFrame, text="ExtCore", onvalue="ExtCore", offvalue="None", variable=ExtCore)
ExtChk.pack(side=LEFT)

googleChk = Checkbutton(jsFrame, text="Google Maps", onvalue="googlemaps", offvalue="None", variable=googlemaps)
googleChk.pack(side=LEFT)

jqueryChk = Checkbutton(jsFrame, text="jQuery", onvalue="jQuery", offvalue="None", variable=jQuery)
jqueryChk.pack(side=LEFT)

kinChk = Checkbutton(jsFrame2, text="Kinetic", onvalue="kinetic", offvalue="None", variable=kinetic)
kinChk.pack(side=LEFT)

mooChk = Checkbutton(jsFrame2, text="MooTools", onvalue="MooTools", offvalue="None", variable=MooTools)
mooChk.pack(side=LEFT)

proChk = Checkbutton(jsFrame2, text="Prototype", onvalue="Prototype", offvalue="None", variable=Prototype)
proChk.pack(side=LEFT)

threeChk = Checkbutton(jsFrame2, text="Three", onvalue="three", offvalue="None", variable=three)
threeChk.pack(side=LEFT)

unChk = Checkbutton(jsFrame2, text="Underscore", onvalue="underscore", offvalue="None", variable=underscore)
unChk.pack(side=LEFT)

hr2 = Label(sep2, text="JavaScript/CSS Libraries", font=("Arial Black", "10"))
hr2.pack(pady=10, side=BOTTOM)

bootstrapChk = Checkbutton(comboFrame, text="Bootstrap", onvalue="bootstrap", offvalue="None", variable=bootstrap)
bootstrapChk.pack(side=LEFT)

dojoChk = Checkbutton(comboFrame, text="Dojo", onvalue="dojo", offvalue="None", variable=dojo)
dojoChk.pack(side=LEFT)

ESRIChk = Checkbutton(comboFrame, text="ESRI Dojo", onvalue="ESRIdojo", offvalue="None", variable=ESRIdojo)
ESRIChk.pack(side=LEFT)

jquiChk = Checkbutton(comboFrame, text="jQuery UI", onvalue="jQueryUI", offvalue="None", variable=jQueryUI)
jquiChk.pack(side=LEFT)

jqmChk = Checkbutton(comboFrame, text="jQuery Mobile", onvalue="jQueryMobile", offvalue="None", variable=jQueryMobile)
jqmChk.pack(side=LEFT)

hr3 = Label(sep3, text="CSS Options", font=("Arial Black", "10"))
hr3.pack(pady=10, side=BOTTOM)

resetChk = Checkbutton(opFrame, text="CSS Reset", variable=CSSreset)
resetChk.pack(side=LEFT)

colorsChk = Checkbutton(opFrame, text="Colors Palette", variable=colorsP)
colorsChk.pack(side=LEFT)

solarChk = Checkbutton(opFrame, text="Solarized Palette", variable=solarP)
solarChk.pack(side=LEFT)

hr4 = Label(sep4, text="_________________________________________________________")
hr4.pack(pady=10, side=BOTTOM)

imgChk = Checkbutton(finFrame, text="Copy myImages", variable=imgDir)
imgChk.pack(side=LEFT,pady=3)

jsChk = Checkbutton(finFrame, text="Copy myJS", variable=jsVal)
jsChk.pack(side=LEFT,pady=3)

cssChk = Checkbutton(finFrame, text="Copy myCSS", variable=cssVal)
cssChk.pack(side=LEFT,pady=3)

textLink = Label(finFrame, text="View README", fg="Blue", cursor="hand2")
textLink.pack(side=LEFT,pady=3)
textLink.bind("<Button-1>", readMe)

createbtn = ttk.Button(buttonFrame, text="Create Project", command=execute)
createbtn.pack(padx=20, side=RIGHT, pady=3)

# Fire------------------------------------------------

root.mainloop()