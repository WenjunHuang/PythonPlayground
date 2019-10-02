import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import Desktop 1.0
import "../dialog"
import "../common" as C
import "../octicons"
import "../styles/variables.mjs" as Vars

C.Pane {
    id: root
    padding: Vars.spacingX2

    BlockBuilder {
        id: bloc
        blocName:'AccountRepositoryBloc'

        onStateChanged: {
            const name = state.name
            if (name === 'RepositoryNotLoadedState')
                bloc.dispatch('LoadAccountRepositoryEvent',)
            else if (name === '')

        }
    }

    ColumnLayout {
        width: parent.width
        spacing:Vars.spacing
        RowLayout {
            Layout.fillWidth: true
            spacing: Vars.spacing

            C.TextInput {
                Layout.fillWidth: true
                placeholderText: 'Filter'
            }
            C.SecondaryButton {
                Layout.alignment: Qt.AlignRight
                image: Octicon {
                    id: icon
                    symbol: 'sync'
                    width: 12
                    height: 16
                }

                RotationAnimation {
                    id: ani
                    loops: Animation.Infinite
                    target: icon
                    from: 0
                    to: 360
                    duration: 2000
                    running:false
                }

                onClicked: {
                }
            }
        }

        ListView {

        }
    }

    states:[
        State{
            name:'uninit'
        },
        State{
            name:'loading'
        },
        State{
            name:'success'
        },
        State{
            name:'failed'
        }
    ]
}
