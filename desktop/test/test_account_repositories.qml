import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Controls 2.0
import '../ui/clone_repository'


Window {
    id: root
    width: 640
    height: 480
    visible: true
    title:'Hello Python World!'

    AccountRepositories{
        anchors.fill: parent
    }

}