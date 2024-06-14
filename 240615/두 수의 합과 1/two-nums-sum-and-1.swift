let input = readLine()!.split(separator: " ").map { Int($0)!} 

let sum = String(input[0] + input[1])

print(sum.filter{ $0 == "1" }.count)