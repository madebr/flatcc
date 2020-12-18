# This file tests the installation of flatbuffers. It is not meant to be used as a subfolder of test.

cmake_minimum_required(VERSION 3.3)
project(flatcc_install_test)

# Fake the base of the project to be the root of flatcc
set(CMAKE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../..")
set(PROJECT_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../..")

enable_testing()

add_subdirectory(test_find_all)
add_subdirectory(test_find_components)


#find_package(flatcc REQUIRED)
#
#if(NOT TARGET flatcc::cli)
#    message(FATAL_ERROR "flatcc::cli target not available")
#endif()
#
#if(NOT TARGET flatcc::runtime)
#    message(FATAL_ERROR "flatcc::runtime target not available")
#endif()
#
#if(NOT TARGET flatcc::compiler)
#    message(FATAL_ERROR "flatcc::compiler target not available")
#endif()
#
#message(STATUS "${CMAKE_MODULE_PATH}")
#
#include(FlatccGenerateSources)
#
#enable_testing()
#
## re-use the monster test + test
#
#set(GEN_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
#set(FBS_DIR "../monster_test")
#
#flatcc_generate_sources(
#    NAME monster_test
#    DEFINITION_FILES "${FBS_DIR}/monster_test.fbs"
#    ALL
#    OUTPUT_DIR "${GEN_DIR}"
#)
#
#add_executable(monster_test ../monster_test/monster_test.c)
#target_link_libraries(monster_test PRIVATE flatcc::runtime flatcc_generated::monster_test)
#
#add_test(NAME monster_test COMMAND monster_test)