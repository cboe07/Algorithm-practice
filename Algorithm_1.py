# DICTIONARY EXERCISES

phonebook_dict = {
	'Alice': '708-493-1834',
	'Bob': '857-384-1234',
	'Elizabeth': '484-584-2923'
}
# EXERCISE 1
print phonebook_dict['Elizabeth']

phonebook_dict.update({'Kareem': '938-489-1234'})
print phonebook_dict

del phonebook_dict['Alice']
print phonebook_dict

phonebook_dict.update({'Bob': '968-345-2345'})
print phonebook_dict

print phonebook_dict.values()

# EXERCISE 2: NESTED DICTIONARIES
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print ramit['email']
print ramit['interests'][0]
print ramit['friends'][0]['email']
print ramit['friends'][1]['interests'][1]

# EXERCISE 3 LETTER SUMMARY
def letter_histogram(word):
	histo = {}
	for i in word:
		if not histo.has_key(i):
			histo[i] = 1
		else:
			histo[i] += 1
	print histo 

user_word = raw_input("Please enter a word into histo: ")
letter_histogram(user_word)

EXERCISE 4 WORD SUMMARY
def para_histogram(paragraph):
    para_list = paragraph.split()
    histo = {}
    for i in para_list:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
           
    print(histo)

user_word = raw_input("Paragraph: ")
para_histogram(user_word)

BONUS CHALLENGE
def letter_histogram(word):
    lyst = word.split(" ")
    histo = {}
    for i in lyst:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
    return histo 

user_word = raw_input("Please enter a word: ")
histo  = letter_histogram(user_word)
chads_list = []
for key in histo:
    chads_list.append([key, histo[key]])
chads_list.sort(key = lambda x: x[1]) 
print chads_list[-1]
print chads_list[-2]
print chads_list[-3]

# print lyst
# print "1: " + lyst[-1][0], "\n2: " + lyst[-2][0] + "\n3: " + lyst[-3][0]

     OR
user_word = raw_input("Please enter a word: ")
histo  = letter_histogram(user_word)
yingrong_list = []
max_key = ""
new_dict = {}
while len(new_dict.keys() <=2):
	max_number = 0
	for i in histo:
		if histo[i] > max_number:
			max_number = histo[i]
			max_key = 1
	del histo[max_key]
	new_dict[max_key] = max_number
print new_dict

# SUPER BONUS CHALLENGE
list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,True,3,45,4,1,"The Beatles",9]

def final_dict(list):
	lyst = word.split(",")
	histo = {}
	for 















