import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import "../octicons"
import "../styles/variables.mjs" as Vars

Pane {
    padding: Vars.spacingX2
    ColumnLayout {
        spacing: Vars.spacing
        anchors.left: parent.left
        anchors.right: parent.right

        ColumnLayout {
            Layout.fillWidth: true
            spacing: Vars.spacing_third
            Text {
                Layout.fillWidth: true
                text: 'User name or email addres'
                font.pixelSize: Vars.font_size
            }
            Rectangle {
                Layout.fillWidth: true
                border.width: 1
                border.color: Vars.box_border_color
                radius: Vars.border_radius
                implicitHeight: _userAccount.implicitHeight

                TextInput {
                    id: _userAccount
                    anchors.fill: parent
                    leftPadding: Vars.spacing_half
                    rightPadding: Vars.spacing_half
                    topPadding: Vars.spacing_third
                    bottomPadding: Vars.spacing_third
                }
            }
        }
        ColumnLayout {
            Layout.fillWidth: true
            spacing: Vars.spacing_third
            Text {
                Layout.fillWidth: true
                text: 'password'
                font.pixelSize: Vars.font_size
            }
            Rectangle {
                Layout.fillWidth: true
                border.width: 1
                border.color: Vars.box_border_color
                radius: Vars.border_radius
                implicitHeight: _userPassword.implicitHeight

                TextInput {
                    id: _userPassword
                    anchors.fill: parent
                    leftPadding: Vars.spacing_half
                    rightPadding: Vars.spacing_half
                    topPadding: Vars.spacing_third
                    bottomPadding: Vars.spacing_third
                    echoMode: TextInput.Password
                }
            }
        }

        Text {
            id:_forgotPassword
            Layout.fillWidth: true
            text: 'Forgot password?'
            color: Vars.link_button_color
            font.pixelSize: Vars.font_size
            font.underline: _forgotPasswordMA.containsMouse
            horizontalAlignment: Text.AlignRight
            MouseArea{
                id: _forgotPasswordMA
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: containsMouse?
                    Qt.PointingHandCursor:Qt.ArrowCursor
            }
        }

        ColumnLayout {
            Layout.fillWidth: true
            spacing: Vars.spacing_half
            Pane {
                Layout.fillWidth: true
                contentHeight: _or.implicitHeight
                padding:0
                Rectangle {
                    height: 1
                    color: Vars.box_border_color
                    Layout.fillWidth: true
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.verticalCenter: parent.verticalCenter
                }

                Pane {
                    anchors.centerIn: parent
                    anchors.verticalCenterOffset: -3
                    padding:0
                    Text {
                        id: _or
                        text: "or"
                        font.pixelSize: Vars.font_size
                    }
                }
            }
            Pane {
                Layout.fillWidth: true
                contentHeight: _externalText.implicitHeight
                padding:0
                RowLayout {
                    anchors.centerIn: parent
                    Text {
                        id: _externalText
                        Layout.fillWidth: true
                        text: 'Sign in using your browser'
                        color: Vars.link_button_color
                        font.pixelSize: Vars.font_size
                        font.underline: _externalTextMA.containsMouse
                        MouseArea{
                            id: _externalTextMA
                            anchors.fill: parent
                            hoverEnabled: true
                            cursorShape: containsMouse?
                                Qt.PointingHandCursor:Qt.ArrowCursor
                        }
                    }
                    Octicon {
                        id: _loadingIcon
                        symbol: 'link-external'
                        width: 12
                        height: 16
                    }
                }
            }
        }
    }
}
