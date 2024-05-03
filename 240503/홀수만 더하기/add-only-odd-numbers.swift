let input = Int(readLine()!)!
var result = 0 
for _ in 0..<input {
    let num = Int(readLine()!)!

    if num % 2 == 1 && num % 3 == 0 {
        result += num
    }
}

print(result)