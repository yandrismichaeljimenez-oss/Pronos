[app]
title = Tu Pronosticos
package.name = tupronosticos
package.domain = com.yandris.tupronosticos
source.dir =.
source.include_exts = py
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET
