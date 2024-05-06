let input = Int(readLine()!)!
var count = 0

for i in 1...input {
    if (i % 2 == 0) || (i % 3 == 0) || (i % 5 == 0) {
        continue
    } else {
        count += 1
    }
}

print(count)