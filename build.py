from pbxproj import XcodeProject
import sys
import os
from distutils.dir_util import copy_tree

cli_args = sys.argv

if len(cli_args) == 2 and cli_args[1] == "help" or cli_args[1] == "-help" or cli_args[1] == "--help" or cli_args[1] == "-h" or cli_args[1] == "--h":
    print("* First argument must be your project's header files directory")
    print("* Second must be your project project's source files directory")
    print("* Third your project's asset directory and fourth GDE's directory")
    print("* Fourth GDE's directory")
    print("* Fifth GDEiOS's directory")
    exit(0)

if len(cli_args) != 6:
    print("Wrong number of arguments, run python3 build.py --help")
    exit(0)

# Build basic libraries
os.system('xcodebuild -project modules/SDL/Xcode/SDL/SDL.xcodeproj -sdk iphoneos -scheme "StaticLibrary-iOS" clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')
os.system('xcodebuild -project modules/SDL_image/Xcode-iOS/SDL_image.xcodeproj -sdk iphoneos -scheme libSDL_image-iOS clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')
os.system('xcodebuild -project modules/SDL_mixer/Xcode-iOS/SDL_mixer.xcodeproj -sdk iphoneos -scheme libSDL_mixer-iOS clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')
os.system('xcodebuild -project iOSProjects/Box2DiOSLib/Box2DiOSLib.xcodeproj -sdk iphoneos -scheme Box2DiOSLib clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')
os.system('xcodebuild -project iOSProjects/freetype2iOSLib/freetype2.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')
os.system('xcodebuild -project iOSProjects/glmiOSLib/glmiOSLib.xcodeproj -sdk iphoneos -scheme glmiOSLib clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')

os.system('rm -rf iOSProjects/gdeiOSLib/gdeiOSLib_.xcodeproj')
copy_tree("iOSProjects/gdeiOSLib/gdeiOSLib.xcodeproj", "iOSProjects/gdeiOSLib/gdeiOSLib_.xcodeproj")

# Setup GDE project
project = XcodeProject.load('iOSProjects/gdeiOSLib/gdeiOSLib.xcodeproj/project.pbxproj')

for dirpath, dirnames, filenames in os.walk(cli_args[4] + "/engine"):
    for filename in [f for f in filenames if f.endswith(".cpp")]:
        cpp_path = os.path.join(dirpath, filename)
        print(filename)
        if filename == "WindowsWindow.cpp" or filename == "LinuxWindow.cpp" or filename == "MacWindow.cpp" or filename == "AndroidWindow.cpp":
            continue
        project.remove_files_by_path(cpp_path)
        project.add_file(cpp_path, force=False)

include = "-I" + cli_args[4] + "/engine/include"
project.remove_other_cflags(include)
project.add_other_cflags(include)

project.save()

# Building GDE library
os.system('xcodebuild -project iOSProjects/gdeiOSLib/gdeiOSLib.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=build -configuration Release')

os.system('rm -rf GDEiOS_.xcodeproj')
copy_tree("GDEiOS.xcodeproj", "GDEiOS_.xcodeproj")

# Setup GDEiOS project
project = XcodeProject.load('GDEiOS.xcodeproj/project.pbxproj')

for dirpath, dirnames, filenames in os.walk(cli_args[2]):
    for filename in [f for f in filenames if f.endswith(".cpp")]:
        print("Adding: " + os.path.join(dirpath, filename))
        project.add_file(os.path.join(dirpath, filename), force=False)

include = "-I" + cli_args[1]
project.add_other_cflags(include)
project.add_file(cli_args[5] + '/modules/SDL/Xcode/SDL/build/libSDL2.a')
project.add_file(cli_args[5] + '/modules/SDL_image/Xcode-iOS/build/libSDL2_image.a')
project.add_file(cli_args[5] + '/modules/SDL_mixer/Xcode-iOS/build/libSDL2_mixer.a')
project.add_file(cli_args[5] + '/iOSProjects/Box2DiOSLib/build/libBox2DiOSLib.a')
project.add_file(cli_args[5] + '/iOSProjects/gdeiOSLib/build/libgdeiOSLib.a')
project.add_file(cli_args[5] + '/iOSProjects/glmiOSLib/build/libglmiOSLib.a')
project.add_file(cli_args[5] + '/iOSProjects/freetype2iOSLib/build/libFreetype2.a')

project.add_file(cli_args[3])

project.save()

# Buildo applicatiom
os.system('xcodebuild -project GDEiOS.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=build -configuration Release -destination generic/platform=iOS')

os.system('rm -rf GDEiOS.xcodeproj')
os.system('mv GDEiOS_.xcodeproj GDEiOS.xcodeproj')

os.system('rm -rf iOSProjects/gdeiOSLib/gdeiOSLib.xcodeproj')
os.system('mv iOSProjects/gdeiOSLib/gdeiOSLib_.xcodeproj iOSProjects/gdeiOSLib/gdeiOSLib.xcodeproj')