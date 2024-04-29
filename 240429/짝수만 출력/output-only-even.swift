let input = readLine()!.split(separator: " ").map{Int($0)!}
var count = input[0]
while count <= input[1] {
    if count % 2 == 0 {
        print(count, terminator: " ")
    }

    count += 1
}