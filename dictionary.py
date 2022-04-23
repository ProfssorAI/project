
tedad_kalamat = int(input()) # شمار کلمات داخل دیکشنری
mydictionary = {} 
for radif in range (tedad_kalamat):
   kalameh = input() # جملات ورودی بر اساس عدد دریافتی 
   kalameh = kalameh.split(' ') #جدا سازی کلمات و ریختن ان داخل لیست
   persian_w = kalameh[0] # ترجمه فارسی جمله
   translate = kalameh[1:] #کلمات با ترجمه خارجی
   for word in translate:
      mydictionary[word] = persian_w # {'i': 'man', 'je': 'man', 'ich': 'man'}
 
jomle = input() # جمله ای که باس ترجمه بشه
jomle = jomle.split(' ')
jomle_jadid = []

for kalameh in jomle:
   jomle_jadid.append(mydictionary.get(kalameh, kalameh)) #dictionary.get(keyname, value)
print(' '.join(jomle_jadid))

# output should be => man am kheili alaghemand in barnamenevisi