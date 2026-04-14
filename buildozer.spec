[app]
title = KnovYourFrend

package.name = knovyourfrend
package.domain = org.example

source.dir = .
source.include_exts = py,pyc,png,jpg,jpeg,kv,mp3

version = 0.1

# IMPORTANT: keep minimal & stable
requirements = kivy,cython

orientation = portrait
fullscreen = 0

# 🔥 ANDROID STABLE LOCK (CRITICAL FIX)
android.api = 34
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a

# 🔥 FORCE BUILD-TOOLS VERSION (PREVENT 37 ISSUE)
android.build_tools_version = 34.0.0

# IMPORTANT: must be images, NOT mp4
presplash.filename = assets/angel.png
icon.filename = assets/demon.png

[buildozer]
log_level = 2
warn_on_root = 1
