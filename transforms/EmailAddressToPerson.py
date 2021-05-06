from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EmailAddressToPerson(DiscoverableTransform):
    """
    Given a  maltego.EmailAddress Entity, return a Person from the Enron dataset
    """

    @classmethod
    def create_entities(cls, request, response):
        email = request.Value
        res = db.get_person_from_mail(email, limit=request.Slider)
        
