let input = Int(readLine()!)!
let num = readLine()!.split(separator: " ").map{Int($0)!}

num.filter { $0%2 == 0 }.forEach { print($0, terminator: " ")}