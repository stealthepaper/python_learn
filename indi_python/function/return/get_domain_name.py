# str.rstrip() and  str.lstrip() 
def get_domain_name (full_domain: str) -> str:
    full_domain = full_domain.replace('https://www.', '')
    full_domain = full_domain.replace('http://', '')
    full_domain = full_domain.split('.')
    return full_domain[0]




print(get_domain_name("http://google.com")) #"google"
print(get_domain_name("http://google.co.jp")) #"google"
print(get_domain_name("http://github.com/carbonfive/raygun"))
print(get_domain_name("https://www.asos.com")) #"asos"
print(get_domain_name("https://www.mywww.com")) # mywww
print(get_domain_name("https://www.whatsapp.com")) # whatsapp
print(get_domain_name("https://www.siemens.com"))
