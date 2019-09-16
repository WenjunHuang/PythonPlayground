import QtQuick 2.13
import QtQuick.Controls 2.5
import QtQuick.Window 2.0
import QtQuick.Shapes 1.13

Window {
    id: root
    visible: true
    title: "Hello Python World!"
    width: 200
    height: 200

    ScrollView {
    width: 200
      height: 200
        clip:true
        Label {
        text:"ABC"
        font.pixelSize: 224
        }

          Shape {
                  width: 200
                  height: 150
        //          anchors.centerIn: parent
                  ShapePath {
                      strokeWidth: 4
                      strokeColor: "red"
                      fillGradient: LinearGradient {
                          x1: 20; y1: 20
                          x2: 180; y2: 130
                          GradientStop { position: 0; color: "blue" }
                          GradientStop { position: 0.2; color: "green" }
                          GradientStop { position: 0.4; color: "red" }
                          GradientStop { position: 0.6; color: "yellow" }
                          GradientStop { position: 1; color: "cyan" }
                      }
                      strokeStyle: ShapePath.DashLine
                      dashPattern: [ 1, 4 ]
                      startX: 20; startY: 20
                      PathLine { x: 180; y: 130 }
                      PathLine { x: 20; y: 130 }
                      PathLine { x: 20; y: 20 }
                  }
                 MouseArea {
                      anchors.fill: parent
                      drag.target: parent
                      drag.axis: Drag.XAndYAxis
                  }
              }
    }


}

