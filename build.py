from pbxproj import XcodeProject
from pbxproj.pbxextensions.ProjectFiles import *
import sys
import os
from distutils.dir_util import copy_tree
from pathlib import Path
import plistlib

arg_must_project_headers = ""
arg_must_project_sources = ""
arg_opt_project_assets = ""
arg_opt_alternative_rde_path = ""
arg_rde_ios_path = str(Path(__file__).parent)
arg_opt_output_path = ""
arg_opt_build_type = "debug"
arg_opt_log_trace = " > /dev/null"
arg_opt_force_rebuild = False
arg_opt_app_name = "RDEiOS_App"
arg_opt_app_icon = "defaultAssets/logo.png"
arg_opt_app_version = "1.0.0.0"
arg_opt_app_orientations = "[portrait]"
arg_opt_install = False

def trace_to_string(trace):
    if " > /dev/null" in trace:
        return "error"
    elif " > /dev/null 2>&1" in trace:
        return "none"
    elif trace == "":
        return "full"

for arg in sys.argv:
    if "--trace" in arg:
        trace = arg.replace("--trace=", "")
        if trace == "none":
            arg_opt_log_trace = " > /dev/null 2>&1"
        elif trace == "error":
            arg_opt_log_trace = " > /dev/null"
        elif trace == "full":
            arg_opt_log_trace = ""
        else:
            print("ERROR: argument --trace must use an option between [none,full,error], the option will be ignored.")
    elif "--headers" in arg:
        arg_must_project_headers = arg.replace("--headers=", "")
    elif "--sources" in arg:
        arg_must_project_sources = arg.replace("--sources=", "")
    elif "--rde_path" in arg:
        arg_opt_alternative_rde_path = arg.replace("--rde_path=", "")
    elif "--build_type" in arg:
        arg_opt_build_type = arg.replace("--build_type=", "").lower()
    elif "--output_path" in arg:
        arg_opt_output_path = arg.replace("--output_path=", "")
    elif "--force_rebuild" in arg:
        arg_opt_force_rebuild = True
    elif "--assets" in arg:
        arg_opt_project_assets = arg.replace("--assets=", "")
    elif "--app_name" in arg:
        arg_opt_app_name = arg.replace("--app_name=", "")
    elif "--app_icon" in arg:
        arg_opt_app_icon = arg.replace("--app_icon=", "")
    elif "--app_version" in arg:
        arg_opt_app_version = arg.replace("--app_version=", "")
    elif "--app_orientations" in arg:
        arg_opt_app_orientations = arg.replace("--app_orientations=", "")
    elif "--install" in arg:
        arg_opt_install = True
    elif arg == "-h" or arg == "--help" or arg == "help":
        print("The script builds the project for iOS, the following parameters are a must to be provided:")
        print("     --headers=<path/to/your/headers>")
        print("     --sources=<path/to/your/sources>")
        print("")
        print("The script will assume that the project RDEiOS is in the same root level as RDE project, if not, these arguments must be provided:")
        print("     --rde_path=<path/to/RDE>")
        print("IT IS RECOMENDED, to have both together.")
        print("")
        print("Other optional parameters are:")
        print("     --build_type=<release,debug> If not specified, it will be debug.")
        print("     --output_path=<path/to/export/IPA> If not specified, it will be build/build_type.")
        print("     --assets=<path/to/your/assets> This sets the assets to be included in the build.")
        print("     --trace=<none, error or full> This sets the level of logs during building.")
        print("     --force_rebuild Will rebuild all of the dependencies.")
        print("     --app_name=<name of your app> Sets the name of the app (RDEiOS_App by default)")
        print("     --app_icon=<path/to/icon> Must be relative to the --assets path!")
        print("     --app_version=<1.0.0.0> Must be in the this format, 4 numbers separated by dots.")
        print("     --app_orientations=[<portrait,reverse_port,landscape,reverse_lands>] Any of the 4 versions (or combination) can be added.")
        print("     --install Installs the build on a connected device.")

if arg_must_project_headers == "":
    print("ERROR: parameter --headers must be provided, pointing to your .h,.hpp files.")
    exit(-1)

if arg_must_project_sources == "":
    print("ERROR: parameter --sources must be provided, pointing to your .c,.cpp files.")
    exit(-1)


def result_log(res, log, allow = False):
    if res == 0:
        print("")
        print("--------------------------------------")
        print(log)
        print("--------------------------------------")
        print("")
    else:
        if not allow:
            exit(-1)

if arg_opt_alternative_rde_path == "":
    arg_opt_alternative_rde_path = str(Path(__file__).parent.parent) + "/RDE"

if arg_opt_output_path == "":
    arg_opt_output_path = "build/" + arg_opt_build_type

print("")
print("----------------------------------------------------")
print("Compiling with options:")
print("     RDE_PATH:       ", arg_opt_alternative_rde_path)
print("     RDE_IOS_PATH:   ", arg_rde_ios_path)
print("     BUILD_TYPE:     ", arg_opt_build_type)
print("     TRACE:          ", trace_to_string(arg_opt_log_trace))
print("     ASSETS_PATH:    ", arg_opt_project_assets)
print("     FORCE_REBUILD:  ", arg_opt_force_rebuild)
print("     HEADERS:        ", arg_must_project_headers)
print("     SOURCES:        ", arg_must_project_sources)
print("     OUTPUT_PATH:    ", arg_opt_output_path)
print("----------------------------------------------------")
print("")


ProjectFiles._FILE_TYPES[u".ico"] = (u"*.ico", "PBXResourcesBuildPhase")
ProjectFiles._FILE_TYPES[u".glsl"] = (u"*.ico", "PBXResourcesBuildPhase")
ProjectFiles._FILE_TYPES[u".ttf"] = (u"*.ico", "PBXResourcesBuildPhase")

#Build basic libraries
if not os.path.exists(arg_rde_ios_path + "/modules/Chipmunk2D/xcode/build/" + arg_opt_build_type + "/libChipmunk-iOS.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project modules/Chipmunk2D/xcode/Chipmunk7.xcodeproj -sdk iphoneos -scheme 'Chipmunk-iOS' clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "Chipmunk was buildt correctly")
else:
    print("Chipmunk already built, skipping")

if not os.path.exists(arg_rde_ios_path + "/modules/SDL/Xcode/SDL/build/" + arg_opt_build_type + "/libSDL2.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project modules/SDL/Xcode/SDL/SDL.xcodeproj -sdk iphoneos -scheme 'StaticLibrary-iOS' clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "SDL2 was buildt correctly")
else:
    print("SDL2 already built, skipping")

if not os.path.exists(arg_rde_ios_path + "/modules/SDL_image/Xcode-iOS/build/" + arg_opt_build_type + "/libSDL2_image.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project modules/SDL_image/Xcode-iOS/SDL_image.xcodeproj -sdk iphoneos -scheme libSDL_image-iOS clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "SDL2_image was buildt correctly")
else:
    print("SDL2_image already built, skipping")

if not os.path.exists(arg_rde_ios_path + "/modules/SDL_mixer/Xcode-iOS/build/" + arg_opt_build_type + "/libSDL2_mixer.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project modules/SDL_mixer/Xcode-iOS/SDL_mixer.xcodeproj -sdk iphoneos -scheme libSDL_mixer-iOS clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "SDL2_mixer was buildt correctly")
else:
    print("SDL2_mixer already built, skipping")

if not os.path.exists(arg_rde_ios_path + "/iOSProjects/freetype/Xcode-iOS/Release-iphoneos/libfreetype.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project iOSProjects/freetype/Xcode-iOS/freetype.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "Freetype2 was buildt correctly")
else:
    print("Freetype2 already built, skipping")

if not os.path.exists(arg_rde_ios_path + "/iOSProjects/GLMLib/build/" + arg_opt_build_type + "/libGLMLib.a") or arg_opt_force_rebuild:
    result = os.system("xcodebuild -project iOSProjects/GLMLib/GLMLib.xcodeproj -sdk iphoneos -scheme GLMLib clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "GLM was buildt correctly")
else:
    print("GLM already built, skipping")






# Setup RDE project
if not os.path.exists(arg_rde_ios_path + "/iOSProjects/RDELib/build/" + arg_opt_build_type + "/libRDELib.a") or arg_opt_force_rebuild:
    result = os.system('rm -rf iOSProjects/RDELib/RDELib_.xcodeproj')
    result_log(result, "Made secure copy of RDELib", True)

    copy_tree("iOSProjects/RDELib/RDELib.xcodeproj", "iOSProjects/RDELib/RDELib_.xcodeproj")
    print("Made copy of RDELib")

    project = XcodeProject.load('iOSProjects/RDELib/RDELib_.xcodeproj/project.pbxproj')

    for dirpath, dirnames, filenames in os.walk(arg_opt_alternative_rde_path + "/engine"):
        for filename in [f for f in filenames if f.endswith(".cpp")]:
            cpp_path = os.path.join(dirpath, filename)
            if filename == "WindowsWindow.cpp" or filename == "LinuxWindow.cpp" or filename == "MacWindow.cpp" or filename == "AndroidWindow.cpp":
                continue
            print(filename)
            project.remove_files_by_path(cpp_path)
            project.add_file(cpp_path, force=False)

    include = "-I" + arg_opt_alternative_rde_path + "/engine/include " + "-I" + arg_opt_alternative_rde_path + "/nonVcpkgDeps/Chipmunk2D/include " + "-I" + arg_opt_alternative_rde_path + "/vcpkg/installed/x64-osx/include " + "-I" + arg_opt_alternative_rde_path + "/vcpkg/installed/x64-osx/include/SDL2 " + "-I" + arg_rde_ios_path + "/modules/SDL/include " + "-I" + arg_rde_ios_path + "/modules/SDL/src"
    print("Linked dirs: ", include)
    project.remove_other_cflags(include)
    project.add_other_cflags(include)

    project.save()

    print("Compiling RDELib... This will take a while")
    result = os.system("xcodebuild -project iOSProjects/RDELib/RDELib_.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=build/" + arg_opt_build_type + " -configuration " + arg_opt_build_type.capitalize() + " " + arg_opt_log_trace )
    result_log(result, "RDELib was buildt correctly")
else:
    print("RDELib already built, skipping")




# Setup RDEiOS project

copy_tree("RDEiOS.xcodeproj", "RDEiOS_.xcodeproj")
print("Made cpy of RDEiOS")

print("")
print("")
print("Starting to compile the project...")
project = XcodeProject.load('RDEiOS_.xcodeproj/project.pbxproj')

for dirpath, dirnames, filenames in os.walk(arg_must_project_sources):
    for filename in [f for f in filenames if f.endswith(".cpp")]:
        print("Adding: " + os.path.join(dirpath, filename))
        project.add_file(os.path.join(dirpath, filename), force=False)

print("")

include = "-I" + arg_must_project_headers + " -I" + arg_opt_alternative_rde_path + "/engine/include " + "-I" + arg_opt_alternative_rde_path + "/nonVcpkgDeps/Chipmunk2D/include " + "-I" + arg_opt_alternative_rde_path + "/vcpkg/installed/x64-osx/include " + "-I" + arg_opt_alternative_rde_path + "/vcpkg/installed/x64-osx/include/SDL2 " + "-I" + arg_rde_ios_path + "/modules/SDL/include " + "-I" + arg_rde_ios_path + "/modules/SDL/src"
print("Linked dirs: ", include)
project.add_other_cflags(include)

exclude_list = ["^.*\.tps$", "^.*\.pdf$"]

print("")

print("Added assets: " + arg_opt_project_assets)
project.add_file(arg_opt_project_assets)
print("Added default assets: " + arg_opt_alternative_rde_path + '/defaultAssets')
project.add_file(arg_opt_alternative_rde_path + '/defaultAssets')
project.remove_files_by_path("defaultAssets/shaders/core")

print("")

print("")
print("------------------- PLIST INFO ----------------------")
print("     CFBundleDisplayName:                ", arg_opt_app_name)
print("     CFBundleIconFile:                   ", arg_opt_app_icon)
print("     CFBundleShortVersionString:         ", arg_opt_app_version)
print("     UISupportedInterfaceOrientations:   ", arg_opt_app_orientations)
print("----------------------------------------------------")
print("")

pl = None
with open('Info.plist', 'rb') as fp:
    pl = plistlib.load(fp)
    pl["CFBundleDisplayName"] = arg_opt_app_name
    pl["CFBundleIconFile"] = arg_opt_app_icon
    pl["CFBundleShortVersionString"] = arg_opt_app_version
    orientations = []
    if "portrait" in arg_opt_app_orientations:
        orientations.append("UIInterfaceOrientationPortrait")
    if "reverse_port" in arg_opt_app_orientations:
        orientations.append("UIInterfaceOrientationPortraitUpsideDown")
    if "landscape" in arg_opt_app_orientations:
        orientations.append("UIInterfaceOrientationLandscapeLeft")
    if "reverse_lands" in arg_opt_app_orientations:
        orientations.append("UIInterfaceOrientationLandscapeRight")
    pl["UISupportedInterfaceOrientations"] = orientations

plist=open('Info.plist','wb')
plistlib.dump(pl, plist)
plist.close()


project.save()

print("Compiling... This may take a while")
result = os.system("xcodebuild -project RDEiOS_.xcodeproj -sdk iphoneos clean archive CONFIGURATION_BUILD_DIR=" + arg_opt_output_path + " -configuration " + arg_opt_build_type.capitalize() + " -destination generic/platform=iOS" + arg_opt_log_trace)
result_log(result, "Full project was buildt correctly")
result = os.system('rm -rf RDEiOS_.xcodeproj' + arg_opt_log_trace )
result = os.system('rm -rf iOSProjects/RDELib/RDELib_.xcodeproj' + arg_opt_log_trace )

if arg_opt_install:
    os.system("ideviceinstaller -i /private/tmp/RDEiOS_.dst/Applications/RDEiOS.app")