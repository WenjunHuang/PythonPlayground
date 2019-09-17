cmake_minimum_required(VERSION 3.1)

project(views LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5 COMPONENTS Core Quick REQUIRED)

add_executable(${PROJECT_NAME} "main.cpp" "main.qml" "LauncherList.qml" "SimpleLauncherDelegate.qml" "gridview/gridview-example.qml" "listview/dynamiclist.qml" "listview/content/StadiumButton.qml" "listview/content/PressAndHoldButton.qml" "listview/expandingdelegates.qml" "listview/content/SmallText.qml" "listview/content/TextButton.qml" "listview/content/RecipesModel.qml" "listview/highlight.qml" "listview/content/PetsModel.qml" "listview/highlightranges.qml" "listview/sections.qml" "listview/content/ToggleButton.qml" "package/view.qml"  "package/Delegate.qml")
target_compile_definitions(${PROJECT_NAME} PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(${PROJECT_NAME} PRIVATE Qt5::Core Qt5::Quick)

