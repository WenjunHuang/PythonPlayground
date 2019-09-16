import QtQuick 2.12
import QtQuick.XmlListModel 2.12
import QtQml.Models 2.12

Package {
   Item {
       Package.name:"browser"
       GridView {
           id: photosGridView
           model: visualModel.parts.grid
           width:mainWindow.width
           height: mainWindow.height - 21
       }
   }
}
