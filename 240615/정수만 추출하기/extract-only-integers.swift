let input = readLine()!.split(separator: " ").map{ String($0) }

var num1 = ""
var num2 = ""

for i in input[0] {
    if i.isNumber {
        num1 += String(i)
    } else {
        break
    }
}

for i in input[1] {
    if i.isNumber {
        num2 += String(i)
    } else {
        break
    }
}

print(Int(num1)! + Int(num2)!)