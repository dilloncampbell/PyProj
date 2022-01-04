print("Employee Payroll Calculator")
emp = input("What is the first employee's name? ")
count = 0
while count <10:
  count +=1
  hours = float(input("Please Enter Hours worked: "))
  rate = float(input("Please Enter Rate of Pay: $"))
  if hours <= 40:
      grossPay = round(rate*hours, 2)
      fedTax = round(grossPay * .1, 2)
      stateTax = round(grossPay * .06, 2)
      fica = round(grossPay * .03,2)
      netPay = round(grossPay - (fedTax + stateTax + fica), 2)
      print("Employee Name: ", emp)
      print("Gross Pay: $", grossPay)
      print("Federal Taxes: $", fedTax)
      print("State Taxes: $", stateTax)
      print("FICA Taxes: $", fica)
      print("Net Pay $", netPay)
      emp = input("What is the next employee's name? ")

  else:
      regularPay = (rate*40)
      overTime = (hours-40)
      otRate = (rate*1.5)
      otPay = round(otRate*overTime)
      grossPay = round(regularPay+otPay)
      fedTax = round(grossPay * .1)
      stateTax = round(grossPay * .06)
      fica = round(grossPay * .03)
      netPay = round(grossPay - (fedTax + stateTax + fica))
      print("Employee Name: ", emp)
      print("Gross Pay: $", grossPay)
      print("Overtime pay: $",otPay)
      print("Federal Taxes: $", fedTax)
      print("State Taxes: $", stateTax)
      print("FICA Taxes: $", fica)
      print("Net Pay $", netPay)
      emp = input("What is the next employee's name? ")
  
    