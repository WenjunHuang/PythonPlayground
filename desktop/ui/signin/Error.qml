import QtQuick 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.13
import "../octicons"
import "../styles/variables.mjs" as Vars

Pane {
    property alias text: _text.text
    padding: Vars.spacing
    leftInset: 0
    rightInset: 0
    topInset: 0
    bottomInset: 0
    contentHeight: _text.implicitHeight

    Octicon {
        id: _icon
        symbol: 'stop'
        width: 14
        height: 16
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter
    }

    ColorOverlay {
        anchors.fill: _icon
        source: _icon
        color: Vars.form_error_text_color
        visible: dismissable
    }

    Text {
        id: _text
        anchors.left: _icon.right
        anchors.leftMargin: Vars.spacing
        font.pixelSize: Vars.font_size
        color: Vars.form_error_text_color
    }

    background: Rectangle {
        color: Vars.form_error_background
    }
}
