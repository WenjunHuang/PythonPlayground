import QtQuick 2.12
import QtQuick.Particles 2.12

Rectangle {
    width: 360
    height: 450
    color:"black"

    ParticleSystem{
        anchors.fill: parent
        ImageParticle{
            groups:["stars"]
            anchors.fill: parent
            source:"qrc:///particleresources/star.png"
        }
        Emitter {
            group:"stars"
            emitRate: 800
            lifeSpan: 2400
            size: 24
            sizeVariation: 8
            anchors.fill: parent
        }

        ImageParticle{
            anchors.fill: parent
            source:"qrc:///particleresources/star.png"
            alpha:0
            alphaVariation: 0.2
            colorVariation: 1.0
        }

        Emitter {
            anchors.centerIn: parent
            emitRate: 400
            lifeSpan: 2400
            size: 48
            sizeVariation: 8
            velocity: AngleDirection{
                angleVariation: 180
                magnitude: 60
            }
        }

        Turbulence {
            anchors.fill: parent
            strength: 2
        }
    }

}
