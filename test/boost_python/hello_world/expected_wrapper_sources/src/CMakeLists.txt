cmake_minimum_required(VERSION 2.8)
if(NOT CMAKE_BUILD_TYPE)
    SET(CMAKE_BUILD_TYPE "Release")
endif()

find_package(Boost COMPONENTS python)
if(NOT Boost_FOUND)
    message(FATAL_ERROR "Unable to find correct Boost version. Did you set BOOST_ROOT?")
endif()
set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)
include_directories("${Boost_INCLUDE_DIRS}")

include_directories("/usr/include/python2.6")

add_library(hello_ext SHARED hello_ext.prap.cpp)
target_link_libraries(hello_ext ${Boost_LIBRARIES})
