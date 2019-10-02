import QtQuick 2.12
import QtQuick.Controls 2.12
import "../styles/variables.mjs" as Vars

Rectangle {
    property alias text: _textInput.text
    property alias echoMode: _textInput.echoMode
    property string placeholderText

    border.width: 1
    border.color: _textInput.focus ? Vars.focus_color : Vars.box_border_color
    radius: Vars.border_radius
    implicitHeight: _textInput.implicitHeight

    TextInput {
        id: _textInput
        anchors.fill: parent
        leftPadding: Vars.spacing_half
        rightPadding: Vars.spacing_half
        topPadding: Vars.spacing_third
        bottomPadding: Vars.spacing_third
        font.pixelSize: Vars.font_size
    }
    Text {
        text: placeholderText
        anchors.fill: parent
        color: Vars.box_border_color
        leftPadding: Vars.spacing_half
        rightPadding: Vars.spacing_half
        topPadding: Vars.spacing_third
        bottomPadding: Vars.spacing_third
        visible: placeholderText && !_textInput.text && !_textInput.focus
    }
}
