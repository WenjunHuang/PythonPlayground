import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import "../styles/variables.mjs" as Vars

Pane {
    id: _dialog
    property string title: 'Demo'
    property bool loading: true
    property bool disabled
    property bool dismissable: true
    property string errorText

    signal dismissed
    signal submitted

    padding: 0
    implicitWidth: 400
    ColumnLayout {
        anchors.left: parent.left
        anchors.right: parent.right
        spacing: 0
        Header {
            id: _header
            dismissable: _dialog.dismissable
            loading: _dialog.loading
            Layout.fillWidth: true
        }
        Rectangle {
            height: 1
            id: _headerDivider
            color: Vars.box_border_color
            Layout.fillWidth: true
        }

        Error {
            id: _error
            text: errorText
            visible: errorText ? true : false
            Layout.fillWidth: true
        }
        Rectangle {
            id: _errorDivider
            height: 1
            color: Vars.form_error_border_color
            visible: errorText ? true : false
            Layout.fillWidth: true
        }

        Content {
            id: _content
            Layout.fillWidth: true
        }
        Rectangle {
            id: _contentDivider
            height: 1
            color: Vars.box_border_color
            Layout.fillWidth: true
        }
        Footer {
            id: _footer
            Layout.fillWidth: true
        }
    }
}
