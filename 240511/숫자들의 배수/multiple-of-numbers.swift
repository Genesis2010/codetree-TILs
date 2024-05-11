let input = Int(readLine()!)!
var count = 1
var drainage5 = 0
var result = input

while true {
    print(result, terminator: " ")

    if result % 5 == 0 {
        drainage5 += 1
        if drainage5 == 2 {
            break
        }
    }

    count += 1
    result = input * count
}