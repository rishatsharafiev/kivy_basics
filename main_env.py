# KIVY_TEXT=pil python main_env.py

import os

### Path control
# os.environ['KIVY_DATA_DIR'] = '<kivy path>/data'
# os.environ['KIVY_MODULES_DIR'] = '<kivy path>/modules'
# os.environ['KIVY_HOME'] = '<user home>/.kivy | <android app path>/.kivy | <user home>/Documents/.kivy'
# os.environ['KIVY_SDL2_PATH'] = '<sdl2_path>'

### Configuration
# os.environ['KIVY_USE_DEFAULTCONFIG'] = '1'
# os.environ['KIVY_NO_CONFIG'] = '1'
# os.environ['KIVY_NO_FILELOG'] = '1'
# os.environ['KIVY_NO_CONSOLELOG'] = '1'
# os.environ['KIVY_NO_ARGS'] = '1'

### Restrict core to specific implementation
# os.environ['KIVY_WINDOW'] = '<sdl2, pygame, x11, egl_rpi>'
# os.environ['KIVY_TEXT'] = '<sdl2, pil, pygame, sdlttf>'
# os.environ['KIVY_VIDEO'] = '<gstplayer, ffpyplayer, ffmpeg, null>'
# os.environ['KIVY_AUDIO'] = '<sdl2, gstplayer, ffpyplayer, pygame, avplayer>'
# os.environ['KIVY_IMAGE'] = '<sdl2, pil, pygame, imageio, tex, dds, gif>'
# os.environ['KIVY_CAMERA'] = '<avfoundation, android, opencv>'
# os.environ['KIVY_SPELLING'] = '<enchant, osxappkit>'
# os.environ['KIVY_CLIPBOARD'] = '<sdl2, pygame, dummy, android>'

### Metrics
# os.environ['KIVY_DPI'] = '1'
# os.environ['KIVY_METRICS_DENSITY'] = '1'
# os.environ['KIVY_METRICS_FONTSCALE'] = '1'

### Graphics
# os.environ['KIVY_GL_BACKEND'] = '<gl|glew|sdl2|angle_sdl2|mock>'
# os.environ['KIVY_GL_DEBUG'] = '1'
# os.environ['KIVY_GRAPHICS'] = '1'
# os.environ['KIVY_GLES_LIMITS'] = '1'
# os.environ['KIVY_BCM_DISPMANX_ID'] = '<0-6>'
# os.environ['KIVY_BCM_DISPMANX_LAYER'] = '0'

import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
