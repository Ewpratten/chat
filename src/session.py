
class Session(object):
    username: str
    uid: str
    secret: str

    conn = None
    mark_disconn = False

    def send(self, text: str):
        try:
            self.conn.send(text.encode() + b"\n\r")
        except:
            self.mark_disconn = True