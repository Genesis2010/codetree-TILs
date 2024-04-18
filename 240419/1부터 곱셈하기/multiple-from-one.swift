let input = Int(readLine()!)!

var result = 1

for i in 1...10 {
    result *= i

    if result >= input {
        print(i)
        break
    }
}