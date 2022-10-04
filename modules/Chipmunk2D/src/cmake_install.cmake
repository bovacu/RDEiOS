# Install script for directory: /Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/src/libchipmunk.7.0.3.dylib"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/src/libchipmunk.7.dylib"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.7.0.3.dylib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.7.dylib"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" -x "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/src/libchipmunk.dylib")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.dylib" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.dylib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/strip" -x "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.dylib")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/src/libchipmunk.a")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.a" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.a")
    execute_process(COMMAND "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ranlib" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libchipmunk.a")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/chipmunk" TYPE FILE FILES
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk_ffi.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk_private.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk_structs.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk_types.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/chipmunk_unsafe.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpArbiter.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpBB.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpBody.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpConstraint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpDampedRotarySpring.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpDampedSpring.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpGearJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpGrooveJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpHastySpace.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpMarch.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpPinJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpPivotJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpPolyShape.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpPolyline.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpRatchetJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpRobust.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpRotaryLimitJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpShape.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpSimpleMotor.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpSlideJoint.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpSpace.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpSpatialIndex.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpTransform.h"
    "/Users/borja.vazquez/GDE/nonVcpkgDeps/Chipmunk2D/include/chipmunk/cpVect.h"
    )
endif()

