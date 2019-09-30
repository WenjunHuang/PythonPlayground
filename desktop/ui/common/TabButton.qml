import QtQuick 2.12
import QtQuick.Controls 2.12
import "../styles/variables.mjs" as Vars

TabButton {
    id: control

    property bool selected: control.TabBar.tabBar.currentIndex === control.TabBar.index

    font.pixelSize: Vars.font_size

    contentItem: Text {
        text: control.text
        font: control.font
        color: Vars.text_color
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        elide: Text.ElideRight
    }

    background: Rectangle {
        implicitHeight: Vars.tab_bar_height
        color: control.hovered ? Vars.tab_bar_hover_background_color : Vars.tab_bar_background_color

        Border {
            commonBorder: false
            lBorderwidth: 0
            tBorderwidth: 0
            bBorderwidth: 1
            rBorderwidth: control.TabBar.index === control.TabBar.tabBar.count - 1 ? 0 : 1
            color: Vars.box_border_color
        }

        Rectangle {
            implicitHeight: 3
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            color: Vars.tab_bar_active_color
            visible: selected
        }
    }

    hoverEnabled: true
}
