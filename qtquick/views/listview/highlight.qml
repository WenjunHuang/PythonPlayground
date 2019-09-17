import QtQuick 2.12
import "content"

Rectangle {
    width: 200
    height: 300

    Component {
        id: petDelegate
        Item {
            id: wrapper
            width: 200
            height: 55
            Column {
                SmallText{text:'Name: ' + name }
                SmallText{text:'Type: ' + type }
                SmallText{text:'Age: ' + age }
            }

            states: State {
                name: 'Current'
                when: wrapper.ListView.isCurrentItem
                PropertyChanges {
                    target: wrapper
                    x: 20
                }
            }
            transitions: Transition {
                NumberAnimation{
                    properties:"x"
                    duration: 200
                }
            }
            MouseArea {
                anchors.fill: parent
                onClicked: wrapper.ListView.view.currentIndex = index
            }
        }
    }

    Component {
        id: highlightBar
        Rectangle {
            width: 200
            height: 50
            color: "#FFFF88"
            y: listView.currentItem.y
            Behavior on y {
                SpringAnimation{
                    spring:2
                    damping: 0.1
                }
            }
        }
    }

    ListView {
        id: listView
        width: 200
        height: parent.height
        x: 30

        model: PetsModel{}
        delegate: petDelegate
        focus: true
        highlight: highlightBar
        highlightFollowsCurrentItem: false
    }
}
