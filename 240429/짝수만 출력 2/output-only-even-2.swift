var input = readLine()!.split(separator: " ").map{Int($0)!}

while input[0] >= input[1] {
    if input[0] % 2 == 0 {
        print(input[0], terminator: " ")
    }

    input[0] -= 1
}