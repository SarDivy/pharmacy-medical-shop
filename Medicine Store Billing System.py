#title
def title():
    print("((======= Medicine Store =======))")
title()
print()
#name input from customer
name=input("Customer Name:")
print()
#showing medicine menu.
def menu():
    print("((         MENU          ))\n1. Paracetamol = ₹50\n2. Cough Syrup = ₹120\n3. Vitamin C = ₹80\n4. Pain Relief = ₹150")

menu()
print()
#asking for medicine number with its quantity.
try:
    med_num=int(input("Write Medicine number:"))
    if med_num<=4 and med_num>=1:
        try:
            quantity=int(input("Enter Quantity of Medicine:"))
            print()
            #calculate bill
            if quantity>0:
                def bill(med_num,quantity):
                    if med_num==1:
                        return quantity*50
                        med_name="Paracetamol"
                    elif med_num==2:
                        return quantity*120
                        med_name="Cough Syrup"
                    elif med_num==3:
                        return quantity*80
                        med_name="Vitamin C"
                    elif med_num==4:
                        return quantity*150
                        med_name="Pain Relief"
                a=bill(med_num,quantity)
                print()
                age_cat=input("Are you a senior citizen?(yes/no):")
                if age_cat=="yes":
                    def bill_discount(a):
                        return a*5/100
                    b=bill_discount(a)
                else:
                    b=0
                def gst(a,b):
                    return (a-b)*5/100
                c=gst(a,b)
                final_bill=a-b+c
                if med_num==1:
                    med_name="Paracetamol"
                elif med_num==2:
                    med_name="Cough Syrup"
                elif med_num==3:
                    med_name="Vitamin C"
                elif med_num==4:
                    med_name="Pain Relief"
                print()
                #final report
                def report():
                    print("((         Report         ))")
                    print("Cuatomer:",name,)
                    print("Medicine:",med_name)
                    print("Quantity:",quantity)
                    print("Original Bill:","₹",a)
                    print("Discount:",b)
                    print("GST:",c)
                    print("Final Bill:",final_bill)
                report()
                    
            else:
                print("quantity must be more than 0")
        except ValueError:
            print("Quantity is must be in number format:")
    else:
        print("Entered Number is not present in menu")
except ValueError:
    print("medicine number must be in numeric format")
    
