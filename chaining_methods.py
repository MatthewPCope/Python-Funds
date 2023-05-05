class User:
    def __init__(self, first, last, age, email):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self): #when called it'll display the user's info
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"email: {self.email}")
        print(f"member: {self.is_rewards_member}")
        print(f"points: {self.gold_card_points}")
        print("<><><><><><><><><>")
        return self
    def enroll(self): #when called the user will get enrolled in the rewards program and get 200 points
        if self.is_rewards_member == True: # if they're already a member, it'll tell them they're already a member
            print(f"{self.first_name}, you are already a member, good job!")
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount): #this allows the user to spend their points
        if self.gold_card_points <= amount: # if you try to spend more points than you have, it'll tell them they don't enough and not deduct any points
            print(f"{self.first_name}, you've dont have enough points.  Keep saving!")
            return
        self.gold_card_points -= amount
        return self
user_Matt = User("Matt", "Cope", 39, "matthew.p.cope@gmail.com") #new user instances created
user_Jen = User("Jan", "Banzian", 41, "janbanzian@gmail.com") 
user_Mark = User("Mark", "Smith", 40, "msmith@gmail.com")
user_Matt.display_info().enroll().spend_points(50).display_info().enroll() #chained all these methods together
user_Jen.display_info().enroll().spend_points(80)
user_Mark.enroll().display_info().spend_points(300)







