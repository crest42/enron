import sqlite3


class EnronEmails(object):
    def __init__(self, conn):
        self.conn = conn

    def get_sent_emails(self, email, max_recipients=0, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        if max_recipients > 0:
            c.execute(
                """
                SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
                FROM emails inner join email_recipients using (email_id)
                WHERE email_id in (select email_id from (select emails.email_id, sender, recipient, count(*) as count from emails join email_recipients on email_recipients.email_id = emails.email_id where sender = ? group by emails.email_id) where count >= ?)
                GROUP BY email_id, subject, sender, date, file_path, body
                ORDER BY random()
                LIMIT ?;
                """, (email, max_recipients, limit,)
            )
        else:
            c.execute(
                """
                SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
                FROM emails inner join email_recipients using (email_id)
                WHERE sender = ?
                GROUP BY email_id, subject, sender, date, file_path, body
                ORDER BY random()
                LIMIT ?;
                """, (email, limit,)
            )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_personal_emails(self, email, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE email_id in (select email_id from (select emails.email_id, sender, recipient, count(*) as count from emails join email_recipients on email_recipients.email_id = emails.email_id where sender = ? group by emails.email_id) where count = 1)
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (email, limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_recieved_emails(self, email, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE recipient = ?
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (email, limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_person_from_mail(self, email, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE recipient = ?
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (email, limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_recipients_by_email(self, email, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE sender = ?
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (email, limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res
    
    def get_recipients_by_email_same_domain(self, email, limit=500):
        domain = email.split('@')[-1]
        c: sqlite3.Cursor = self.conn.cursor()

        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE sender = ?
            and recipient like ?
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (email, f'%@{domain}', limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_thread_by_subject(self, subject, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        #print(f'%: {subject}')
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE (subject like ? or subject = ?)
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (f'%: {subject}%', subject, limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

    def get_recipients_from_mail(self, email_id, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT recipient
            FROM email_recipients
            WHERE email_id = ?
            ORDER BY random()
            LIMIT ?;
            """, (email_id, limit,)
        )
        res = list(c.fetchall())
        return res

    def get_tlds_from_ppl(self, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT distinct top_domain from people
            ORDER BY random();
            """
        )
        res = list(c.fetchall())
        for i, d in enumerate(res):
            res[i] = '.' + str(d['top_domain'].split('.')[-1])

        return res[0:limit]
    def get_ppl_by_domain(self, domain, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email from people
            where domain = ?
            ORDER BY random()
            limit ?;
            """,
            (domain, limit)
        )
        res = list(c.fetchall())
        return res

    def get_domains_by_tld(self, tld, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT distinct top_domain from people
            where top_domain like ?
            ORDER BY random();
            """,
            (f'%{tld}',)
        )
        res = list(c.fetchall())
        return res[0:limit]

    def get_domain_from_top_domain(self, domain, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT distinct domain from people
            where top_domain = ?
            ORDER BY random();
            """,
            (domain,)
        )
        res = list(c.fetchall())
        return res[0:limit]

    def search_mails_by_phrase(self, phrase, limit=500):
        c: sqlite3.Cursor = self.conn.cursor()
        c.execute(
            """
            SELECT email_id, subject, sender, date, file_path, body, group_concat(recipient) as recipients
            FROM emails inner join email_recipients using (email_id)
            WHERE (subject like ? or body like ?)
            GROUP BY email_id, subject, sender, date, file_path, body
            ORDER BY random()
            LIMIT ?;
            """, (f'%{phrase}%', f'%{phrase}%', limit,)
        )
        res = list(c.fetchall())
        for d in res:
            d["recipients"] = d["recipients"].split(",")
        return res

db: EnronEmails = None


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def setup():
    global db
    import os
    loc = list(os.path.split(__file__)[:-1]) + ["enron_dedup.db"]
    path = os.path.join(*loc)
    #print(f"Using sqlite db at: {path}")
    conn = sqlite3.connect(path, check_same_thread=False)
    conn.row_factory = dict_factory
    db = EnronEmails(conn)
