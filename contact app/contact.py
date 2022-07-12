class Contact:
    contactId = -1
    def __init__(self, firstName, lastName, isActive, contactDetails):
        self.contactId = Contact.contactId
        self.firstName, self.lastName = firstName, lastName
        self.isActive = isActive
        self.contactDetails = contactDetails

    @staticmethod
    def createContact(firstName, lastName, isActive, contactDetails):
        Contact.contactId += 1
        return Contact(firstName, lastName, isActive, contactDetails)