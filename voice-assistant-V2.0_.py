import os

import eel # type: ignore

eel.init('engine\www')

os.system('start msedge.exe --app="http://localhost:800/index.html"')

eel.start('index.html',  host='localhost' , block=True)