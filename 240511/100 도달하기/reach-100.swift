let input = Int(readLine()!)!
var i = 2
var result = [1, input]

while true {
    let sum = result[i-1] + result[i-2]
    result.append(sum)

    if sum > 100 {
        break
    }

    i += 1
}

print(result.map{String($0)}.joined(separator: " "))