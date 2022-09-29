class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        pass

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member")

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Not enough points")


colby = User("Colby", "Leed", "colbyleed@yahoo.com", 35)

colby.display_info()

colby.enroll()

colby.spend_points(50)

colby.display_info()

colby.enroll()

leanne = User("LeAnne", "Leed", "leanneleed@gmail.com", 37)

leanne.display_info()

leanne.enroll()

leanne.spend_points(80)

leanne.display_info()

danny = User("Danny", "Olshefsky", "dolshefsky@yahoo.com", 35)

danny.display_info()

danny.spend_points(40)
