import easyocr

reader =easyocr.Reader(['ko'])
results =reader.readtext('img03.png')
for results in results:
    text =results[1]
    print(text)
results =reader.readtext('./img/image4.png')
for results in results:
   text=results[1]
   print(text)