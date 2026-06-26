words1 = "Hello World"
words2 = "   fly me   to   the moon "
words3 = "luffy is still joyboy"


def lengthOfLastWord(s):
    lastWord = 0
    for i in range(len(s)):
        if s[i].isalpha():
            lastWord += 1
        try:
            if s[i+1] == " " and s[i+2].isalpha():
                lastWord = 0
        except IndexError:
            pass

    print(lastWord)


lengthOfLastWord(words1)
lengthOfLastWord(words2)
lengthOfLastWord(words3)


# I SHOULD HAVE REVERSED THE LIST IN THE FOR LOOP THEN FIN THE LENGTH OF THE FIRST WORD!!!
