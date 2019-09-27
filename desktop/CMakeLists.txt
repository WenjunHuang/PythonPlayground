cmake_minimum_required(VERSION 3.1)

project(desktop LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5 COMPONENTS Core Quick REQUIRED)

add_executable(${PROJECT_NAME} "./ui/main.qml"
    "./ui/styles/color_system.mjs"
    "./ui/styles/variables.mjs"
    "./ui/dialog/Dialog.qml"
    "./ui/dialog/DialogContent.qml"
    "./ui/dialog/DialogError.qml"
    "./ui/dialog/DialogFooter.qml"
    "./ui/dialog/DialogHeader.qml"
    "./ui/border/Border.qml"
    "./ui/octicons/Octicon.qml"
    )
target_compile_definitions(${PROJECT_NAME} PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(${PROJECT_NAME} PRIVATE Qt5::Core Qt5::Quick)

