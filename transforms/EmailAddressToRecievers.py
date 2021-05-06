from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EmailAddressToRecievers(DiscoverableTransform):
    """
    Given a  maltego.EmailAddress Entity, return the set of Emails sent by that address from the Enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        email_address = request.Value
        domain = request.getTransformSetting('domain')
        minSend = int(request.getTransformSetting('minSend'))
        res = db.get_recipients_by_email(email_address, domain, minSend, limit=request.Slider)
        for d in res:
            for r in d['recipients']:
                ent = response.addEntity('maltego.EmailAddress', r)
