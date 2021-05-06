from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email


class EnronDatasetToTLD(DiscoverableTransform):
    """
    Given a  robin.EnronDataset Entity, return a list of Involved TLDs.
    """

    @classmethod
    def create_entities(cls, request, response):
        res = db.get_tlds_from_ppl(limit=request.Slider)
        for d in res:
            ent = response.addEntity('maltego.Domain', d)
    