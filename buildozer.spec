[app]
title = Ambulance Booking System
package.name = ambulancebooking
package.domain = org.ambulance

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,requests

# Comment out icon and presplash for now since files don't exist
# icon.filename = %(source.dir)s/ambulance_icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
# Handle ncurses issues in CI environment
android.allow_newer_ndk = True
android.allow_newer_sdk = True

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CALL_PHONE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.accept_sdk_license = True
android.gradle_dependencies = 
android.add_java_dir = 

orientation = portrait
fullscreen = 0