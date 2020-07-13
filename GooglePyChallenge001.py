def solution(message):
    acsending = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    descending = ("z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a")
    result = ""
    
    for alphabet in message:
        if (alphabet.isalpha() and alphabet.islower()):
           result += descending[acsending.index(alphabet)]
        else:
            result += alphabet
    
    return result


print(solution("vmxibkgrlm"))
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
print(solution("123567"))