let input = readLine()!.split(separator: " ").map{Int($0)!}
var result = 0
var count = 0

for (_, i) in input.enumerated() {
    if i >= 250 {
        break
    } else {
        result += i
        count += 1
    }
}

print(result, ceil(Double(result)/Double(count)))