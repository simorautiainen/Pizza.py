import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
from sys import argv


page = requests.get(argv[1])
soup = BeautifulSoup(page.content,features="lxml")
hrefs = soup.find("ul", id="restaurant_list")
hrefs1 = hrefs.find_all("li", class_="restaurant_list_item")
better_values = []
all_pizzas = {}
all_pizzas_with_real_values = {}
file = open("pizzaonline.txt","w")
for i in hrefs1:
    #Getting every link from every restaurant_list_item
    linkki = i.find("a")["href"]
    pizzerian_nimi = i.find("a").get_text()
    pizzapage = requests.get("https://pizza-online.fi{}".format(linkki))
    pizzasoppa = BeautifulSoup(pizzapage.content,features="lxml")


    #all em categories
    kategoriat = pizzasoppa.find_all("div",class_="category_products")

    for erilajikkeet in kategoriat:
        if("pizza" in erilajikkeet.find("h3").get_text().lower()):


            try:
                #making lists for every dataproductids
                lista = [d["data-product_id"] for d in erilajikkeet.select("li")]
                #print(lista)
                for dataid in lista:

                    tuotteen_tiedot = pizzasoppa.find("li", {"data-product_id" : "{}".format(dataid)})
                    nimi = tuotteen_tiedot.find("span").get_text()

                    kaikki_hinnat = tuotteen_tiedot.find("select", id="product_variant_for_{}".format(dataid))
                    hinta_lista = [d.get_text() for d in kaikki_hinnat.find_all("option")]

                    koko_nimi = pizzerian_nimi + " " + nimi
                    j=0
                    for i in hinta_lista:
                        j = j+1
                        string = str(j)
                        toinen_nimi = koko_nimi + "(" + string + ")"
                        all_pizzas.update({toinen_nimi:i})
            #Just because pizzaonline is not good and has empty categories this needs
            #to be here.

            except KeyError:
                pass

em_values = all_pizzas.values()
em_keys = list(all_pizzas.keys())

for i in em_values:
    #because drinks has their volume first and we don't want that as our
    #price, so we do this

    try:
        better_values.append(float(re.findall("\d+\.\d+",i.replace(",","."))[1]))
    except IndexError:
        better_values.append(float(re.findall("\d+\.\d+",i.replace(",","."))[0]))

#making two lists out of the values we got.

for i in range(len(better_values)):

    all_pizzas_with_real_values.update({em_keys[i] : better_values[i]})




ordered_pizza = OrderedDict(sorted(all_pizzas_with_real_values.items(), key=lambda x: x[1]))

for k,v in ordered_pizza.items():
    ordered_pizza[k] = all_pizzas.get(k)


for k,v in ordered_pizza.items():
    file.write("{} : {} \n".format(k,v))

file.close()
