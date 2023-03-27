import json 
shift = 11
text = "the quick brown fox jumped over the lazy dog"
results = ""
#file_pointer= open("encript.txt", "x")
def caeser_cipher(text, shift):

    """

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """
    result = ""
    for char in text:
        if char.isalpha():
        # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
        # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start * shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
            result += char
            #results.append(result)
            #print(results)
    return results

def main():
   file_pointer = open("ch06\exercises\encripted.txt", "w")
   result = caeser_cipher(text, shift)
   results = []
   results.append(result)
   for i in results:
       file_pointer.write(i)
       file_pointer.close()
       print('done')
       return None


main()
#caeser_cipher(text, shift)

