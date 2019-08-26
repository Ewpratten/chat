
class Session(object):
    username: str
    uid: str
    secret: str

    conn = None

    def send(self, text: str):
        self.conn.send(text.encode() + b"\n\r")