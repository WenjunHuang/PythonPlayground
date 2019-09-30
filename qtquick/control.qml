import QtQuick 2.12
import QtQuick.Controls 2.12

Pane {
    id:control
    padding: 14
    leftInset: 10
    topInset: -20
    rightInset: 10
    bottomInset: 10
    contentItem:Text{
        id:content
    text:"Content"
    }
//    background:Rectangle{
//    color:"blue"
//    }

    Component.onCompleted: {
        console.log(content.height)
        console.log(control.availableHeight)
        console.log(control.implicitHeight)
        console.log(control.height)
    }
}
