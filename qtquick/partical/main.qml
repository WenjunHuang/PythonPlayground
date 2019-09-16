import QtQuick 2.13
import QtQuick.Window 2.13

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    LauncherList {
        id: ll
        anchors.fill:parent
        Component.onCompleted: {
            addExample("All at once",
                       "Uses all ImageParticle features",
                       Qt.resolvedUrl("content/allatonce.qml"))
            addExample("Colored", "Colorized image particles",  Qt.resolvedUrl("content/colored.qml"));
            addExample("Color Table", "Color-over-life rainbow particles",  Qt.resolvedUrl("content/colortable.qml"));
            addExample("Deformation", "Deformed particles",  Qt.resolvedUrl("content/deformation.qml"));
            addExample("Rotation", "Rotated particles",  Qt.resolvedUrl("content/rotation.qml"));
            addExample("Sharing", "Multiple ImageParticles on the same particles",  Qt.resolvedUrl("content/sharing.qml"));
            addExample("Sprites", "Particles rendered with sprites",  Qt.resolvedUrl("content/sprites.qml"));
        }
    }
}
