import xml.etree.ElementTree as ET

data = '''<person>
<name>Nate</name>
<phone type="intl">0909875640</phone>
<email hide="Yes"/>
</person>'''

xml = ET.fromstring(data)
print('Name:',xml.find('name').text)
print('Attr:',xml.find('email').get('hide'))
print('Phone:',xml.find('phone').get('type'))
