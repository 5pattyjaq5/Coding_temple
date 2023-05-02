#question 1 :
def user(user_name):
    print(F'hello_{user_name}')

i = input("What is you name?")
user(i)

#Question 2
def first_odds():
    for value in range(101):
        if value % 2!= 0:
            print(value)


first_odds()


#Question 3 
def max_num_in_list(a_list):
    



# Question 4
def is_leap_year(a_year):





#Question 5
def is_consecutive(a_list):
    for index_position in range(len(a_list)-1):
        if a_list[index_position] <a_list[index_position + 1]:
            return True
        

a_list = {1,2,3}

