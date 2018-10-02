data = input('> ')

'''
data = [['a', 'b', 'c', 'd'], ['aaaaaaaaaa', 'b', 'c', 'qwa'], ['a', 'bbbbbbb', 'c', 'woop'], ['asdas', 'qweqw', 'c', 'd']]

widths = [max(map(len, col)) for col in zip(*data)]
for row in data:
	print("  ".join((val.ljust(width) for val, width in zip(row, widths))))

a           b        c  d   
aaaaaaaaaa  b        c  qwa 
a           bbbbbbb  c  woop
asdas       qweqw    c  d  

PP KbrKbr ee BB DD slsl AyAy Ssi mm rr tt cecw gg UU lala stmagi agispd Hh HH Hh HH Hh HH HH HH Hh HH Hh HH HH HH HH Hh HH Hh HH HH Hh HH HH Hh
PP KbrKbr ee BB DD slsl AyAy SS mm rr tt Cce gg UU lala agicha spdspd HH HH HH HH HH HH HH Hh Hh Hh Hh Hh HH HH Hh Hh HH Hh HH HH Hh HH HH HH
PP KbrKbr Ee BB DD slsl AyAy Ssi mm rr tt Ccw gg UU Lla agicha stmstr HH Hh Hh Hh Hh HH HH HH Hh Hh HH HH Hh Hh Hh Hh HH Hh HH HH Hh HH Hh Hh
PP KbrKbr Ee BB DD slsl AyAy SS mm rr tt cchce gg UU Lla chaagi intspd HH HH HH HH HH HH Hh Hh Hh Hh HH HH HH HH Hh HH HH HH HH HH HH HH Hh Hh
PP KbrKbr ee BB DD slsl AyAy SS mm rr tt Cce gg UU lala chacha spdcha HH HH HH HH HH HH Hh Hh HH HH HH HH Hh HH HH HH Hh Hh Hh Hh Hh HH HH Hh
PP KbrKbr ee BB DD slsl AyAy SS mm rr tt cchce gg UU Lla spdagi intstm HH Hh HH HH HH HH Hh Hh Hh Hh Hh HH HH HH HH HH HH HH HH HH HH HH HH HH
'''
data = data.split()

# Eye Colour
print('Eye Colour')
eye_1 = ['PP', 'Pp', 'Py']
eye_2 = ['pp', 'py']
eye_3 = ['yy']
print(data[0] + ' - ', end='')
if data[0] in eye_1:
	print('Normal eye colour')
elif data[0] in eye_2:
	print('Eye colour ignores merle')
elif data[0] in eye_3:
	print('Blue eyes')
print()

# Dominant black / Brindle
overriden_6 = False
print('Dominant black/Brindle')
coat_1 = ['KK', 'KKbr', 'Kk']
coat_2 = ['KbrKbr', 'Kbrk']
coat_3 = ['kk']
print(data[1] + ' - ', end='')
if data[1] in coat_1:
	print('Overrides agouti pattern on pair #6, gives solid black coat')
	overriden_6 = True
elif data[1] in coat_2:
	print('Gives brindled coat')
elif data[1] in coat_3:
	print('Allows expression of pattern on pair #6 in coat')
print()

# Red Extension / Masking
print('Red Extension/Masking')
mask_1 = ['EmEm', 'EmE', 'Eme']
mask_2 = ['EE', 'Ee']
mask_3 = ['ee']
print(data[2] + ' - ', end='')
if data[2] in mask_1:
	if data[1] == 'KK':
		print('Allows black in coat')
	else:
		print('Allows black in coat, has a black mask')
elif data[2] in mask_2:
	print('Allows black in coat, no mask')
elif data[2] in mask_3:
	print('No black in coat(only red), no mask')
print()

# Chocolate
print('Chocolate')
pigment_1 = ['BB', 'Bb']
pigment_2 = ['bb']
print(data[3] + ' - ', end='')
if data[3] in pigment_1:
	print('Black pigment')
elif data[3] in pigment_2:
	print('All black pigment turns into chocolate')
print()

# Dilution
print('Dilution')
dilute_1 = ['DD', 'Dd']
dilute_2 = ['dd']
print(data[4] + ' - ', end='')
if data[4] in dilute_1:
	print('No dilution')
elif data[4] in dilute_2:
	print('Dilution. All black pigment turns into blue, all chocolate pigment turns into mouse grey')
print()

# Silvering
print('Silvering')
silver_1 = ['SlSl', 'Slsl']
silver_2 = ['slsl']
print(data[5] + ' - ', end='')
if data[5] in silver_1:
	print('Causes "silvering". Masks all other colour and makes the dog solid white')
elif data[5] in silver_2:
	print('No silvering')
print()

# Agouti
print('Agouti')
agouti_1 = 'Ay'
agouti_2 = 'aw'
agouti_3 = 'at'
agouti_4 = 'asa'
print(data[6] + ' - ', end='')
if overriden_6:
	print('Overriden by #1')
elif agouti_1 in data[6]:
	print('Sable pattern')
elif agouti_2 in data[6]:
	print('Grizzle pattern')
elif agouti_3 in data[6]:
	print('Tanpoint pattern')
elif agouti_4 in data[6]:
	print('Saddle pattern')
else:
	print('Recessive solid black')
print()

# White
print('White')
white_1 = 'S'
white_2 = 'si'
white_3 = 'sp'
white_4 = 'sw'
print(data[7] + ' - ', end='')
if white_1 in data[7]:
	print('No modifications')
elif white_2 in data[7]:
	print('Irish white')
elif white_3 in data[7]:
	print('Piebald white')
elif white_4 in data[7]:
	print('Extreme piebald white')
print()

# Merling
print('Merling')
merle_1 = ['MM', 'Mm']
merle_2 = ['mm']
print(data[8] + ' - ', end='')
if data[8] in merle_1:
	print('Black areas are merled')
elif data[8] in merle_2:
	print('No merling')
print()

# Roaning
print('Roaning')
roan_1 = ['RR', 'Rr']
roan_2 = ['rr']
print(data[9] + ' - ', end='')
if data[9] in roan_1:
	print('White areas are roaned')
elif data[9] in roan_2:
	print('No roaning')
print()

# Ticking
print('Ticking')
tick_1 = 'T'
tick_2 = 'ts'
tick_3 = 'ti'
print(data[10] + ' - ', end='')
if tick_1 in data[10]:
	if white_1 in data[7]:
		print('Ticking, but not shown')
	else:
		print('Ticking')
elif tick_2 in data[10]:
	print('Dalmatian spots')
elif tick_3 in data[10]:
	print('No ticking or spots')
print()

# Colour Intensity
print('Colour Intensity')
intense_1 = 'C'
intense_2 = 'cch'
intense_3 = 'ce'
intense_4 = 'cw'
print(data[11] + ' - ', end='')
if intense_1 in data[11]:
	print('Normal red pigment')
elif intense_2 in data[11]:
	print('Red lightened to fawn')
elif intense_3 in data[11]:
	print('Red to lightened to cream')
elif intense_4 in data[11]:
	print('Red lightened to silver')
print()

# Greying
print('Greying')
grey_1 = ['GG', 'Gg']
grey_2 = ['gg']
print(data[12] + ' - ', end = '')
if data[12] in grey_1:
	print('Turns black into steel blue and chocolate into faded brown')
elif data[12] in grey_2:
	print('No greying')
print()

# Light Undersides
print('Light Undersides')
underside_1 = ['UU', 'Uu']
underside_2 = ['uu']
print(data[13] + ' - ', end='')
if data[13] in underside_1:
	print('Light undersides')
elif data[13] in underside_2:
	print('Not light undersides')
print()

# Litter Size
print('Litter Size')
litter_1 = 'L'
litter_2 = 'l'
litter_3 = 'lala'
print(data[14] + ' - ', end='')
if data[14] in litter_1:
	print('Medium litter (4-8 puppies)')
elif data[14] in litter_2:
	print('Small litter (1-3 puppies)')
elif data[14] in litter_3:
	print('Large litter (9-12 puppies)')
print()

stats = {
	'agi': 'Agility Boost',
	'cha': 'Charisma Boost',
	'int': 'Intelligence Boost',
	'spd': 'Speed Boost',
	'stm': 'Stamina Boost',
	'str': 'Strength Boost'
}
# Stat Boost
print('Stat Boost')
print(data[15] + ' - ' + stats[data[15][0:3]] + ' and ' + stats[data[15][3:6]])
print()

# Extra Stat Boost
print('Extra Stat Boost')
print(data[16] + ' - ' + stats[data[16][0:3]] + ' and ' + stats[data[16][3:6]])

# Hip Rating

# Elbow Rating

# Eye Rating

# Ear Rating