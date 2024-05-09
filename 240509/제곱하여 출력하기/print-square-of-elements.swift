import Foundation

let input = Int(readLine()!)!

var num = readLine()!.split(separator: " ").map{Int($0)!}

for i in num {
    print(pow(Decimal(i), 2), terminator: " ")
}