class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # bulls=0
        # cows=0
        # freq={}
        # freq2={}
        # for i in secret:
        #     # s.add(secret[i])
        #     if i in freq:
        #         freq[i]+=1
        #     else:
        #         freq[i]=1
        # for i in guess:
        #     # s.add(secret[i])
        #     if i in freq2:
        #         freq2[i]+=1
        #     else:
        #         freq2[i]=1
        # for i in range(len(secret)):
        #     if secret[i]==guess[i]:
        #         bulls+=1
        #         freq[secret[i]]-=1
        #         freq2[guess[i]]-=1
        
        #     elif guess[i] in secret and freq[guess[i]]==freq2[guess[i]]:
        #         # print(freq)
        #         cows+=1
        #         freq[guess[i]]-=1
        #         freq2[guess[i]]-=1
                
        # return str(bulls)+'A'+str(cows)+'B'
        bulls = 0
        cows = 0
        secret_dict  = {}
        guess_dict  = {}
        
        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1
            else:
                secret_dict[i] = secret_dict.get(i, 0) + 1
                guess_dict[j] = guess_dict.get(j, 0) + 1
        for i in secret_dict:
            if i in guess_dict:
                cows += min(secret_dict[i], guess_dict[i])
        return f"{bulls}A{cows}B"
            
            
            
        