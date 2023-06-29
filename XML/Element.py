
import xml.etree.ElementTree as ET
"""
String method
data = '''<?xml version="1.0"?>
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <genre>Computer</genre>
      <price>44.95</price>
      <publish_date>2000-10-01</publish_date>
      <description>An in-depth look at creating applications 
      with XML.</description>
   </book>
</catalog>
'''
myroot = ET.fromstring(data)

"""


#File method
mytree = ET.parse('Sample.xml')
myroot = mytree.getroot()

'''
#Looping through all the elements
for x in myroot[0]:
   print(x.tag, x.attrib)

#Print the tab of the first children of the root element
print(myroot[0].tag)
print(myroot[0].attrib)

#Print the tab of the first children of the root element
for x in myroot[1]:
    print(x.text)


#To find all element
for x in myroot.findall('book'):
    author = x.find('author').text
    genre = x.find('genre').text
    print(f'The author is {author}  and the genre is {genre}')

#To change the price and add a $ - in fron of all of them and write it back as a new file.
#The set method to set a new attribute called "updated" and we set it to yes. So people know it was updated
for price in myroot.iter('price'):
    new_price = '$ - ' + str(price.text)
    price.text = str(new_price)
    price.set('updated', 'yes')

#To modify the original file we simply pass the name of the file as a parameter here  
mytree.write('new.xml')


#To create a new element we use the SubElement method. Create an element called ratings for each book
for book in myroot.iter('book'):
    ratings = ET.SubElement(book,'ratings')
    ratings.text = 'It sounds amazing'
mytree.write('new2.xml')

#To remove attributes, we use the pop function
mytree2 = ET.parse('Sample.xml')
myroot2 = mytree2.getroot()

for book in myroot2.iter('book'):
    if 'ratings' in book.attrib:
      book.attrib.pop('ratings')

mytree2.write('new3.xml')

#We can also use remove as well or clear.
myroot[0].remove(mytoor[0][0])
myroot[0].clear()
'''



