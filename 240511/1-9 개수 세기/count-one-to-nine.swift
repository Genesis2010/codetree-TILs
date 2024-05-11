let input = Int(readLine()!)
var result = Array(repeating: 0, count: 10)

let input2 = readLine()!.split(separator : " ").map{Int($0)!}

input2.map{ result[$0] += 1 }

for i in 1..<result.count {
    print(result[i])
}