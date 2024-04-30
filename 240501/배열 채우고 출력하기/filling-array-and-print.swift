let input = readLine()!.split(separator: " ").map{String($0)}

for i in input.reversed() {
    print(i, terminator: "")
}