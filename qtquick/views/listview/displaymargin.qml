import QtQuick 2.12

Item {
    width: 480
    height: 320

    ListView {
        id: view
        anchors.top: header.bottom
        anchors.bottom: footer.top
        width: parent.width
        cacheBuffer: 0
        displayMarginBeginning: 40
        displayMarginEnd: 40

        model: 100
        delegate: Rectangle {
            objectName: "delegate"
            width: parent.width
            height: 25
            color: index % 2?"steelblue": "lightsteelblue"
            Text{
                anchors.centerIn: parent
                color:"white"
                text:"Item" + (index + 1)
            }
        }
    }

    Rectangle {
        id: header
        width: parent.width
        height: 40
        color: "#AAFF0000"
        Text {
            anchors.centerIn: parent
            font.pixelSize: 24
            text:"Header"
        }
    }

    Rectangle {
        id: footer
        anchors.bottom: parent.bottom
        width: parent.width
        height: 40
        color: "#AAFF0000"

        Text {
            anchors.centerIn: parent
            font.pixelSize: 24
            text:"Footer"
        }
    }

}
