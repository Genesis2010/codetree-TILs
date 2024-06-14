let input = readLine()!
let input2 = readLine()!

var firstNum = ""
var secondNum = ""

firstNum = input.filter { $0.isNumber }
secondNum = input2.filter { $0.isNumber }

print(Int(firstNum)! + Int(secondNum)!)