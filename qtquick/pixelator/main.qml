import QtQuick 2.12
import QtQuick.Window 2.12
import ImageModel 1.0

Window {
    visible: true
    width: 900
    height: 900
    title:qsTr("TableView Pixelator")

    Component {
        id: pixelDelegate
        Item {
            readonly property real gray: model.display / 255.0
            readonly property real size: 16

            implicitWidth: size
            implicitHeight: size

            Rectangle {
            id: rect
            anchors.centerIn: parent
            color:"#09102b"
            radius: size - gray * size
            implicitWidth: radius
            implicitHeight: radius
            ColorAnimation on color {
                id: colorAnimation
                running: false
                to: "#41cd52"
                duration: 1500
            }
            }
            MouseArea {
                anchors.fill: parent
                hoverEnabled: true
                onEntered: rect.color = "#cecfd5"
                onExited: colorAnimation.start()
            }
        }
    }

    TableView {
        id: tableView
        anchors.fill: parent
        model: ImageModel {
            source:"./qt.png"
        }
        delegate:pixelDelegate
    }
}