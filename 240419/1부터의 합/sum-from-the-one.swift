let input = Int(readLine()!)!
var sum = 0
var result = 0

for i in 1...100 {
    if sum >= input {
        break
    } else {
        sum += i
        result = i
    }
}

print(result)