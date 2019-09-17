import QtQuick 2.12
import QtGraphicalEffects 1.13
import "content"

Rectangle {
    id: container
    width: 500
    height: 400
    color: "#343434"

    // The model
    ListModel {
        id: fruitModel

        ListElement {
            name: "Apple"
            cost: 2.45
            attributes: [
                ListElement {
                    description: "Core"
                },
                ListElement {
                    description: "Deciduous"
                }
            ]
        }
        ListElement {
            name: "Banana"
            cost: 1.95
            attributes: [
                ListElement {
                    description: "Tropical"
                },
                ListElement {
                    description: "Seedless"
                }
            ]
        }
        ListElement {
            name: "Cumquat"
            cost: 3.25
            attributes: [
                ListElement {
                    description: "Citrus"
                }
            ]
        }
        ListElement {
            name: "Durian"
            cost: 9.95
            attributes: [
                ListElement {
                    description: "Tropical"
                },
                ListElement {
                    description: "Smelly"
                }
            ]
        }
    }

    Component {
        id: listDelegate
        Item {
            id: delegateItem
            width: ListView.view.width
            height: 80
            clip: true

            Column {
                id: arrows
                anchors {
                    left: parent.left
                    verticalCenter: parent.verticalCenter
                }
                Item {
                    width: arrowUp.width
                    height: arrowUp.height

                    Image {
                        id: arrowUp
                        source: "content/pics/arrow-up.png"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: fruitModel.move(index, index - 1, 1)
                            enabled: index !== 0
                        }
                    }

                    ColorOverlay {
                        anchors.fill: arrowUp
                        source: arrowUp
                        color: "gray"
                        visible: index === 0
                    }
                }

                Item {
                    width: arrowDown.width
                    height: arrowDown.height
                    Image {
                        id: arrowDown
                        source: "content/pics/arrow-down.png"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: fruitModel.move(index, index + 1, 1)
                            enabled: index !== fruitModel.count - 1
                        }
                    }
                    ColorOverlay {
                        anchors.fill: arrowDown
                        source: arrowDown
                        color: "gray"
                        visible: index === fruitModel.count - 1
                    }
                }
            }

            Column {
                anchors {
                    left: arrows.right
                    horizontalCenter: parent.horizontalCenter
                    bottom: parent.verticalCenter
                }

                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: name
                    font.pixelSize: 15
                    color: "white"
                }

                Row {
                    anchors.horizontalCenter: parent.horizontalCenter
                    spacing: 5
                    Repeater {
                        model: attributes
                        Text {
                            text: description
                            color: "white"
                        }
                    }
                }
            }
            Item {
                anchors {
                    left: arrows.right
                    horizontalCenter: parent.horizontalCenter
                    top: parent.verticalCenter
                    bottom: parent.bottom
                }

                Row {
                    anchors.centerIn: parent
                    spacing: 10

                    PressAndHoldButton {
                        anchors.verticalCenter: parent.verticalCenter
                        source: "content/pics/plus-sign.png"
                        onClicked: fruitModel.setProperty(index, "cost",
                                                          cost + 0.25)
                    }

                    Text {
                        id: costText
                        anchors.verticalCenter: parent.verticalCenter
                        text: '$' + Number(cost).toFixed(2)
                        font.pixelSize: 15
                        color: "white"
                        font.bold: true
                    }

                    PressAndHoldButton {
                        anchors.verticalCenter: parent.verticalCenter
                        source: "content/pics/minus-sign.png"
                        onClicked: fruitModel.setProperty(index, "cost",
                                                          Math.max(0,
                                                                   cost - 0.25))
                    }

                    Image {
                        source: "content/pics/list-delete.png"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: fruitModel.remove(index)
                        }
                    }
                }
            }

            ListView.onAdd: SequentialAnimation {

                PropertyAction {
                    target: delegateItem
                    property: "height"
                    value: 0
                }

                NumberAnimation {
                    target: delegateItem
                    property: "height"
                    to: 80
                    duration: 250
                    easing.type: Easing.InOutQuad
                }
            }

            ListView.onRemove: SequentialAnimation {

                PropertyAction {
                    target: delegateItem
                    property: "ListView.delayRemove"
                    value: true
                }

                NumberAnimation {
                    target: delegateItem
                    property: "height"
                    to: 0
                    duration: 250
                    easing.type: Easing.InOutQuad
                }

                PropertyAction {
                    target: delegateItem
                    property: "ListView.delayRemove"
                    value: false
                }
            }
        }
    }

    ListView {
        id: lisView
        anchors {
            left: parent.left
            top: parent.top
            right: parent.right
            bottom: buttons.top
            margins: 20
        }
        model: fruitModel
        delegate: listDelegate
        move: Transition {
            NumberAnimation {
                properties: "x,y"
                duration: 250
            }
        }
        moveDisplaced: Transition {
            NumberAnimation {
                properties: "x,y"
                duration: 250
            }
        }
    }

    Row {
        id: buttons
        anchors {
            left: parent.left
            bottom: parent.bottom
            margins: 20
        }
        spacing: 10

        StadiumButton {
            text: "Add an item"
            onClicked: {
                fruitModel.append({
                                      "name": "Pizza Margarita",
                                      "cost": 5.95,
                                      "attributes": [{
                                              "description": "Cheese"
                                          }, {
                                              "description": "Tomato"
                                          }]
                                  })
            }
        }

        StadiumButton {
            text: "Remove all items"
            onClicked: fruitModel.clear()
        }
    }
}
