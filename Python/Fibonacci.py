class Fibonacci:
    def ValueOf(self, sequence):
        if (sequence == 0):
            return 0
        elif (sequence == 1):
            return 1
        elif (sequence == 2):
            return 1
        else:
            return self.ValueOf(sequence-1) + self.ValueOf(sequence-2)

