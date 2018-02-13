class Person:
    def __init__(self, name, email, phone, friends=[], greeting_count=0, unique_greeted={}):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = greeting_count
        self.unique_greeted = unique_greeted

    def __str__(self):
        return "Person: {} {} {} Friend Count: {} Greeting Count: {} Unique Greeted: {}".format(self.name, self.email, 
        self.phone, len(self.friends), self.greeting_count, len(self.unique_greeted))

    def greet(self, other_person):
        print("Hello {}, I am {}!".format(other_person.name, self.name))
        self.greeting_count += 1
        
        self.unique_greeted[other_person] = "Greeted"
        
        #unique_greeted_length = len(self.unique_greeted)


    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print("{} friend count : {} ".format(self.name, len(self.friends)))

    def print_greeting_count(self):
        print("{} greeting count: {}".format(self.name, self.greeting_count))

    def num_unique_people_greeted(self):
        print(len(self.unique_greeted))

# Add's Sonny to list of people 
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", [], 0, {})
# Add's Jordan to list of people
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", [], 0, {})

sonny.greet(jordan) # Sonny greets Jordan
print("Sonny greeting count: {}".format(sonny.greeting_count)) # Counts amount of times Sonny greeted Jordan
jordan.greet(sonny) # Jordan greets Sonny
print("Jordan greeting count: {}".format(jordan.greeting_count)) # Counts amount of times Jordan greeted Sonny

sonny.print_contact_info()
jordan.print_contact_info()

jordan.add_friend(sonny)    # Jordan adds Sonny as a firend
sonny.add_friend(jordan)

jordan.num_friends()    # Displays friend count for Jordan
sonny.num_friends()     # Displays friend count for Sonny

sonny.greet(jordan)
sonny.greet(jordan)
sonny.print_greeting_count()

jordan.greet(sonny)
jordan.print_greeting_count()

mike = Person("Mike", "Mike@hotmail.com", "473-285-4918", [], 0, {})
tom = Person("Tom", "Tom@hotmail.com", "435-345-2112", [], 0, {})

mike.greet(jordan)
mike.greet(tom)
tom.greet(mike)
tom.greet(mike)

jordan.add_friend(mike)

jordan.greet(mike)
jordan.greet(tom)

jordan.add_friend(mike)
mike.add_friend(jordan)

print(sonny)
print(jordan)
print(mike)
print(tom)

jordan.num_unique_people_greeted()