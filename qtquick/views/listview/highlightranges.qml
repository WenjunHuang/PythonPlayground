import QtQuick 2.0
import "content"

Rectangle {
    id: root
    property int current: 0
    property bool increasing: true

    SequentialAnimation {
        id: anim
        loops: -1
        running: true
        ScriptAction {
            script: if (increasing) {
                        current++
                        if (current >= aModel.count - 1) {
                            current = aModel.count - 1
                            increasing = !increasing
                        }
                    } else {
                        current--
                        if (current <= 0) {
                            current = 0
                            increasing = !increasing
                        }
                    }
        }

        PauseAnimation {
            duration: 500
        }
    }

    MouseArea {
        id: ma
        z: 1
        anchors.fill: parent
        onClicked: {
            z = 1 - z
            if (anim.running)
                anim.stop()
            else
                anim.restart()
        }
    }

    width: 320
    height: 480

    ListView {
        id: list1
        height: 50
        width: parent.width
        model: PetsModel {
            id: aModel
        }
        delegate: petDelegate
        orientation: ListView.Horizontal

        highlight: Rectangle {
            color: "lightsteelblue"
        }
        currentIndex: root.current
        onCurrentIndexChanged: root.current = currentIndex
        focus: true
    }

    ListView {
        id: list2
        y: 160
        height: 50
        width: parent.width
        model: PetsModel {
        }
        delegate: petDelegate
        orientation: ListView.Horizontal
        highlight: Rectangle {
            color: "yellow"
        }
        currentIndex: root.current
        preferredHighlightBegin: 80
        preferredHighlightEnd: 220
        highlightRangeMode: ListView.ApplyRange
    }

    ListView {
        id: list3
        y: 320
        height: 50
        width: parent.width
        model: PetsModel{}
        delegate: petDelegate
        orientation: ListView.Horizontal
        highlight: Rectangle{color:"yellow"}
        currentIndex: root.current
        onCurrentIndexChanged: root.current = currentIndex
        preferredHighlightBegin: 125
        preferredHighlightEnd: 125
        highlightRangeMode: ListView.StrictlyEnforceRange
    }

    Component {
        id: petDelegate
        Item {
            width: 160
            height: column.height
            Column {
                id: column
                Text {
                    text: 'Name: ' + name
                }
                Text {
                    text: 'Type: ' + type
                }
                Text {
                    text: 'Age: ' + age
                }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: root.current = index
            }
        }
    }
}
