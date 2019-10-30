import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12
import Test 1.0

Window {
    width: 480
    height: 480
    visible:true
    property var foo : Kind.Bar
    Text {
        text: "value is:" + foo
        anchors.centerIn:parent
    }
}