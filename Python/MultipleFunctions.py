class MultipleFunctions():

    def subfields():
        print("Subfields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
           
    
    def Oddeven():
        num= int(input("Enter a number:"))
        if(num%2!=0):
            print(num,"is Odd number")
        else:
            print(num,"is Even number")
    
    def Eligible():
        Gender=input("Your Gender:")
        age=int(input("Your age:"))
        Male="Male"
        Female="Female"
        Elg="Eligible"
        Nelg="NotEligible"
        if(Gender==Male):
            if(age>=21):
                print(Elg)
            else:
                print(Nelg)
                
        elif(Gender==Female):
            if(age>=18):
                print(Elg)
            else:
                print(Nelg)
        else:
            print("Not Eligible")
    
    def Percentage():
        subject1=int(input("Subject1:"))
        subject2=int(input("Subject2:"))
        subject3=int(input("Subject3:"))
        subject4=int(input("Subject4:"))
        subject5=int(input("Subject5:"))
        Total=subject1+subject2+subject3+subject4+subject5
        print("Total is:", Total)
        Percent=float((Total/500)*100)
        print("Percentage is:", Percent)
    
    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area=float((Height*Breadth)/2)
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth1:"))
        Perimeter=Height1+Height2+Breadth1
        print("Perimeter of Triangle:",Perimeter)