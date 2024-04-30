let input = readLine()!.split(separator: " ").map{Int($0)!}

print(Array(input[0]...input[1]).reduce(0, +))