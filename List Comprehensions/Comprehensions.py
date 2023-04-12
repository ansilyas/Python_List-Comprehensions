#%%
from tkinter import W


even_number=[x for x in range(1,101) if x%2==0]
print(even_number)
# %%
odd_number=[x for x in range(1,101) if x%2!=0]
print(odd_number)
# %%
word=["year","letter","lazy","they","fox","game","hero"]
answer=[[w.upper(),w.lower(),len(w)] for w in word]
print(answer)
# %%
