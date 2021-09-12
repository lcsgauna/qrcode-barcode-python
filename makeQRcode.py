import qrcode

random_url = {
    'Google' : 'https://www.google.com',
    'Youtube':'https://www.youtube.com',
    'Github' : 'https://www.github.com'
}

for name_url in random_url:
    url = random_url[name_url]
    image_qrcode = qrcode.make(url)
    image_qrcode.save(f'qrcode_{name_url}.png')