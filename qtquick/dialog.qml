import QtQuick 2.0
import QtQuick.Controls 2.12

Item {
    width: 640
    height: 480

    Item {
        id: dialogContainer
        anchors.fill: parent
        Dialog {
            id: dialog
            title: "Title"
            modal: true
            closePolicy: Popup.NoAutoClose
            anchors.centerIn: Overlay.overlay
            onAccepted: console.log("Ok clicked")
            onRejected: console.log("Cancel clicked")
            footer: Row{
                Button{
                    text:'close'
                    onClicked:{
                        dialogContainer.hide()
                    }
                }
            }
        }

        state: 'hidden'
        states: [
            State {
                name: 'show'
                PropertyChanges {
                    target: dialog
                    scale: 0.1
                    opacity: 0.1
                    visible: true
                }
            },
            State {
                name: 'hidden'
                PropertyChanges {
                    target: dialog
                    visible: false
                }
            }
        ]
        transitions: [
            Transition {
                from: "hidden"
                to: "show"
                SequentialAnimation {

                    PropertyAction {
                        target: dialog
                        properties: "scale,opacity,visible"
                    }
                    ParallelAnimation {
                        NumberAnimation {
                            target: dialog
                            property: "opacity"
                            to: 1.0
                            duration: 200
                            easing.type: Easing.InOutQuad
                        }

                        NumberAnimation {
                            target: dialog
                            property: "scale"
                            to: 1.0
                            duration: 200
                            easing.type: Easing.InOutQuad
                        }
                    }
                }
            },
            Transition {
                from: "show"
                to: "hidden"
                SequentialAnimation {
                    ParallelAnimation {
                        NumberAnimation {
                            target: dialog
                            property: "opacity"
                            to: 0.1
                            duration: 300
                            easing.type: Easing.InOutQuad
                        }

                        NumberAnimation {
                            target: dialog
                            property: "scale"
                            to: 0.1
                            duration: 300
                            easing.type: Easing.InBack
                        }
                    }

                    PropertyAction {
                        target: dialog; property: "visible";value:false }
                }
            }
        ]

        function open() {
            dialogContainer.state = 'show'
        }

        function hide() {
            dialogContainer.state = 'hidden'
        }
    }

    Button {
        text: 'show dialog'
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        onClicked: {
            dialogContainer.open()
        }
    }
}
