import QtQuick 2.12

Rectangle {
    id: container

    property alias text: label.text
    signal clicked

    width: label.width + 20
    height: label.height + 6
    radius: height / 2

    gradient: Gradient {
        GradientStop{
            id:gradientStop
            position: 0.0
            color:"#FF28A6EE"
        }
        GradientStop {
            position: 1.0
            color:"#FF28C4EF"
        }
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        onClicked: {
            container.clicked()
        }
    }

    Text {
        id: label
        anchors.centerIn: parent
    }

    states: State {
        name:"pressed"
        when: mouseArea.pressed
        PropertyChanges {
            target: gradientStop
            color:"#FF457EE0"
        }
    }

}
