#string are immutable
a = "!!!!! Jawad !!!!! !!!!!!Nafi!!!"
print(len(a))

print(a)

print(a.upper())

print(a.rstrip())

print(a.replace("Jawad", "Kazi Jawad"))

print(a.split(" "))

blogHeading ="my name is kazi jawadul islam" 
print(blogHeading.capitalize())

str1=" Jawad is my name"
print(str1.center(50,"-"))

str2 = '!!!! Hello Welcome to my blog !!!!'
print(str2.endswith("blog"))
print(str2.endswith("!!!!"))

str3='Banhladesh is a beautiful country'
print(str3.find("beautiful"))

str4='BanGladesHIsaBeautifulCountRy'
print(str4.isalnum())

str5='Bangladesh is a super country\n'
print(str5.isprintable())

str6='Bangladesh is a super country'
print(str6.isprintable())

repeat="Bangladesh is a beautiful country. Bangladesh is a democratic country.Bangladesh is mainly a riverian country"
print(repeat.count("Bangladesh"))

