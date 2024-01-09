[app]


# (str) Title of your application
title = A_Calk

# (str) Package name
package.name = acalk

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.include_exts = py,png,jpg,kv,atlas

# Path to the directory containing your main.py
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (list) Garden requirements
#garden_requirements = 

# (str) Custom source folders for requirements
# source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (int) Application versioning (method 2)
# version.code = 1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY
# kivy.adapters, kivy.atlas, kivy.audio, kivy.cache, kivy.config, kivy.deps, kivy.factory, kivy.gesture, kivy.graphics, kivy.lang, kivy.lib, kivy.logger, kivy.network, kivy.parsers, kivy.support, kivy.tools, kivy.uix, kivy.utils, kivy.vector, kivy.input, kivy.context, kivy.effect, kivy.storage, kivy.core, kivy.animation, kivy.atlas, kivy.audio, kivy.cache, kivy.config, kivy.deps, kivy.factory, kivy.gesture, kivy.graphics, kivy.lang, kivy.lib, kivy.logger, kivy.network, kivy.parsers, kivy.support, kivy.tools, kivy.uix, kivy.utils, kivy.vector, kivy.input, kivy.context, kivy.effect, kivy.storage, kivy.core, kivy.animation, kivy.atlas, kivy.audio, kivy.cache, kivy.config, kivy.deps, kivy.factory, kivy.gesture, kivy.graphics, kivy.lang, kivy.lib, kivy.logger, kivy.network, kivy.parsers, kivy.support, kivy.tools, kivy.uix, kivy.utils, kivy.vector, kivy.input, kivy.context, kivy.effect, kivy.storage, kivy.core, kivy.animation, kivy.atlas, kivy.audio, kivy.cache, kivy.config, kivy.deps, kivy.factory, kivy.gesture, kivy.graphics, kivy.lang, kivy.lib, kivy.logger, kivy.network, kivy.parsers, kivy.support, kivy.tools, kivy.uix, kivy.utils, kivy.vector, kivy.input, kivy.context, kivy.effect, kivy.storage, kivy.core, kivy.animation, kivy.atlas, kivy.audio, kivy.cache, kivy.config, kivy.deps, kivy.factory, kivy.gesture, kivy.graphics, kivy.lang, kivy.lib, kivy.logger, kivy.network, kivy.parsers, kivy.support, kivy.tools, kivy.uix, kivy.utils, kivy.vector, kivy.input, kivy.context, kivy.effect, kivy.storage, kivy.core, kivy.animation

# (str) Application log level (debug, info, warning, error, critical)
log_level = 2

# (str) Android logcat filters to use
# logcat_filters = *:S python:D

# (bool) Avoid doing a check before uploading to the playstore
#publish.skip_check = True

# (bool) Use --private data storage (True) or --dir public storage (False)
#public_storage = False

# (str) Override default android toolchain to compile with the latest NDK
#toolchain = 

# (bool) Try to compile in one big apk
#compact = False

# (list) List of source patterns to exclude
#source.exclude_exts = pyc,pyo,__pycache__,zip,trash

# (list) List of inclusions using pattern matching
#source.include_exts = py,png,jpg,kv,atlas