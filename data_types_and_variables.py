from contextlib import nullcontext
from xmlrpc.client import boolean

print("Movies Rental")
# rent little mermaid for 3 days, Brother Bear for 5 days, hercules for 1 day
# how much have to pay, cost 3 dollar per day
Mermaid = 3
Brother_Bear = 5 
Hercules =1
print ("Total Day Rental:",Mermaid+Brother_Bear+Hercules,"Days")
print ("Total Cost $", 3*Mermaid+Brother_Bear+Hercules,)

# working as contractor for 3 companies: Google, Amazon, and Facebook.
# Which Google pays $400/hr, Amazon $380/hr, and Facebook $350/hr
# income for this week, 10 hr facebook, 6 hr google, and 4 hr Amazon
print ("Weekly Salary")
Google=480
Amazon=380
Facebook=350
print("Total Salary This Week $", Google*6+Amazon*4+Facebook*10)

# student can enroll if the class is not full or schedule is not conflict
full_class=0
schedule_conflict=0
print("Enrollment", bool(full_class))
print("Enrollment", bool(schedule_conflict))

def item():
    if item > 2:
        return ("offer applied")
    else:
        return ("This Offer can't apply")

username= 'codeup'
password = 'notastrongpassword'
def newp(password):
    if len(password)>5:
        return True
    if len(username)<20:
        return True
    if password!= username:
        return True
    else:
        return False
def newu(username):
    if len(password)>5:
        return True
    if len(username)<20:
        return True
    if password!= username:
        return True
    else:
        return False

print(newp("notastrongpassword"))
print(newu('codeup'))

