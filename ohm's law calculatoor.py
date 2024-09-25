#will ask the user for calculation Voltage, Current or Resistance
while True:
    ohms_law = input("Type '1' if you want to solve for Voltage"
                    "\nType '2' if you want to solve for Current"
                    "\nType '3' if you want to solve for Resistance: ")
#will ask the user to input with respect to user choice
    if ohms_law == '1':
        current = float(input("Enter current: "))
        resistance = float(input("Enter resistance: "))
        voltage = current * resistance
        print("The Voltage is {voltage} Volts".format(voltage=voltage))
    elif ohms_law == '2':
        voltage = float(input("Enter voltage: "))
        resistance = float(input("Enter resistance: "))
        current = voltage / resistance
        print("The current is {current} A".format(current=current))
#will ask the user to try again