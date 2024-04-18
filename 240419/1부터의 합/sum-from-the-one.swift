let input = Int(readLine()!)!
var sum = 0
var result = 0

for i in 1...100 {
    sum += i
    if sum >= input {
        print(i)
        break
    }
}