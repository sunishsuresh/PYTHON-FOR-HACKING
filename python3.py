################dictionaries | [] -> list | () -> tuples | {} -> dictionaries |
print ( "Dictionaries are keys and values : " )
drinks = {"cola" : 7,"black mama" : 10 ,"sugarcane" : 15}
#drink is "key" and prise is "value" 
print (drinks)

company = {"IT" : ["surya","ais","coco"] ,"Eco" : ["kali","harsh","loly"],
} #dictionaries -> list[]
print(company)

#adding in dictionaries 
company["legal"] = ["jake","mike"] #for adding in dictionaries | var[]=[] |
#add new key : values pair
print(company)

# var.update({})
company.update ({"spon":["koko","ani","sia"]})
company.update({"promocode" :["ASDA","ASDD","FGDDF"]})
print(company)
drinks["cola"] = 4 #updating value | var[key] = value |

#get value of key   | var.get()
print(drinks.get("black mama"))
print(company.get("IT"))

#list and dictionaries
movie = ["your name","I want to eat","mob pshco","attack on titan"]
name = ["surya", "sykon" ,"mike", "arc"]
combine = zip(movie,name)
movie_dict = {key:value for key,value in combine} #same as list zip |{key:value for key,value in var}
print (movie_dict)
