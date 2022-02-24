#Main Program: To get details from User (Name, AGe and booking confirmation)
#Madhan


def feedback(fname1):
    # feedback
    print("Hello {}, Please provide the feedback of the Booking Service".format(fname1))
    inpt = int(input("Enter 1-5 [1-low 5 High]: "))
    print("Thank you for providing your feedback {}".format(inpt))
    print()
    print()

lst=list()
for i in range(1,51):
    lst.append(i)
fname=list()
for j in range(1,51):
    fname.append(j)
lname=list()
for k in range(1,51):
    lname.append(k)
agep=list()
for i in range(1,51):
    agep.append(i)
r=1
while r==1:

    print("1.Book ticket")
    print('2.Cancel ticket\n')

    choice=int(input("\nEnter your option: "))

    if choice==1:
        tic=int(input('Enter seat no. (1-51 seats only)'))
        if lst[tic-1]==tic:
            fname1= str(input('Enter your first name \n'))
            lname1 = str(input('Enter your last name \n'))
            age1 = str(input('Enter your age \n'))
            lst.pop((tic-1))
            fname.pop(tic-1)
            lname.pop(tic - 1)
            agep.pop(tic - 1)
            lst.insert(tic-1,'B')
            fname.insert(tic - 1, 'fname1')
            lname.insert(tic - 1, 'lname1')
            agep.insert(tic - 1, 'age1')
            print('\n**************************')
            print("your ticket is booked ")
            print('**************************\n')
            feedback(fname1)
        else:
            print('\n**************************')
            print("seat is already booked try other seat")
            print('**************************\n')


    elif choice==2:
        tic=int(input('Enter seat no'))
        if lst[tic-1]==tic:
            print('\n**************************')
            print("This seat is not booked")
            print('**************************\n')
        else:
            lst.pop(tic-1)
            lst.insert(tic-1,tic)
            print('\n**************************')
            print("your ticket is cancelled")
            print('**************************\n')
    r=2
