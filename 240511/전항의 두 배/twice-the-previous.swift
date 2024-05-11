var input = readLine()!.split(separator: " ").map{Int($0)!}

for i in 2...9 {
    input.append(input[i-1] + 2 * input[i-2])
}

print(input.map{String($0)}.joined(separator: " "))