class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        liste = []  
        final_liste = [] 
        for i in range (len(nums)) :   
            if nums[i] ==  key :   
                liste.append (i)   
        for i in range (len(nums))  :   
            for j in range (len(liste)) :   
                if abs (liste[j] - i )  <= k  :   
                    final_liste.append(i)   
                    break    
        return  final_liste