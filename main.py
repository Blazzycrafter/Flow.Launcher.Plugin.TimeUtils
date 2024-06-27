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


import clipboard
from flowlauncher import FlowLauncher


class times(FlowLauncher):

    def query(self, query):
        return [
            {
                #"Title": f"{if not query time.time()}{('Your query is: ' + query , query)[query == '']}",
                "Title": f"{'Your query is: ' + query if query else time.time()}",
                "SubTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "copy_to_clipboard",
                    "parameters": [f"{'Your query is: ' + query if query else time.time()}"]
                }
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]

    def copy_to_clipboard(self, text):
        clipboard.copy(text)

if __name__ == "__main__":
    times()
