find_package(flatcc REQUIRED)

if(NOT TARGET flatcc::cli)
    message(FATAL_ERROR "flatcc::cli target not available")
endif()

if(NOT TARGET flatcc::runtime)
    message(FATAL_ERROR "flatcc::runtime target not available")
endif()

if(NOT TARGET flatcc::compiler)
    message(FATAL_ERROR "flatcc::compiler target not available")
endif()

include(FlatccGenerateSources)

# re-use flatcc monster_test

add_subdirectory("${PROJECT_SOURCE_DIR}/test/monster_test" monster_test)
