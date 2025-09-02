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

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CALL_PHONE

android.api = 30
android.minapi = 21
android.ndk = 21.4.7075529
android.sdk = 30
android.gradle_dependencies = 
android.add_java_dir = 

# Ensure proper SDK paths
android.sdk_path = %(buildozer_dir)s/android/platform/android-sdk
android.ndk_path = %(buildozer_dir)s/android/platform/android-sdk/ndk/21.4.7075529

# Python for Android settings for 2024.1.21
android.arch = arm64-v8a armeabi-v7a
android.allow_newer_python = True
android.allow_newer_sdk = True
android.allow_newer_ndk = True

# Build settings
android.private_storage = True

# Additional compatibility settings
android.enable_androidx = True
android.gradle_dependencies = androidx.core:core:1.6.0

orientation = portrait
fullscreen = 0