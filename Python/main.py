from Fibonacci import Fibonacci

text = "The value of Fibonacci sequence {0} is {1}"

sequence = 5
value = Fibonacci().ValueOf(sequence)
print (text.format(sequence, value))

sequence = 10
value = Fibonacci().ValueOf(sequence)
print (text.format(sequence, value))