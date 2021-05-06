from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class PersonToScheduledEvents(DiscoverableTransform):
    """
    Given a  maltego.EnronPerson Entity, return a list of of meetings scheduled by this person.
    """

    @classmethod
    def create_entities(cls, request, response):
        person = request.Value
        #res = db.get_recipients_from_mail(email_id, limit=request.Slider)
