import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import "../dialog"
import "../common" as C
import "../styles/variables.mjs" as Vars

GithubDialog {
    title: 'Clone a Repository'

    contentComponent: Component {
        C.Pane {
            ColumnLayout {
                width: parent.width
                C.TabBar {
                    id: _tabBar
                    Layout.fillWidth: true
                    C.TabButton {
                        text: 'GitHub.com'
                    }
                    C.TabButton {
                        text: 'GitHub Enterprise Server'
                    }
                    C.TabButton {
                        text: 'URL'
                    }
                }
                StackLayout {
                    Layout.fillWidth: true
                    currentIndex: _tabBar.currentIndex
                    C.Pane {
                        id: _githubDotCom
                        Loader {
                            anchors.left: parent.left
                            anchors.right: parent.right
                            sourceComponent: _githubDotComCallToAction
                        }
                    }
                    C.Pane {
                        id: _githubEnterprise
                        Loader {
                            anchors.left: parent.left
                            anchors.right: parent.right
                            sourceComponent: _githubEnterpriseCallToAction
                        }
                    }
                    C.Pane {
                        id: _generic
                    }
                }
            }
        }
    }

    Component {
        id: _githubDotComCallToAction
        C.Pane {
            padding: Vars.spacing
            width: parent.width

            RowLayout {
                width: parent.width
                spacing: Vars.spacingX2
                Text {
                    //Layout.preferredWidth: parent.width - _signInBtn.width - parent.spacing
                    elide: Text.ElideRight
                    text: 'Sign in to your GitHub.com account to access your repositories.'
                    wrapMode: Text.WordWrap
                }
                Button {
                    id: _signInBtn
                    Layout.alignment: Qt.AlignBottom | Qt.AlignRight
                    implicitHeight: Vars.button_height
                    implicitWidth: 120
                    hoverEnabled: true
                    opacity: enabled ? 1.0 : 0.6
                    contentItem: Text {
                        text: 'Sign In'
                        font {
                            pixelSize: Vars.font_size
                        }
                        color: Vars.button_text_color
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }

                    background: Rectangle {
                        radius: Vars.border_radius
                        border.width: Vars.base_border_width
                        border.color: Vars.base_border_color
                        color: (hovered
                                && enabled) ? Vars.button_hover_background : Vars.button_background
                    }
                }
            }
        }
    }

    Component {
        id: _githubEnterpriseCallToAction
        C.Pane {
            padding: Vars.spacing
            width: parent.width

            RowLayout {
                width: parent.width
                spacing: Vars.spacingX2
                Text {
                    elide: Text.ElideRight
                    text: 'If you have a GitHub Enterprise Server account at work,sign in to it to get access to your repositories.'
                    wrapMode: Text.WordWrap
                }
                Button {
                    id: _signInBtn
                    Layout.alignment: Qt.AlignBottom | Qt.AlignRight
                    implicitHeight: Vars.button_height
                    implicitWidth: 120
                    hoverEnabled: true
                    opacity: enabled ? 1.0 : 0.6
                    contentItem: Text {
                        text: 'Sign In'
                        font {
                            pixelSize: Vars.font_size
                        }
                        color: Vars.button_text_color
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }

                    background: Rectangle {
                        radius: Vars.border_radius
                        border.width: Vars.base_border_width
                        border.color: Vars.base_border_color
                        color: (hovered
                                && enabled) ? Vars.button_hover_background : Vars.button_background
                    }
                }
            }
        }
    }

    Component {
        id: cloneGenericRepository
        C.Pane {
            padding: Vars.spacingX2
            ColumnLayout {
                width: parent.width
                spacing: Vars.spacing
                ColumnLayout {
                    spacing: Vars.spacing_third
                }
            }
        }
    }
}
