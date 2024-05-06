let input = Int(readLine()!)!
var result = [Int]()

for i in 1...input {
    if i % 2 == 0 || i % 10 == 5 || (i % 3 == 0) && !(i % 9 == 0) {
        continue
    } else {
        result.append(i)
    }
}

result.map{ print($0, terminator: " ") }