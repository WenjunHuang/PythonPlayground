import QtQuick 2.12
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.13
import "../styles/variables.mjs" as Vars
import "../border"
import "../octicons"

Rectangle {
    property string title: "Demo"
    property bool dismissable:true
    property bool loading: true
    signal dismissed

    height: 50
    color: 'white'

    Border {
        commonBorder: false
        bBorderwidth: Vars.base_border_width
        borderColor: Vars.base_border_color

        Component.onCompleted: {
            console.log(Vars.base_border_width)
            console.log(Vars.base_border_color)
        }
    }

    Text {
        id: _title
        text: title
        font {
            weight: Vars.font_weight_semibold
            pixelSize: Vars.font_size_md
        }
        color: Vars.text_color
        anchors.left: parent.left
        anchors.leftMargin: Vars.spacingX2
        anchors.verticalCenter: parent.verticalCenter
    }

    Octicon {
        id: _loadingIcon
        symbol: 'sync'
        width: 12
        height: 16
        anchors.left: _title.right
        anchors.leftMargin: Vars.spacing
        anchors.verticalCenter: parent.verticalCenter
    }

    Octicon {
        id: _closeIcon
        symbol:'x'
        width:12
        height:16
        anchors.right:parent.right
        anchors.rightMargin: Vars.spacingX2
        anchors.verticalCenter: parent.verticalCenter
        visible: dismissable
    }

    ColorOverlay {
        anchors.fill:_closeIcon
        source:_closeIcon
        color:Vars.text_secondary_color
        visible: dismissable
    }

    RotationAnimation {
        id: _loadingIconAnimation
        target: _loadingIcon
        direction: RotationAnimation.Clockwise
        loops: Animation.Infinite
        from: 0
        to: 360
        duration: 1000
        running: false
    }

    states: [
        State {
            name: "normal"
            when: !loading
            StateChangeScript {
                script: _loadingIconAnimation.stop()
            }
            PropertyChanges {
                target: _loadingIcon
                visible: false
            }
        },
        State {
            name: "loading"
            when: loading
            PropertyChanges {
                target: _loadingIcon
                visible: true
            }
            StateChangeScript {
                script: _loadingIconAnimation.start()
            }
        }
    ]
}
