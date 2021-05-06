from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class ThreadToEmails(DiscoverableTransform):
    """
    Given a  maltego.EnronThread Entity, return a list of participants from the enron dataset.
    """

    @classmethod
    def create_entities(cls, request, response):
        thread = request.Value
        #res = db.get_recipients_from_mail(email_id, limit=request.Slider)
        