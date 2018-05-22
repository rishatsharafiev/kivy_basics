### KIVY_HOME
# <KIVY_HOME>/config.ini

### Dekstop
# <HOME_DIRECTORY>/.kivy/config.ini
# Windows: C:\Users\tito\.kivy\config.ini
# OS X: /Users/tito/.kivy/config.ini
# Linux: /home/tito/.kivy/config.ini

### Android
# <ANDROID_APP_PATH>/.kivy/config.ini
# /data/data/org.kivy.launcher/files/.kivy/config.ini

### iOS
# <HOME_DIRECTORY>/Documents/.kivy/config.ini

### Local configuration

# №1
from kivy.config import Config

Config.read(<file>)
# set config
Config.write()

# №2
import os
os.environ['KIVY_HOME'] = <folder>

# №3
set KIVY_HOME=<folder> # Windows:
export KIVY_HOME=<folder> # Linux & OSX:
