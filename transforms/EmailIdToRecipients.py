from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EmailIdToRecipients(DiscoverableTransform):
    """
    Given a  maltego.ConversationEmail Entity, return a list of reciepients from the Enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        email_id = request.getProperty("email_id")
        res = db.get_recipients_from_mail(email_id, limit=request.Slider)
        for d in res:
            response.addEntity('maltego.EmailAddress', d['recipient'])
