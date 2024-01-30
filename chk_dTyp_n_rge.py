# tic tac toe
print("validate user input data ")


def user():
    choice = ("wrong")
    while choice.isdigit() == False: #condition wher ewe want to stop here we want to stop at when we get choise.isdigit true
        choice = input("Enter no. should be in 0 to 10")
        if choice.isdigit() == False:
            print("oops? wrong input")
    return int(choice)


#way to check in range of 0  to 10
def user():
    choice = ("wrong")
    withinrange=False
    acceptedRange=[0,11]

    while choice.isdigit() == False or withinrange: #condition wher ewe want to stop here we want to stop at when we get choise.isdigit true
        choice = input("Enter no. should be in 0 to 10")
        # check dataType
        if choice.isdigit() == False:
            print("oops? wrong input")

        #     right dateType  but what if wrong range
        if choice.isdigit()==True:
            # check range
            if int(choice)in acceptedRange:
                withinrange=True
            else:
                print("out of range bro")
                withinrange=False
    return int(choice)

def check_d_n_range():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice = input("pick a position (0,1,2):")
        if choice not in ['0','1','2']:
            print("sorry invalid choice")
    return int(choice)


the_list = [1, 2, 3]


def disp():
    print("here the list")
    print(the_list)


def check_d_n_range():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("pick a position (0,1,2):")
        if choice not in ['0', '1', '2']:
            print("sorry invalid choice")
        return int(choice)


def position_choice():
    choice = 'wrong'
    while choice not in ['1', '2', '3']:
        choice = input("pick (0 1 2)")
        if choice not in ['0', '1', '2', '2']:
            print("invalid")
    return int(choice)


def replace_with_given_no(the_list, position):
    user_no = input("tyep whatever ")
    the_list[position] = user_no
    return the_list


def game_working_with_fn():
    choice = 'wrong'
    while choice not in ['y', 'n']:
        choice = input('y:keep playing/n'
                       'n:quit')
        if choice not in ['y', 'n']:
            print("sorry wrong input")
    if choice == 'y':
        return True
    else:
        return False



