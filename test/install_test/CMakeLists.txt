# This file tests the installation of flatbuffers. It is not meant to be used as a subfolder of test.

cmake_minimum_required(VERSION 3.3)
project(flatcc_install_test)

# Fake the base of the project to be the root of flatcc
set(CMAKE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../..")
set(PROJECT_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../..")

enable_testing()

add_subdirectory(test_find_all)
add_subdirectory(test_find_components)
