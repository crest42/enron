from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class DomainToEnronUsers(DiscoverableTransform):
    """
    Given a  maltego.Domain Entity, return a list of Users for this Domain.
    """

    @classmethod
    def create_entities(cls, request, response):
        domain = request.Value
        res = db.get_ppl_by_domain(domain, limit=request.Slider)
        for d in res:
            ent = response.addEntity('maltego.EmailAddress', d['email'])
    