# sfml_rpgen

License: CCO

Information: Simple compile tool build using window 10 visual studio community 2017 current default set. Using the python with scons command to run builds with visual studio code.

Compile default set to release build. Window 10 32bit. VS2017

To build this project you need to install python to path and scons package. If you on windows you need to install vs2017 since there are script in the bat or task build section in vscode.

Configs:(Window 10 Config Current build)
 * build_config.py
 * SConstruct (Scons build script compiler config)
 * .vscode
 * vsbuild_debug
 * vsbuild_release

Programs and Codes:
 * Visual Studio Code 
 * Viusal Studio Tool VS2017
 * Python 2.7.13
  * scons http://scons.org/
 * SFML 2.4.2 (Current in folder for testing purpose)
 * IMGUI 1.51 (Config setting for SMFL)

Credits:
 * https://github.com/eliasdaler/imgui-sfml

 Information: Help with the imgui setup build with SFML.

Notes:
 * lib warrnings first time build will show error. After that there is no errors when compile again.
 * Tends to get Dlls or Libs errors.