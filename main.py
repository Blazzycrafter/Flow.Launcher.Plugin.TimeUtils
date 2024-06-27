# -*- coding: utf-8 -*-

import sys,os,time
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))


import pyperclip as clipboard
from flowlauncher import FlowLauncher


class times(FlowLauncher):

    def query(self, query):
        return self.q(query)

    # def context_menu(self, data):
    #    return [
    #        {
    #        }
    #    ]

    def q(self, query):
        templateUNUSED = {
            "Title": "",
            "SubTitle": "",
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {
                "method": "",
                "parameters": []
            }
        }
        # empty: show time
        if query == "":
            t= time.localtime()
            return [
                {
                    "Title": f"current time: {t.tm_hour}:{t.tm_min}:{t.tm_sec}",
                    "SubTitle": "Press Enter to copy to clipboard",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "copy_to_clipboard",
                        "parameters": [f"{t.tm_hour}:{t.tm_min}:{t.tm_sec}"]
                    }
                }
            ]
    def copy_to_clipboard(self, text):
        clipboard.copy(text)

if __name__ == "__main__":
    times().query("test")
