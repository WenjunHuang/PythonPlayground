import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtQuick.Dialogs 1.2
import "../dialog"
import "../common" as C
import "../styles/variables.mjs" as Vars

GithubDialog {
    title: 'Create a New Repository'
    submitButtonText: 'Create Repository'
    dismissButtonText: 'Cancel'

    contentComponent: Component {
        C.Pane {
            padding: Vars.spacingX2
            ColumnLayout {
                spacing: Vars.spacing
                anchors.left: parent.left
                anchors.right: parent.right
                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: Vars.spacing_third
                    Text {
                        text: 'Name'
                        font.pixelSize: Vars.font_size
                    }
                    C.TextInput {
                        Layout.fillWidth: true
                        placeholderText: 'repository name'
                    }
                }
                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: Vars.spacing_third
                    Text {
                        text: 'Description'
                        font.pixelSize: Vars.font_size
                    }
                    C.TextInput {
                        Layout.fillWidth: true
                    }
                }
                ColumnLayout {
                    Layout.fillWidth: true
                    spacing: Vars.spacing_third
                    Text {
                        text: 'Local Path'
                        font.pixelSize: Vars.font_size
                        Layout.fillWidth: true
                    }
                    RowLayout {
                        Layout.fillWidth: true
                        spacing: Vars.spacing
                        C.TextInput {
                            Layout.fillWidth: true
                        }
                        Button {
                            id: _chooseButton
                            Layout.alignment: Qt.AlignRight
                            hoverEnabled: true
                            contentItem: Text {
                                id: _text
                                text: 'Choose...'
                                font {
                                    pixelSize: Vars.font_size
                                }
                                color: Vars.secondary_button_text_color
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }

                            background: Rectangle {
                                implicitHeight: Vars.button_height
                                implicitWidth: _text.implicitWidth + Vars.spacingX2
                                radius: Vars.border_radius
                                border.width: Vars.base_border_width
                                border.color: Vars.base_border_color
                                color: Vars.secondary_button_background
                            }
                            onClicked: {
                                fileDialog.open()
                            }
                        }
                    }
                }
                C.CheckBox {
                    text: 'Initialize this repository with a README'
                }

                ColumnLayout {
                    spacing: Vars.spacing_third
                    Layout.fillWidth: true
                    Text {
                        text: 'Git Ignore'
                        font.pixelSize: Vars.font_size
                        color: Vars.text_color
                    }
                    C.ComboBox {
                        Layout.fillWidth: true
                        model: ['None', 'Python', 'CPP', 'SBT']
                    }
                }
                ColumnLayout {
                    spacing: Vars.spacing_third
                    Layout.fillWidth: true
                    Text {
                        text: 'License'
                        font.pixelSize: Vars.font_size
                        color: Vars.text_color
                    }
                    C.ComboBox {
                        Layout.fillWidth: true
                        model: ['None', 'MIT', 'GPL']
                    }
                }
            }
        }
    }

    FileDialog {
        id: fileDialog
        modality: Qt.WindowModal
        title: "Choose a folder"
        selectFolder: true
        selectedNameFilter: "All files (*)"
        onAccepted: {
            console.log("Accepted: " + fileUrls)
        }
        onRejected: {
            console.log("Rejected")
        }
    }
}
