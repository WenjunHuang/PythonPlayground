import QtQuick 2.12

Item {
    width: 200
    height: 100

    Rectangle {
        id: redRect
        width: 100
        height: 100
        color: "red"
    }

    Rectangle {
        id: blueRect
        x: redRect.width
        width: 50
        height: 50
        color: "blue"

        states: [
            State {
                name: "reparented"
                ParentChange {
                    target: blueRect
                    parent: redRect
                    x: 10
                    y: 10
                    width: 100
                    height: 100
                }
            }
        ]

        MouseArea {
            anchors.fill: parent
            onClicked: blueRect.state = "reparented"
        }

        transitions: Transition {
            ParentAnimation {
                NumberAnimation {
                    properties: "x,y,width,height"
                    duration: 100
                }
            }
        }
    }
}
