find_package(flatcc REQUIRED COMPONENTS cli)

if(NOT TARGET flatcc::cli)
    message(FATAL_ERROR "flatcc::cli target not available")
endif()

if(TARGET flatcc::runtime)
    message(FATAL_ERROR "flatcc::runtime should not be available with the cli component")
endif()

if(TARGET flatcc::compiler)
    message(FATAL_ERROR "flatcc::compiler should not be available with the cli component")
endif()

find_package(flatcc REQUIRED COMPONENTS runtime)

if(NOT TARGET flatcc::runtime)
    message(FATAL_ERROR "flatcc::runtime target not available")
endif()

if(NOT TARGET flatcc::compiler)
    message(FATAL_ERROR "flatcc::compiler target not available")
endif()

include(FlatccGenerateSources)

# re-use flatcc reflection_test

add_subdirectory("${PROJECT_SOURCE_DIR}/test/reflection_test" reflection_test)
