let input = readLine()!.split(separator: " ").map{Int($0)!}

for i in input {
    if i == 0 {
        break
    }

    if i % 2 == 0 {
        print(i/2, terminator: " ")
    } else {
        print(i+3, terminator: " ")
    }
}