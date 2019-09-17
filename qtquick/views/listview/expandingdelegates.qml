import QtQuick 2.12
import "content"

Rectangle {
    id: page
    width: 400
    height: 240
    color: "black"

    Component {
        id: recipeDelegate
        Item {
            id: recipe
            property real detailsOpacity: 0

            width: listView.width
            height: 70

            Rectangle {
                id: background
                x: 2
                y: 2
                width: parent.width - x * 2
                height: parent.height - y * 2
                color: "ivory"
                border.color: "orange"
                radius: 5
            }

            MouseArea {
                anchors.fill: parent
                onClicked: recipe.state = 'Details'
            }

            Row {
                id: topLayout
                x: 10
                y: 10
                height: recipeImage.height
                width: parent.width
                spacing: 10

                Image {
                    id: recipeImage
                    width: 50
                    height: 50
                    source: picture
                }

                Column {
                    width: background.width - recipeImage.width - 20
                    height: recipeImage.height
                    spacing: 5

                    Text {
                        text: title
                        font.bold: true
                        font.pointSize: 16
                    }

                    SmallText {
                        text: "Ingredients"
                        font.bold: true
                        opacity: recipe.detailsOpacity
                    }

                    SmallText {
                        text: ingredients
                        wrapMode: Text.WordWrap
                        width: parent.width
                        opacity: recipe.detailsOpacity
                    }
                }
            }
            Item {
                id: details
                x: 10
                width: parent.width - 20
                anchors {
                    top: topLayout.bottom
                    bottomMargin: 10
                    bottom: parent.bottom
                }
                opacity: recipe.detailsOpacity

                SmallText {
                    id: methodTitle
                    anchors.top: parent.top
                    text: "Method"
                    font.pointSize: 12
                    font.bold: true
                }

                Flickable {
                    id: flick
                    width: parent.width
                    anchors {
                        top: methodTitle.bottom
                        bottom: parent.bottom
                    }
                    contentHeight: methodText.height
                    clip: true

                    Text {
                        id: methodText
                        text: method
                        wrapMode: Text.WordWrap
                        width: details.width
                    }
                }

                Image {
                    anchors {
                        right: flick.right
                        top: flick.top
                    }
                    source:"content/pics/moreUp.png"
                    opacity: flick.atYBeginning ? 0: 1
                }

                Image {
                    anchors{
                        right: flick.right
                        bottom: flick.bottom
                    }
                    source:"content/pics/moreDown.png"
                    opacity: flick.atYEnd ? 0: 1
                }
            }

            TextButton {
                y: 10
                anchors {
                    right: background.right
                    rightMargin: 10
                }
                opacity: recipe.detailsOpacity
                text:"Close"
                onClicked: recipe.state = ''
            }

            states:State{
                name:"Details"
                PropertyChanges{
                    target: background
                    color: "white"
                }
                PropertyChanges {
                    target: recipeImage
                    width: 130
                    height: 130
                }
                PropertyChanges {
                    target: recipe
                    detailsOpacity: 1
                    x: 0
                }
                PropertyChanges {
                    target: recipe
                    height: listView.height
                }
                PropertyChanges {
                    target: recipe.ListView.view
                    explicit: true
                    contentY: recipe.y
                }
                PropertyChanges {
                    target:  recipe.ListView.view
                    interactive: false
                }
            }

            transitions: Transition {
                ParallelAnimation{

                    ColorAnimation {
                        property:"color"
                        duration: 500
                    }
                    NumberAnimation {
                        duration:300
                        properties:"detailsOpacity,x,contentY,height,width"
                    }
                }

            }
        }
    }

    ListView {
        id: listView
        anchors.fill: parent
        model: RecipesModel{}
        delegate: recipeDelegate
    }
}
