import json


class Customer:
    lastname = ""
    firstName = ""
    fullName=""
    dateOfBirth= "1970-01-01"
    personalEmail = ""
    place = ""
    postalCode=""
    personalTelephone = ""
    serviceTelephone = ""
    title = ""
    salutation = ""
    extendedName = ""
    serviceEmail=""
    street=""
    countryCode= "DEU"
    comment= "This is synthetic customer data"

    def toJson(self):
        return json.dumps(self,default=lambda o:o.__dict__)