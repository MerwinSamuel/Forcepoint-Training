class ContactDetail:
    detailId = -1
    def __init__(self, detailType, contactDetail):
        self.detailId = ContactDetail.detailId
        self.detailType, self.contactDetail = detailType, contactDetail

    @staticmethod
    def createContactDetail(detailType, contactDetail):
        ContactDetail.detailId += 1
        return ContactDetail(detailType, contactDetail)