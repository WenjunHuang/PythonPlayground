import QtQuick 2.12
import QtQml.Models 2.12

Rectangle {
    id: root
    color: "white"
    width: 320
    height: 480
    property int upTo: 0

    SequentialAnimation on upTo {
        loops: -1
        NumberAnimation {
            to: 8
            duration: 3500
        }
        NumberAnimation {
            to: 0
            duration: 3500
        }
    }

    ListModel {
        id: myModel
        ListElement { display: "One" }
        ListElement { display: "Two" }
        ListElement { display: "Three" }
        ListElement { display: "Four" }
        ListElement { display: "Five" }
        ListElement { display: "Six" }
        ListElement { display: "Seven" }
        ListElement { display: "Eight" }
    }

    DelegateModel {
        id: visualModel
        delegate: Delegate {}
        model: myModel
    }

    ListView {
        id: lv
        height: parent.height / 2
        width: parent.width
        model: visualModel.parts.list
    }
    GridView {
        y: parent.height/2
        height: parent.height / 2
        width: parent.width
        cellWidth: width / 2
        cellHeight: 50
        model: visualModel.parts.grid
    }

    Text {
        anchors.bottom: parent.bottom
    }
}
