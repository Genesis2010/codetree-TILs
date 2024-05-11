let input = readLine()!.split(separator: " ").map{Int($0)!}

var result = Array(repeating: 0, count: 10) 

for i in input {
    if i == 0 {
        break
    }
    result[(i/10)-1] += 1
}

for (index, value) in result.enumerated().reversed() {
    print("\((index+1)*10) - \(value)")
}