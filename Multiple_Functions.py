class multipleFunctions():
    def oddEvent():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even Number")
            result="Even Number"
        else:
            print("Odd Number")
            result="Odd Number"
        return result
        
    def BMI():
        weight=int(input("Enter your Weight:-"))
        if(weight>0 and weight<20):
            print("Underweight")
            Msg="Underweight"
        elif(weight>=20 and weight<25):
            print("Normal Weight")
            Msg="Normal Weight"
        elif(weight>=25 and weight<30):
            print("Overweight")
            Msg="Overweight"
        elif(weight>=30 and weight<35):
            print("Moderately obese")
            Msg="Moderately obese"
        elif(weight>=35 and weight<40):
            print("Severely obsere")
            Msg="Severely obsere"
        else:
            print("Very sererely obsese")
            Msg="Very sererely obsese"
        return Msg

    def AI_SubFields():
        print("Sub-Fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")   

    def MarriageElegible(Gender,Age):
        if Gender=="Male":
            if Age>=22:
                print("Gender= Male, Age=",Age,"Your are Eligible to marriage")
            else:
                print("Gender= Male, Age=",Age,"Your are not Eligible to marriage")
        else:
            if Age>=18:
                print("Gender= Female, Age=",Age,"Your are Eligible to marriage")
            else:
                print("Gender= Female, Age=",Age,"Your are not Eligible to marriage")  

    def CalculateMark1():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total: ",total)
        per=total/500*100
        return per