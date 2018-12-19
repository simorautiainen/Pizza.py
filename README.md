# Pizza.py
By launching it on terminal and giving argument a pizzaonline address you'll get all that you can buy in min to max order in your txt file.
You'll need to have installed following libraries:
  Requests;
  bs4, for BeautifulSoup;
  re;
  collections, for OrderedDict;
  
So you go to pizza-online website and write your address there. Then press enter. Then it will load you to another site where you can see all the restaurants that are in your reach. Then get sites address and copy it. Write in your shell/terminal
python pizza.py "sites address"
like mine
python pizza.py "https://pizza-online.fi/web/find/index?search_by=address&value=N%C3%A4yttelij%C3%A4nkatu+28%2C+33720+Tampere%2C+Suomi#search_results"
and wait until its loaded. Then open pizza.txt file and see all pizzas

