import QtQuick 2.12
import QtQuick.Controls 2.12
import "../styles/variables.mjs" as Vars

Pane {
    id: _footer
    padding:Vars.spacingX2
    contentHeight: _cancelButton.implicitHeight

    Button {
        id: _cancelButton
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        text: 'Cancel'
        implicitHeight: 25
        implicitWidth: 120
        contentItem: Text {
            text: _cancelButton.text
            font {
                pixelSize: Vars.font_size
            }
            color: Vars.secondary_button_text_color
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        background: Rectangle {
            implicitHeight: 25
            implicitWidth: 128
            radius: Vars.border_radius
            border.width: Vars.base_border_width
            border.color: Vars.base_border_color
            color: Vars.secondary_button_background
        }
    }
    Button {
        id:_signinButton
        text: 'Sign in'
        implicitHeight: 25
        implicitWidth: 120
        anchors.right: _cancelButton.left
        anchors.rightMargin: Vars.spacing_half
        anchors.verticalCenter: parent.verticalCenter
        contentItem: Text {
            text: _signinButton.text
            font {
                pixelSize: Vars.font_size
            }
            color: Vars.button_text_color
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }

        background: Rectangle {
            implicitHeight: 25
            implicitWidth: 128
            radius: Vars.border_radius
            border.width: Vars.base_border_width
            border.color: Vars.base_border_color
            color: Vars.button_background
        }
    }
}
