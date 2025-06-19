#Short Circuiting

is_Friend = True

is_User = True

if is_Friend or is_User:
    print("Best friends for ever")
elif is_Friend and is_User:
    print("Maybe best friends for ever")
else:
    print("Maandamano")

#But note: the elif condition (and) is never reached, even though it’s more specific. That might not be what you intended.

if is_Friend and is_User:
    print("Maybe best friends for ever")
elif is_Friend or is_User:
    print("Best friends for ever")
else:
    print("Maandamano")

#This would be the default or rather more correct way of doing  it 