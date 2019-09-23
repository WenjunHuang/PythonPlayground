import QtQuick 2.12
import QtQml.Models 2.12

Item {
    id: root

    width: 320
    height: 480

    property bool dragging: false

    Component {
        id: packageDelegate
        Package {
            id: packageRoot

            MouseArea{
                id: visibleContainer
                Package.name: "visible"

                width: 64
                height: 64
                enabled: packageRoot.DelegateModel.inSelected
                drag.target: draggable

                Item {
                    id: draggable

                    width: 64
                    height: 64
                    Drag.active: visibleContainer.drag.active

                    anchors {
                        horizontalCenter: parent.horizontalCenter
                        verticalCenter: parent.verticalCenter
                    }

                    states: State {
                        when: visibleContainer.drag.active

                        AnchorChanges {
                            target: draggable
                            anchors {
                                horizontalCenter:undefined
                                verticalCenter: undefined
                            }
                        }
                        ParentChange {
                            target: selectionView
                            parent: draggable
                        }
                        PropertyChanges {
                            target: root
                            dragging: true
                        }
                        ParentChange {
                            target: draggable
                            parent: root
                        }
                    }
                }

                DropArea{
                    anchors.fill: parent
                    onEntered: selectedItems.move(0,visualModel.items.get(packageRoot.DelegateModel.itemsIndex),selectedItems.count)
                }
            }

            Item {
                id: selectionContainer
                Package.name:"selection"
                width: 64
                height: 64
                visible: PathView.onPath
            }

            Rectangle {
                id: content
                parent: visibleContainer

                width: 58
                height: 58

                radius: 8

                gradient: Gradient {
                    GradientStop{id:gradientStart; position: 0.0; color:"#8AC953"}
                    GradientStop{id: gradientEnd; position: 1.0; color:"#8BC953"}
                }

                border.width: 2
                border.color: "#007423"

                state: root.dragging && packageRoot.DelegateModel.inSelected ? "selected":"visible"

                Text {
                    anchors.fill:parent
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    color:"white"
                    text:modelData
                    font.pixelSize: 18
                }
            }
        }
    }

}
