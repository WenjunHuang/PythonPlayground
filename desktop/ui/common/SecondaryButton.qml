import QtQuick 2.12
import "../styles/variables.mjs" as Vars

Button {
    id: control
    implicitHeight: Vars.button_height

    hoverEnabled: true
    contentItem: Text {
        text: control.text
        font {
            pixelSize: Vars.font_size
        }
        color: Vars.secondary_button_text_color
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    background: Rectangle {
        radius: Vars.border_radius
        border.width: Vars.base_border_width
        border.color: Vars.base_border_color
        color: Vars.secondary_button_background
    }
}
