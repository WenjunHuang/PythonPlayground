import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

Window {
    width: 640
    height: 280
    title: "Python Async"
    visible: true

    Item {
        id: root
        anchors.fill: parent
        anchors.margins: 6

        TextField {
            id: inputUrl
            text:"https://jsonplaceholder.typicode.com/todos/1"
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right: parent.right
        }

        ScrollView {
            anchors.top: inputUrl.bottom
            anchors.topMargin: 6
            anchors.bottom: btnGet.top
            anchors.left: parent.left
            anchors.right: parent.right
            TextArea {
                id: taResponse
                placeholderText: qsTr("Enter description")
            }
        }

        Button {
            id: btnGet
            text: "Get"
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: {
                var url = inputUrl.text
                if (url) {
                    root.state = "loading"
                    const result = http.fetch(url,(result)=>{
                    taResponse.text = result;
                    root.state = "normal";
                                              })
                }
            }
        }

        Rectangle{
            id: busy
            color: Qt.rgba(0,0,0,0.2)
            visible: false
            enabled: visible
            anchors.fill: parent
        BusyIndicator{
            anchors.centerIn:parent
        }
        }

        state: "normal"
        states: [
            State {
                name: "loading"
                PropertyChanges {
                    target: btnGet
                    enabled: false
                }
                PropertyChanges {
                    target:busy
                    visible:true
                }
            },
            State {
                name: "normal"
            }
        ]
    }
}
