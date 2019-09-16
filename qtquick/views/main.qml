import QtQuick 2.13
import QtQuick.Window 2.13

Window {
    visible: true
    width: 320
    height: 480
    title: qsTr("Hello World")
    LauncherList {
        id: ll
        anchors.fill: parent
        Component.onCompleted: {
            addExample("GridView", "A simple GridView", Qt.resolvedUrl("gridview/gridview-example.qml"))
            addExample("Dynamic List", "A dynamically alterable list", Qt.resolvedUrl("listview/dynamiclist.qml"))
            addExample("Expanding Delegates", "A ListView with delegates that expand", Qt.resolvedUrl("listview/expandingdelegates.qml"))
            addExample("Highlight", "A ListView with a custom highlight", Qt.resolvedUrl("listview/highlight.qml"))
            addExample("Highlight Ranges", "The three highlight ranges of ListView", Qt.resolvedUrl("listview/highlightranges.qml"))
            addExample("Sections", "ListView section headers and footers", Qt.resolvedUrl("listview/sections.qml"))
            addExample("Packages", "Transitions between a ListView and GridView", Qt.resolvedUrl("package/view.qml"))
            addExample("PathView", "A simple PathView", Qt.resolvedUrl("pathview/pathview-example.qml"))
            addExample("ObjectModel", "Using a ObjectModel", Qt.resolvedUrl("objectmodel/objectmodel.qml"))
            addExample("Display Margins", "A ListView with display margins", Qt.resolvedUrl("listview/displaymargin.qml"))
            addExample("DelegateModel", "A PathView using DelegateModel to instantiate delegates", Qt.resolvedUrl("delegatemodel/slideshow.qml"))
            addExample("Draggable Selections", "Enabling drag-and-drop on DelegateModel delegates", Qt.resolvedUrl("delegatemodel/dragselection.qml"))
        }
    }
}
