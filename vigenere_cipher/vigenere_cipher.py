class VigenereCipher(object):
    '''Encoding and Decoding the Vigenere Cipher'''

    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p_text, k_word in zip(plaintext, keyword):
            cipher.append(combine_character(p_text, k_word))
        return "".join(cipher)

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def decode(self, cyphertext):
        plain = []
        keyword = self.extend_keyword(len(cyphertext))
        for c_text, k_word in zip(cyphertext, keyword):
            plain.append(separate_character(c_text, k_word))
        return "".join(plain)


def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)
