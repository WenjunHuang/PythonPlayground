import QtQuick 2.12
import QtQuick.Controls 2.12
import '../config.mjs' as Config

Rectangle {
    id: root
    width: 400
    height: 240
    color: "white"
    border.width:2
    border.color:"black"

    ListModel {
        id: appModel
        ListElement {
            name: "Music"
            icon: "pics/109951164453376191.jpeg"
        }
        ListElement {
            name: "Movies"
            icon: "pics/109951164455153525.jpeg"
        }
        ListElement {
            name: "Camera"
            icon: "pics/109951164456538009.jpeg"
        }
        ListElement {
            name: "Calendar"
            icon: "pics/109951164456579996.jpeg"
        }
        ListElement {
            name: "Messaging"
            icon: "pics/109951164456605073.jpeg"
        }
        ListElement {
            name: "Todo List"
            icon: "pics/109951164457291208.jpeg"
        }
        ListElement {
            name: "Contacts"
            icon: "pics/109951164457425046.jpeg"
        }
    }

    Component {
        id: appDelegate
        Item {
            width: myIcon.width
            height:myIcon.height
            scale: PathView.iconScale
            opacity: PathView.iconOpacity
            z:PathView.iconZorder
            anchors.verticalCenter: view.verticalCenter

            Image {
                width: 540
                height: 200
                id: myIcon
                anchors.horizontalCenter: parent.horizontalCenter
                source: icon
            }
            Text {
                anchors {
                    bottom: myIcon.bottom
                    right: myIcon.right
                }
                //text: parent.PathView.isCurrentItem ? name + " yes" : name
                text: name
            }

            MouseArea {
                anchors.fill: parent
                onClicked: view.currentIndex = index
            }
        }
    }

    Component {
        id: appHighlight
        Rectangle {
            width: 50
            height: 50
            color: "lightsteelblue"
        }
    }

    PathView {
        id: view
        anchors.bottom: pageIndicator.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        //highlight: appHighlight
        preferredHighlightBegin: 0.5
        preferredHighlightEnd: 0.5
        //focus: true
        model: appModel
        delegate: appDelegate
        snapMode:PathView.SnapToItem
        currentIndex:pageIndicator.currentIndex
        path: Path {
            startX: 0
            startY: 0
            PathAttribute {
                name: "iconScale"
                value: 0.5
            }
            PathAttribute {
                name:"iconOpacity"
                value: 0.3
            }
            PathAttribute{
                name:"iconZorder"
                value:0
            }

//            PathQuad {
//                x: 200
//                y: 150
//                controlX: 50
//                controlY: 200
//            }
//            PathAttribute {
//                name: "iconScale"
//                value: 1.0
//            }
//            PathAttribute {
//                name:"iconOpacity"
//                value: 1.0
//            }
//            PathQuad {
//                x: 390
//                y: 50
//                controlX: 350
//                controlY: 200
//            }
            PathLine{
                x:view.width / 2
                y:0
            }

            PathAttribute {
                name: "iconScale"
                value: 1.0
            }
            PathAttribute {
                name:"iconOpacity"
                value: 1.0
            }
            PathAttribute{
                name:"iconZorder"
                value:9999
            }
            PathLine{
                x:view.width
                y:0
            }
            PathAttribute {
                name: "iconScale"
                value: 0.5
            }
            PathAttribute {
                name:"iconOpacity"
                value: 0.3
            }

            PathAttribute{
                name:"iconZorder"
                value:0
            }
        }
    }
    PageIndicator {
          id: pageIndicator
          anchors.bottom:parent.bottom
          anchors.horizontalCenter: parent.horizontalCenter
          interactive: true
          count: appModel.count
          currentIndex: view.currentIndex
      }
}
