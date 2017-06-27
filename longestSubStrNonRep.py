class Solution:
    # @param A : string
    # @return an integer
    
    def lengthOfLongestSubstring(self, A):
        s=A
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


        start = length = 0
        from collections import defaultdict
        d=defaultdict(int)
        for i in range(len(A)):
            if A[i]in d and start<=d[A[i]]:
                start = d[A[i]]+1
            else:
                length = max(length,i-start+1)
            d[A[i]]=i
        return length



a='adasdghhjkasgfhjagsjkfgahjsgdfjkasghdjyasfghjasgdhjasgdjashgdjas'
a='abcabcbb'
a='abcde'
a='iMik7M0zSLAdEwWmWNIZNH9s5tq5XBBPkReJ7bE4YzrW2aoCxflomFGdR56ihWppWcI8G4uf6GiZDcby5kkippUtnhfIQes3tZtXnvGu6DTVf0qpAZm1mg5oBpRVIPEo2SHfvPCOV9LpBSP16eUJqZEMvhO8A9wcQxLuHcGJLp5eedZCd0r6K4ugkAtMiDwQpOmTJnGJDkf5kPeZfAbVgbqPrXHE9BC7heCu3PFG3ss1A3uoQpIGAmirlATMYWqeFh8KE9cHZ9rjQOArNVCRhzkQye6JsmIwgN33LqmKCdfc5VJmq95aulgYq4rvBqekUN7zkX9DwZRg2huLDlRtmfycepV0YV0503hB0TGJ14fs8SHfiKuzqi6Lzx1n47jl7nDybGQB8XxfQgpHn00qjaOWU6WsOlqeQftCgXnEX1vQDdJqyK5t90KcyK4LVupxv4zoSEdvlxlEzJcuBesFAqBIxkCTn9I1Wu2p55ItcAyXUuT1QzrIVFynvYvvkh5q72kBhXf8mqX6ZF0mN3uILfNuoXbI5iwdRbCx1wTHEwTKWwDnHXCQTh7sCt5PSlqhnHcyJUb1K2piBXBsVOCa0c1A09GQOs6ubIWfmuq4ZeJtmwGCFKv70W5y2HdjjHWoYMWycPLsHupk2aA6tlEQuOpGMrUW1fJBxuyQt7E9KLScvQ9qaXApddKqCj8ciZfyLPzyvUqfmKGrLDovRDFspT5ubjUMVeYZ742bAq0ELuDsXs67FyR1Kk2eULAKplkWRdNBQq1amSTcSMoW8cOWkiyv5zQ12hR2zmMDBxTTGXy8u8Tlur9dQnXu5SwAqsCpAOxkSNeRqzk7Iy05wUHnexylXyZyH2NSKu0YM5GcWxoPyS9hVayjYtWdeJ1z47w74J05xZZ4oM2l0rDgv9oQCKyhhPt3LVF6P6OGetqNcEqMRd3TQlxwyyC35d6Y6daRGlmv8zMcvHoC0aUlSM9eXQUfM5q9PFkWZLQspceuW2TuXbgeQsfhLwlBZ126oa7qNldkDmV9MgK5nqBs2n7MCnrcgsvRwI0QoYPZjOr9TWLmbImBZohHb0ks07qlchr9J5lx9bXdszPIS0zetGJ4b1O1Ad92V9r17EGS7kNwmsWNyL7R6XUN4HvJv2NQFQRide2fpX1HV2C4HDZNOj2rLVOzjAkB0IQuHts7aW8JwJbGMS9PD1RjsA7FPX1cYHpvFV5S45zkFhirRdXjBGS67GmNiNrDZaMSPMxf267eEIveFDSnqoDNAHpXFywGT9LSu2aQ6rLCZD0vDkOrIY9OBiJ13VBygWqOFx6p84wBfoQwE3UHvGOB4HiJjPxqGAA3WRCSO4fECvnKcMfy2mj1YUR2gVeMyBWUAcbTuobmpPMe7P3goNSqwC8fLUFhHrgcnlxHBhH9C1A17X9fYzZASmibYRhFlIh4LQAFwQUIDBmYzAmZ6Ql3yqmrnMEjsPdbkcjPy3hHXkehx3fp1I5dNmnvZx2ravEewm82vHOYOVnBbrsmQszujfWqzVJCepOlgNcnEdqD1D8h5pVraLvDql5jzrsFUHujVtL3qjO7p6WFe513KOfUhhmYk8KHNSPvDFrw6bXZvdNb0ZogkkSgQI3AjdmpJgzY3DSR6UmCRnehczTZJuZzEAJEVfy2AwI5JdIEmrEzWjfSfP8jTgHAJ9GKXaar1KdimLh85G9KEkFeCG8YTj0OtTvdkcH9FoN6iZEKmqp958j2TGfSKGYi8xBOQZeNdbslst363abrVBIasRzMIY948BaH9INr'
a='WC8PE9ZRdHIu0niQOS2uuGdSUPOKSmjLcbP1cVtfXAuTASSWcnkaw5fo4LLWJASNGHP6zWy8yus8419dZ9qDxN8wOEgqxkURrRcE1JCF5IZoDOlJTTCQ3WrRN1qgQJU19eXdRNQ5J1nK1C5KnkO8HYSnmC66gdyy9bLmycdLQhFGFBCe0j2TKoGjaTYJxWRqB'
a='adhirchmondal'
print Solution().lengthOfLongestSubstring(a)