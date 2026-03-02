import xml.etree.ElementTree as ET

# Parsing from a file
tree = ET.parse('books.xml')
root = tree.getroot()
# print(root)

# From a string
# fiction 
fiction_counter = 10

# for book in root.findall()

book_4 = root.find(".//book[@id='4']")
print(book_4.attrib)
book_4.set('genre', 'action')

pages_7.task 

ET.indent(root)