import datetime

class MessagerUser():

    user_detail = []
    messenger = []
    base_messager = """ Hi {name} ! 
    Thanks you for the purchase on {date}.
    We hope you are exited about using it . Just at a
    reminder purchase total was ${total}.
    Have a great one !
    @Sang lee <3
    """

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f"%(amount)
        detail = {
            "name": name,
            "amount": amount
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"] = email
        self.user_detail.append(detail)

    def get_details(self):
        return self.user_detail

    def make_messager(self):
        if len(self.user_detail) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_messager
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messenger.append(new_msg)
            return self.messenger
        return []

# obj = MessagerUser()
# obj.add_user("Sang", 125.2, email="sangitk41d@gmail.com")
# obj.add_user("July", 112.2)
# obj.add_user("Gon", 165.2)
# obj.add_user("Xuka", 178.6)
# obj.add_user("Xeko", 114.2)

#print(obj.user_detail)
#print("\n", obj.make_messager())

