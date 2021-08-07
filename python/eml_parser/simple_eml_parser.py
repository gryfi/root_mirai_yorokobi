import mailparser
#https://pypi.org/project/mail-parser/

f = open("namefileinput.eml","r")
mail = mailparser.parse_from_file_obj(f)
f.close()

import codecs
f2 = codecs.open(""namefileoutput","w","utf-8")
f2.write(mail.body)
f2.close()
