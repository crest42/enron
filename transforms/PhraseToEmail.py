from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email

class PhraseToEmail(DiscoverableTransform):
    """
    Given a  maltego.Phrase Entity, return a list of matching emails from the enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        phrase = request.Value
        sender = request.getTransformSetting('sender')
        res = PhraseToEmail.get_emails(phrase, sender, limit=request.Slider)
        for d in res:
            ent = row_dict_to_conversation_email(d, response)
            ent.setLinkLabel("sent")

    @staticmethod
    def get_emails(phrase, sender, limit=250):
        return db.search_mails_by_phrase(phrase, sender, limit)
