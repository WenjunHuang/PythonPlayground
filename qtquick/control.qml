import QtQuick 2.12
import QtQuick.Controls 2.12

Pane {
    id: control
    topPadding: 0;bottomPadding: 0;leftPadding: 10;rightPadding: 10;
    implicitWidth: 120
    leftInset: 0
    topInset: 0
    rightInset: 0
    bottomInset: 0
    contentItem: Text {
        id: content
        text: "Content"
        horizontalAlignment: Qt.AlignHCenter
    }

    Component.onCompleted: {
        console.log(`width:${control.width}, height:${control.height}`);
        console.log(`contentWidth:${control.contentWidth}, contentHeight:${control.contentHeight}`);
        console.log(`Text width:${content.width}, height:${content.height}`);
    }
}
