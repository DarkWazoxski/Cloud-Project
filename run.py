def clean_line(list):
	clean_list=[]
	for item in list:
		clean_item=item.strip()
		
		if clean_item != "":
			clean_list.append(clean_item)
	
	return clean_list
	

list=["  Hello  ","\n", "  World  ", "  Python  "]
cleaned_list = clean_line(list)
print(cleaned_list)
