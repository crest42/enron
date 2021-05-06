from maltego_trx.transform import DiscoverableTransform
from db import db
from utils import row_dict_to_conversation_email

MODIFIERS = ['re:', 'fw:']

class EmailToThread(DiscoverableTransform):
    """
    Given a  maltego.ConversationEmail Entity, return a Email Thread from the Enron Dataset
    """

    @classmethod
    def create_entities(cls, request, response):
        subject = ' '.join(request.Value.split(' ')[:-1]).strip()
        for mod in MODIFIERS:
            if mod.lower() in subject[0:len(mod)].lower():
                subject = subject[len(mod):]
        subject = subject.strip()
        res = db.get_thread_by_subject(subject, limit=request.Slider)
        for d in res:
            ent = row_dict_to_conversation_email(d, response)
            ent.setLinkLabel("sent")