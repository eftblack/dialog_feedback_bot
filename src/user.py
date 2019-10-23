class User:
    def __init__(self, id_, name=None, surname=None, org=None):
        self.id_ = id_
        self.name = name
        self.surname = surname
        self.org = org
        self.last_key = ""
        self.lock_msg = False

    def is_full_profile(self):
        if self.id_ and self.name and self.surname and self.org:
            return True
        return False

    def form(self):
        return "{0} {1}\n" \
               "{2}\n".format(self.name, self.surname, self.org)

    def filling_data(self, last_key, data):
        if last_key == "hello" or last_key == "second_name":
            self.name = data
        elif last_key == "surname" or last_key == "second_surname":
            self.surname = data
        elif last_key == "org":
            self.org = data
