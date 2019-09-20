import QtQuick 2.12
import QtQml.Models 2.12

Rectangle {
    id: root
    color: "lightgray"
    width: 320
    height: 480
    property bool printDestruction: false

    ObjectModel {
        id: itemModel

        Rectangle {
            width: view.width
            height: view.height
            color: "#FFFEF0"
            Text {
                text: "Page 1"
                font.bold: true
                anchors.centerIn: parent
            }

            Component.onDestruction: if (printDestruction)
                                         print("destroyed 1")
        }

        Rectangle {
            width: view.width
            height: view.height
            color: "#F0FFF7"
            Text {
                text:"Page 2"
                font.bold: true
                anchors.centerIn: parent
            }
            Component.onDestruction: if (printDestruction) print("destroyed 2")
        }
    }
}
