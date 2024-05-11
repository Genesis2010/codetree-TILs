let input = readLine()!.split(separator: " ").map{Int($0)!}
var result = Array(repeating: 0, count: 7) 

for i in input {
    result[i] += 1
}

for i in 1..<result.count {
    print("\(i) - \(result[i])")
}