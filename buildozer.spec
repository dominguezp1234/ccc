[app]

# (str) Title of your application
title = APKCALCULADORA

# (str) Package name
package.name = apkcalculadora

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy.dell

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Incluye hostpython3 para librerías estándar como 'math' y 'random'
requirements = python3,kivy,hostpython3

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

#
# buildozer specific
#

[buildozer]

# (int) Log level (2 = debug with command output)
log_level = 2
