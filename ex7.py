#Python exercise 7
total_bill = int(input("Total bill amount? "))
service_level = input("Level of service, which can be one of the following: good, fair or bad? ")
good = .20
fair = .15
bad = .10

if service_level == "good":
    total_tip = total_bill * good
    total_bill = total_bill + total_tip
    print("Tip amount ${:.2f} ".format(total_tip))
    print("Total amount ${:.2f} ".format(total_bill))

elif service_level == "fair":
    total_tip = total_bill * fair
    total_bill = total_bill + total_tip
    print("Tip amount ${:.2f} ".format(total_tip))
    print("Total amount ${:.2f} ".format(total_bill))

elif service_level == "bad":
    total_tip = total_bill * bad
    total_bill = total_bill + total_tip
    print("Tip amount ${:.2f} ".format(total_tip))
    print("Total amount ${:.2f} ".format(total_bill))
