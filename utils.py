def row_dict_to_conversation_email(d, response):
    ent = response.addEntity(
        "maltego.ConversationEmail", f'{d["subject"]} [#{d["email_id"]}]'
    )
    ent.addProperty(fieldName="email_id", displayName="Email ID", value=d["email_id"])
    ent.addProperty(fieldName="email", displayName="Sender Email", value=d["sender"])
    ent.addProperty(fieldName="email.recipients", displayName="Recipient Emails", value=d["recipients"])
    ent.addProperty(fieldName="timestamp", displayName="Time Sent", value=d["date"])
    ent.addProperty(fieldName="path", displayName="File Path", value=d["file_path"])
    ent.addProperty(fieldName="content", displayName="Content", value=d["body"])
    return ent


def row_dict_to_email_address(d, response):
    ent = response.addEntity(
        "maltego.EmailAddress", d["email"]
    )
    ent.addProperty(fieldName="domain", displayName="Domain", value=d["domain"])
    ent.addProperty(fieldName="topdomain", displayName="Top Domain", value=d["top_domain"])
    ent.addProperty(fieldName="name", displayName="Name", value=d["name"])
    return ent
