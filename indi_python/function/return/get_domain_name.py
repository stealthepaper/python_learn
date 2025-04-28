# Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и возвращает его в качестве строки
def get_domain_name (full_domain: str) -> str:
    full_domain = full_domain.replace('https://', '')
    full_domain = full_domain.replace('http://', '')
    full_domain = full_domain.split('.')
    for i in full_domain:
        if i == 'www':
            return full_domain[1]
        else: 
            return full_domain[0]


print(get_domain_name("http://google.com")) #"google"
print(get_domain_name("http://google.co.jp")) #"google"
print(get_domain_name("www.xakep.ru")) #"xakep"
print(get_domain_name("http://github.com/carbonfive/raygun"))
print(get_domain_name("https://youtube.com")) #"youtube"
print(get_domain_name("https://www.asos.com")) #"asos"
print(get_domain_name("http://www.lenovo.com")) #"lenovo"
print(get_domain_name("https://www.mywww.com")) # mywww
print(get_domain_name("https://www.whatsapp.com")) # whatsapp
print(get_domain_name("https://www.siemens.com"))
print(get_domain_name("http://www.zombie-bites.com"))