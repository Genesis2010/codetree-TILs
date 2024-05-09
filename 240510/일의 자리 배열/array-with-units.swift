let input = readLine()!.split(separator: " ").map{Int($0)!}
var result = [input[0], input[1]]


for i in 0..<10 {
    if i > 1 {
        result.append((result[i-1] + result[i-2]) % 10)
    }

    print(result[i], terminator: " ")
}