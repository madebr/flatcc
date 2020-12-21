set(GEN_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
set(FBS_DIR "${PROJECT_SOURCE_DIR}/test/monster_test")

flatcc_generate_sources(
    NAME reflection_test
    SCHEMA_FILES "${FBS_DIR}/monster_test.fbs"
    BINARY_SCHEMA
    OUTPUT_DIR "${GEN_DIR}"
)

add_executable(reflection_test reflection_test.c)
target_link_libraries(reflection_test PRIVATE flatcc::runtime flatcc_generated::reflection_test)

flatcc_add_test(NAME reflection_test COMMAND $<TARGET_FILE:reflection_test>)
