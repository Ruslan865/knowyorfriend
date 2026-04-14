[app]
title = KnovYourFrend

package.name = knovyourfrend
package.domain = org.example

source.dir = .
source.include_exts = py,pyc,png,jpg,jpeg,kv,mp3

version = 0.1

# Only real python dependencies (IMPORTANT FIX)
requirements = kivy,cython

orientation = portrait
fullscreen = 0

# 🔥 ANDROID STABLE CONFIG (FIXES YOUR ERROR)
android.api = 34
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a

# ❌ WRONG IN YOUR VERSION FIXED HERE
# MUST BE PNG, NOT MP4
presplash.filename = assets/angel.png
icon.filename = assets/demon.png

# Optional optimizations
android.allow_backup = True
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
