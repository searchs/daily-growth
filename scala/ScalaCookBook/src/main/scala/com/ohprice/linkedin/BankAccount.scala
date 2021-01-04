package com.ohprice.linkedin

object Account extends App {
  var c1 = new BankAccount("Sola", "Brookes", balance = 12300, acctType = "Checking")
  var c2 = new BankAccount("Duke", "Brakes", balance = 762300, acctType = "Savings")
  var c3 = new BankAccount("Moremi", "Douglas", balance = 36300, acctType = "Checking")
  println(c1)
  println(c2)
  println(c3)

}

class BankAccount(val fName: String,
                  val lName: String,
                  val balance: Double,
                  val acctType: String = "Savings") {

  val acctNumber:Int = BankAccount.nextAccNum()

  override def toString: String = "Account Name: " + customerName +
    "\nAccount Number: " + acctNumber +
    "\nAccount Type: " + acctType +
    "\nAccount Balance: £" + balance +
    "\n" + "=" * 65 + "\n"

  def customerName: String = fName + " " + lName

}

class Customer(val fName: String,
                  val lName: String)

object BankAccount {
  var accountNumber = 5000

  def nextAccNum() = {
    accountNumber += 1
    accountNumber
  }

}
