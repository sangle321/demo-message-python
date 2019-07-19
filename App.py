from Messager import MessagerUser
import datetime

obj = MessagerUser()

obj.add_user("Sang", 125.2, email="sangitk41d@gmail.com")
obj.add_user("July", 112.2)
obj.add_user("Gon", 165.2)
obj.add_user("Xuka", 178.6)
obj.add_user("Xeko", 114.2)

# print(obj.make_messager())

defaut_user = ["sang", "Jully", "Gon", "Xuka", "Xeko"]
defaut_amount = [125.2, 112.2, 165.2, 178.2, 114.2]
base_messager = """ Hi {name} ! 
    Thanks you for the purchase on {date}.
    We hope you are exited about using it . Just at a
    reminder purchase total was ${total}.
    Have a great one !
    @Sang lee <3
    """
def make_messagess(users, amounts):
    if len(users) == len(amounts):
        i = 0
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for user in users:
            user = user[0].upper() + user[1:].lower()
            new_amount = "%.2f"%amounts[i]

            new_msg = base_messager.format(
                name=user,
                date=date_text,
                total=new_amount
            )
            i += 1
            print(new_msg)

make_messagess(defaut_user,defaut_amount)