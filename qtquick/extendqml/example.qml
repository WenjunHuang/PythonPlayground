import QtQuick 2.12
import People 1.0

BirthdayParty{
    property var foo:BirthdayParty.Classic
    property var bar:BirthdayParty.Small
    host:Boy {
        name:"Bob Jones"
        shoe{size:12;color:"white";brand:"Bikey";price:90.0}
    }
        Boy{name:"Leo Hodges"
        BirthdayParty.rsvp:"2009-07-01"
            shoe{
                size:8
                color:"blue"
                brand:"Luma"
                price: notExist
            }
            Component.onCompleted:{
            console.log(shoe.price)
            }
        }
        Girl{name:"Anne Brown"
            shoe.size: 7
            shoe.color:"red"
            shoe.brand:"Job Macobs"
            shoe.price:699.99
        BirthdayParty.rsvp:"2009-07-06"
        }
}