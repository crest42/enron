from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EmailAddressToRecieversSameDomain(DiscoverableTransform):
    """
    Given a  maltego.EmailAddress Entity, return the set of Emails sent by that address from the Enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        email_address = request.Value
        res = db.get_recipients_by_email_same_domain(email_address, limit=request.Slider)
        for d in res:
            for r in d['recipients']:
                ent = response.addEntity('maltego.EmailAddress', r)
