var result = 0

for _ in 0..<10 {
    if Int(readLine()!)! % 2 == 1 {
        result += 1
    }
}

print(result)