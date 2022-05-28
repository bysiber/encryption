#This algorithm converts each letter of the entered text into a unique hash.
from hash import hash_MD5

tr_s = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
tr_b = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
spcs = [" ","/","\\",":","*","_","-",".",",","#","`","'","^","<",">","$","{","}","[","]","|","%","+","-","&","(",")","="]
CHARACTERS = tr_s + tr_b + nums + spcs

class MD5BC(): # MD5 BASİC CRYPTOR
    def __init__(self,chars,privateKey):
        self.privateKey = privateKey #This key must be safeguarded
        self.PHash = hash_MD5(self.privateKey)
        self.chars = chars

    def findIndex(self,chr):
        counter = 0
        for ichr in self.chars:
            if ichr == chr:
                return counter
            counter += 1
        return -1



    def encrypt(self,data):
        encryptedData = ""
        hashCounter = 1 #hashCounter range -> (1,length of data)
        for dt in data:
            #you need to use hashCounter, if you add hashCounter , frequency analysis won't work
            ptxt = str(hashCounter) + self.privateKey + dt 
            hashTxt = hash_MD5(ptxt)
            encryptedData += hashTxt + "\n"
            hashCounter += 1
        return encryptedData

    def decrypt(self,hashes):
        decryptedData = ""
        hashCounter = 1
        hashList = hashes.split('\n')
        for hash in hashList:
            hKey = str(hashCounter) + self.privateKey
            for chr in self.chars:
                if hash_MD5(hKey + chr) == hash:
                    decryptedData += chr
            hashCounter += 1

        return decryptedData





if __name__ == "__main__":
    pKey = "jhA8hs8UA82LKAmX9ajs821Jx"
    bcryptor = MD5BC(CHARACTERS,pKey)
    hashes = bcryptor.encrypt("feel")
    print("from letters of text to hashes:\n",hashes)
    print("from hashes to text:\n",bcryptor.decrypt(hashes))



