#!python
import os

#--------
# Config files
#--------
IMGUI_PATH = 'imgui'
#--------
# folder dir and output folder or file
#--------

projectname = 'sfml_rpgen'				#holds the project name
#projectpackage = 'main'					#holds the project folder
SRC_PATH = 'src'
builddir = '.' + os.sep + SRC_PATH      #holds the build directory for this project

#-------
#---- SFML ----
SFML_LIBS = 'SFML-2.4.2\\lib'
#SFML_LIBS = 'C:\\sfml-build\\lib\\Release'
SFML_BIN = 'SFML-2.4.2\\bin\\'

#--include files
include_packages = []
include_packages.append(SRC_PATH)
include_packages.append('SFML-2.4.2\\include')
include_packages.append(SRC_PATH + os.sep + 'imgui')
#include_packages.append(SRC_PATH + os.sep + 'rpgen')


#--engine node packages
core_packages = []

#--lib
lib_packages = []
lib_packages.append('rpgen')
lib_packages.append('imgui')
lib_packages.append('opengl32')

lib_packages.append('sfml-window')
lib_packages.append('sfml-system')
lib_packages.append('sfml-audio')
lib_packages.append('sfml-graphics')
lib_packages.append('sfml-network')
#lib_packages.append('sfml-main')
#lib_packages.append('flac')
#lib_packages.append('freetype')
#lib_packages.append('jpeg')
#lib_packages.append('ogg')
#lib_packages.append('vorbisenc')
#lib_packages.append('vorbisfile')

dll_packages = []
#--release
dll_packages.append('sfml-audio-2')
dll_packages.append('sfml-graphics-2')
dll_packages.append('sfml-network-2')
dll_packages.append('sfml-system-2')
dll_packages.append('sfml-window-2')

#--add list
lib_packages += core_packages
include_packages +=core_packages

lib_files = []
#lib_files.append("SFML-2.4.2\\lib\\sfml-graphics-s.lib")
#lib_files.append(SFML_LIBS + "\\sfml-graphics.lib")
#lib_files.append(SFML_LIBS + "\\sfml-audio.lib")
#lib_files.append(SFML_LIBS + "\\sfml-network.lib")
#lib_files.append(SFML_LIBS + "\\sfml-system.lib")
#lib_files.append(SFML_LIBS + "\\sfml-window.lib")
