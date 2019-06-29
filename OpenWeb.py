#-*- coding:UTF-8 -*-

import sys
import webbrowser


def openWeb(url):
    sys.path.append("libs")
    webbrowser.open(url)
    print(webbrowser.get())
