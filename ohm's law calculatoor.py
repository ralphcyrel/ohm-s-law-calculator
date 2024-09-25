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
#will ask the user to try again