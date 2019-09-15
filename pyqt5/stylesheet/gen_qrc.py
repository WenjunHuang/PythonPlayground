import os
import subprocess

with open('stylesheet.qrc', 'w') as w:
    w.write("<!DOCTYPE RCC>")
    w.write("<RCC version=\"1.0\">")
    w.write("<qresource prefix=\"/\">")

    for image in os.listdir('./images'):
        w.write(f"<file>images/{image}</file>")

    for style in os.listdir('./styles'):
        w.write(f"<file>styles/{style}</file>")

    w.write("</qresource>")
    w.write("</RCC>")

subprocess.call(['pyrcc5', '-o', 'stylesheet_rc.py', 'stylesheet.qrc'])
