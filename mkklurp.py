#!/usr/bin/env python3

import sys
import os
import sh
import subprocess

homedir = os.getenv("HOME")

# realpath = os.path.realpath(path)
# klurpdir=os.path.dirname(os.path.abspath(__file__))
klurpdir = os.path.dirname(os.path.realpath(__file__))
basepath = os.getcwd()
projectname = "demoproject"
appname = "demoapp"

venvname = sys.argv[1] if len(sys.argv) > 1 else "demovenv"

if len(sys.argv) > 2:
    projectname = sys.argv[2]

if len(sys.argv) > 3:
    appname = sys.argv[3]

venvpath = os.path.join(basepath, venvname)

print(venvname, projectname, appname)

subprocess.run(["python3", "-m", "venv", venvname])

staticdir = os.path.join(venvpath, "static")
mediadir = os.path.join(venvpath, "media")
enginedir = os.path.join(venvpath, "engine")
rundir = os.path.join(venvpath, "run")
# templatesdir = os.path.join(projectpath, "run")

os.mkdir(staticdir)
os.mkdir(mediadir)
os.mkdir(enginedir)
os.mkdir(rundir)

os.chdir(venvpath)
sh.sh('-c', '. bin/activate; pip3 install django; pip3 install gunicorn')
projectstring = f'django-admin startproject {projectname}'

sh.sh('-c', projectstring)
interfacename = "interface"
enginename = "engine"
projectname = "demoproject"
appname = "demoapp"
templatesname = "templates"

os.rename(projectname, interfacename)
projectpath = os.path.join(venvpath, interfacename)
projectfilespath = os.path.join(projectpath, projectname)
demoapppath = os.path.join(projectpath, appname)

templatespath = os.path.join(projectpath, templatesname)
os.mkdir(templatespath)
# app2path = os.path.join(venvpath, app2name)
# app3path = os.path.join(venvpath, app3name)
# app4path = os.path.join(venvpath, app4name)

enginepath = os.path.join(venvpath, enginename)

os.chdir(projectpath)
appstring = f'python3 manage.py startapp {appname}'
sh.sh('-c', appstring)

# os.chdir("/home/handyc/klurp")
# os.chdir(correct_klurp_directory_set_at_install")
# klurp = "klurp"
# klurppath = os.path.join(homedir, klurp)
os.chdir(klurpdir)
copystring1 = f'cp -r samplefiles/demoapp/*.py {demoapppath}'
# copystring2 = 'cp -r samplefiles/project/*.py ' + projectpath
copystring2 = f'cp -r samplefiles/project/*.py {projectfilespath}'
copystring3 = f'cp -r samplefiles/engine/* {enginepath}'
copystring4 = f'cp -r samplefiles/templates/* {templatespath}'
# copystring5 = 'cp -r samplefiles/users/* ' + userpath

sh.sh('-c', copystring1)
sh.sh('-c', copystring2)
sh.sh('-c', copystring3)
sh.sh('-c', copystring4)
# sh.sh('-c', copystring5)
print(copystring1)
print(copystring2)
print(copystring3)
print(copystring4)
# print(copystring5)


#

# copy the template files

# cp samplefiles/project/*.py projectpath
# cp samplefiles/engine/* enginepath
# cp samplefiles/engine/* enginepath

# subprocess.run(["ls", "-l"])
# exit with message
# print ('thanks for using klurp')
# print ('exited at: 00 00 00 on 00 00 00 0000 at location 00,00,00')
# coords

# cp ~/scripts/samplefiles/project/*.py $projectpath
# cp ~/scripts/samplefiles/engine/* $enginepath
# cp -r ~/scripts/samplefiles/engine/* $enginepath
