import QtQuick 2.12
import People 1.0

BirthdayParty{
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
                price:19.95
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