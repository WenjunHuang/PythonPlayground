import QtQuick 2.13
import QtQuick.Window 2.13
import QtQml.Models 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    id: mainWindow
    visible: true
    title: qsTr("Hello World")

    property real downloadProgress: 0
    property bool imageLoading: false
    property bool editMode: false
    width: 800
    height: 400
    color:"#d5d6d8"

    ListModel {
        id: photosModel
        ListElement{tag:"Flowers"}
        ListElement{tag:"Wildlife"}
        ListElement{tag:"Prague"}
    }

    DelegateModel {
        id: albumVisualModel
        model: photosModel
        delegate: AlbumDelegate{}
    }

    Rectangle {
        focus: true
        Keys.onBackPressed: {
            event.accepted = true
            backButton.clicked()
        }
    }
}
