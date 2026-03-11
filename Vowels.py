#To Count Vowels

sentence=input("Enter any string: ")
sentence=sentence.lower()
vowel_count=0
vowels="a e i o u A E I O U"
count=[i for i in sentence if i in vowels]
print("total vowel count: ",len(count))
