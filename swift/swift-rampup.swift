import UIKit

//comments
var str: String = "Allo, Ola!"
/**
 Multiline comments
 */
str = "Mully Box"

let houseNumber:Int64 = 20

str.uppercased()

str.split(separator: " ")
houseNumber.hashValue

//Constants
let surname = "Ajibode"

//cannot re-assign value to constant
//surname = "Ajibowo-Increase"

var rate: Float = 0.25 //Float has less accuracy than Double [Float: 32 bits, Double: 64 bit system]
//Swift: Double is inferred type
var cash = 83000

Int.max

var nums = 185

if nums <= 100 {
    print("Number = \(nums).")
} else {
    print("\(nums) does not meet the condition")
}

var a = 12.5
var t: Float = 90.03

var res = a + Double(t)

Double(16/3)


//IF ELSE + TERNARY OPERATOR
var tempF = 32
var isFreezing: Bool = true

if tempF == 32 {
    print("freezin temp!")
    isFreezing = true
}else if tempF < 32 {
    isFreezing = true
} else {
    isFreezing = false
    print("Temp is ok man!")
}

//ternary
isFreezing = tempF <= 32 ? true : false
var comment: String = tempF <= 32 ? "It is really freezing": "Common man! Not even Cold!"

var number = 1

var numStr = "one"

switch number {
case 0:
    numStr = "zero"
case 1:
    numStr = "one"
case 2:
    numStr = "two"
default:
    break
}

var sentence = "The number is \(numStr)."


//FOR LOOPS

for x in 0...10 {
    print("x is \(x).")
}

var y = 0

while y <= 9 {
    print("y is now equal to \(y)")
    y += 1
}

var g = -3
repeat {
    print("Nums: \(g)")
    g += 1
} while g <= 3


var states = ["DK":"Dakota",
              "NY":"New York",
              "DV":"Devon",
              "OT":"Ottawa"]


for(k,v) in states {
    print(k,v)
}


//FUNCTIONS
func greeting(name: String) -> String  {
    return "Allo \(name)"
}

greeting(name: "Holly")

//ARRAYS

var cars = ["Benz", "BMW", "Beetle", "Volvo", "Skoda", "Fiat"]
cars.count
cars.append("Tesla")
var counts = cars.count
//cars.insert("Jaguar", 8)
print(cars)
var emptyDict = [String:String]()

emptyDict["NY"] = "New York"
print(emptyDict)
emptyDict["NY"] = nil
print(emptyDict)
emptyDict["PA"] = "Pennysylavania"

states.updateValue("London", forKey: "OT")

print(states)


//SET

var teams : Set<String>

var myBills: Set = ["electricity", "water", "internet", "water"]
var ints: Set = [1,2,3]

//TUPLES
var products = [123: "Bananas", 234: "Apples", 345: "Pears", 456: "Agbalumo"]

for(sku, product) in products { //the (sku, product) is a Tuple
    print("The SKU for \(product) is \(sku)")
}

var mac = ("MacBook Pro", 2015 )
print(mac.0)
print(mac.1)


var laptop = (model: "Thin Machine", year: 2019)
print(laptop.model)
print(laptop.year)


func getCarDetails() -> (model: String, topSpeed: Int, isConvertible: Bool) {
    let model = "Camaro"
    let topSpeed = 145
    let isConvertible = true
    
    return (model, topSpeed, isConvertible)
}


var camaro = getCarDetails()

print(camaro.model)
print(camaro.topSpeed)
print(camaro.isConvertible)


//OPTIONALS
var score: Int?
score  = 21

//forced unwrapping
print("The Score is currently \(score!).")


if score != nil {
    print("Force Unwrapping: The score is currently \(score!)")
} else {
    print("Could not get the score")
}

// optional binding
if let confirmedScore = score {
    print("Optional Binding: The score is currently \(confirmedScore)")
} else {
    print("Could get the current score.")
}


//import Foundation


