with open('st.txt','w') as f:
    f.write('Привет от Python!')
my_list = list()
with open('st.txt','r') as f:
    my_list.append(f.read())

print(my_list)
