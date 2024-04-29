let input = Int(readLine()!)!

var i = 1 

while i <= input {
    if i % 3 == 0 {
        print(i, terminator: " ")
    }

    i += 1
}