let input = readLine()!.split(separator: " ").map{Double($0)!}
print(input.reduce(0.0,+)/Double(input.count))