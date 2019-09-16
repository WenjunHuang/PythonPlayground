import QtQuick 2.0
import QtQuick.Particles 2.0

Rectangle {
    color: "white"
    width: 640
    height: 480
    ParticleSystem {
        id: sys
    }

    ImageParticle {
        sprites: [
            Sprite {
                name:"bear"
                source:"../images/bear_tiles.png"
                frameCount: 13
                frameDuration: 120
            }
        ]
        colorVariation: 0.5
        rotationVelocityVariation: 360
        colorTable: "../images/colortable.png"
        system:sys
    }
    Friction {
        factor: 0.1
        system:sys
    }

    Emitter {
        system: sys
        anchors.centerIn: parent
        id:particles
        emitRate: 200
        lifeSpan: 6000
        velocity: AngleDirection{
            angleVariation: 360
            magnitude: 80
            magnitudeVariation: 40
        }
        size: 60
        endSize: 120
    }

    Text {
        x: 16
        y: 16
        text: "QML..."
        style: Text.Outline
        styleColor: "#AAAAAA"
        font.pixelSize: 32
    }
    Text {
        anchors.bottom: parent.bottom
        anchors.right: parent.right
        anchors.margins: 16
        text:"... can you be trusted with the power?"
        style:Text.Outline
        styleColor:"#AAAAAA"
        font.pixelSize: width>400?32:16
    }

}
