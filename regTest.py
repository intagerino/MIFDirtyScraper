import re

text = "Sdefffv Seeasdcfyyy gmsi axf//fdsoei ajc344ks dd"
text2= '<a href="/mif/employees/edmundas-gaigalas/">Edmundas Gaigalas, Doc., Dr.</a> Ęetras Įana'
text3= 'DM 1k. <a href="/mif/groups/duomenu-mokslas-1k-1gr-2019-2/">1gr.</a>, <a href="/mif/groups/duomenu-mokslas-1k-2gr-2019/">2gr.</a><br>EKO 1k. <a href="/mif/groups/ekonometrija-1k-1gr-2019/">1gr.</a>, <a href="/mif/groups/ekonometrija-1k-2gr-2019/">2gr.</a>'

reg = "/^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u"
reg2 = "[A-Z][a-z]+"
reg3 = "([A-Z]+\s[1-4][k])"
reg5 = "[A-Ž][a-ž]*\s([A-Ž][a-ž]*\s?)+"
reg6 ="[A-ZČĖĘĮŲŪČŠŽ][a-ząčęėįųūčšž]+\s([A-ZČĖĘĮŲŪČŠŽ][a-ząčęėįųūčšž]+\s?)+"

gn = re.findall(reg2, text2)

#print(*re.findall(reg3, text3))
for m in re.finditer(reg6, text2):
    print(m.group(0))
#[A-Za-ząčęėįųūčšžČĖĘĮŲŪČŠŽ]+