import QtQuick 2.0
import QtQuick.Controls 2.12
import "dialog_config.js" as Config

Item {
    width: 640
    height: 480

    Item {
        id: dialogContainer
        anchors.fill: parent
        Popup {
            id: dialog
            modal: true
            closePolicy: Popup.NoAutoClose
            anchors.centerIn: Overlay.overlay
            //            standardButtons: Dialog.Ok | Dialog.Cancel
            //            onAccepted: console.log("Ok clicked")
            //            onRejected: console.log("Cancel clicked")
            background: Rectangle {
                border.color: 'orange'
                radius: Config.kBaseUnit * 2
            }
            contentItem: Column {
                Item {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 50
                    Text {
                        id: header
                        text: "Title"
                        font.pixelSize: Config.kTextUnit * 6
                        anchors.left: parent.left
                        anchors.verticalCenter: parent.verticalCenter
                    }
                }
                Item {
                    id: content
                    //                    anchors.top: header.bottom
                    implicitHeight: 200
                    implicitWidth: 200
                }
                Item {
                    id: footer
                    height: 50
                    anchors.left:parent.left
                    anchors.right:parent.right

                    Button {
                        anchors.right: parent.right
                        anchors.rightMargin: Config.kBaseUnit * 3
                        anchors.verticalCenter: parent.verticalCenter
                        text: 'Close'
                        onClicked: {
                            dialogContainer.hide()
                        }
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
                        target: dialog
                        property: "visible"
                        value: false
                    }
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
