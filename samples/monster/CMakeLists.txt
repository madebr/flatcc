set(GEN_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
set(FBS_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

flatcc_generate_sources(monster_sample
    DEFINITION_FILES monster.fbs
    ALL
    OUTPUT_DIR "${GEN_DIR}"
)

add_executable(monster monster.c)
target_link_libraries(monster PRIVATE flatcc::runtime flatcc_generated::monster_sample)

if (FLATCC_TEST)
    add_test(NAME monster COMMAND monster)
endif()
