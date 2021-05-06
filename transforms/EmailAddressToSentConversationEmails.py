from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EmailAddressToSentConversationEmails(DiscoverableTransform):
    """
    Given a  maltego.EmailAddress Entity, return the set of Emails sent by that address from the Enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        email_address = request.Value
        res = db.get_sent_emails(email_address, limit=1000)
        for d in res:
            ent = row_dict_to_conversation_email(d, response)
            ent.setLinkLabel("sent")
    
