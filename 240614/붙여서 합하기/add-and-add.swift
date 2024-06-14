let input = readLine()!.split(separator: " ").map{ String($0) }

let ab = input[0] + input[1]
let ba = input[1] + input[0]

print(Int(ab)! + Int(ba)!)