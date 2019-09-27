import QtQuick 2.12
import QtQuick.Controls 2.12

Popup {
    property string title
    property bool loading
    property bool disabled
    property Item header
    property Item footer

    signal dismissed()
    signal submit()


}
