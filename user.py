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
    def enroll(self): #when called the user will get enrolled in the rewards program and get 200 points
        if self.is_rewards_member == True: # if they're already a member, it'll tell them they're already a member
            print(f"{self.first_name}, you are already a member, good job!")
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self, amount): #this allows the user to spend their points
        if self.gold_card_points <= amount: # if you try to spend more points than you have, it'll tell them they don't enough and not deduct any points
            print(f"{self.first_name}, you've dont have enough points.  Keep saving!")
            return
        self.gold_card_points -= amount
user_Matt = User("Matt", "Cope", 39, "matthew.p.cope@gmail.com") #created a new instance of a user named Matt
user_Matt.enroll() #Matt gets enrolled and gets 200 points
print(user_Matt.is_rewards_member) #testing Matt's enrollment
user_Matt.spend_points(50) # Matt spent 50 points
print(user_Matt.gold_card_points) # checking Matt's spend points
user_Jen = User("Jen", "Benzian", 41, "jenbenzian@gmail.com") #created a new user instance named Jen
user_Mark = User("Mark", "Smith", 40, "msmith@gmail.com") #created a new user instance named Mark
user_Jen.enroll() #enrolled Jen
user_Mark.enroll() # enrolled Mark
user_Jen.spend_points(80) #jen spends 80 points
user_Jen.display_info() #displaying user info
user_Mark.display_info() #displaying user info
user_Matt.display_info() #displaying user info
user_Mark.spend_points(300) #Mark spent 300 points which is too many
print(user_Mark.gold_card_points) #Mark didn't have enough points so he stays at his current amount which is 200
user_Matt.enroll() # tried to re-enroll Matt but he's already a member
