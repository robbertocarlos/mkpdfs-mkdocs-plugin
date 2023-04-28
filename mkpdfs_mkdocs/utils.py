from bs4 import BeautifulSoup


def modify_html(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.new_tag('a',
                     href=href,
                     title='Download',
                     download=None
                     )
    a['class'] = 'md-content__icon pdf-download-btn'
    i = soup.new_tag('i')
    i['class'] = 'fa fas fa-download'
    small = soup.new_tag('small')
    a.append(i)
    small.append(' PDF')
    a.append(small)
    if soup.article:
        soup.article.insert(0, a)
    else:
        soup.find('div', **{'role': 'main'}).insert(0, a);
    return str(soup)


def modify_html_svg_download(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    svg_icon = '<svg height="35px" id="Layer_1" version="1.1" viewBox="0 0 512 512" width="30px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style=" padding-bottom: 10px; "> <path d="M128,0c-17.6,0-32,14.4-32,32v448c0,17.6,14.4,32,32,32h320c17.6,0,32-14.4,32-32V128L352,0H128z" style="fill: #e2e5e7"></path> <path d="M384,128h96L352,0v96C352,113.6,366.4,128,384,128z" style="fill: #b0b7bd"></path> <polygon points="480,224 384,128 480,128 " style="fill: #cad1d8"></polygon> <path d="M416,416c0,8.8-7.2,16-16,16H48c-8.8,0-16-7.2-16-16V256c0-8.8,7.2-16,16-16h352c8.8,0,16,7.2,16,16 V416z" style="fill: #f15642"></path> <g> <path d="M101.744,303.152c0-4.224,3.328-8.832,8.688-8.832h29.552c16.64,0,31.616,11.136,31.616,32.48 c0,20.224-14.976,31.488-31.616,31.488h-21.36v16.896c0,5.632-3.584,8.816-8.192,8.816c-4.224,0-8.688-3.184-8.688-8.816V303.152z M118.624,310.432v31.872h21.36c8.576,0,15.36-7.568,15.36-15.504c0-8.944-6.784-16.368-15.36-16.368H118.624z" style="fill: #ffffff"></path> <path d="M196.656,384c-4.224,0-8.832-2.304-8.832-7.92v-72.672c0-4.592,4.608-7.936,8.832-7.936h29.296 c58.464,0,57.184,88.528,1.152,88.528H196.656z M204.72,311.088V368.4h21.232c34.544,0,36.08-57.312,0-57.312H204.72z" style="fill: #ffffff"></path> <path d="M303.872,312.112v20.336h32.624c4.608,0,9.216,4.608,9.216,9.072c0,4.224-4.608,7.68-9.216,7.68 h-32.624v26.864c0,4.48-3.184,7.92-7.664,7.92c-5.632,0-9.072-3.44-9.072-7.92v-72.672c0-4.592,3.456-7.936,9.072-7.936h44.912 c5.632,0,8.96,3.344,8.96,7.936c0,4.096-3.328,8.704-8.96,8.704h-37.248V312.112z" style="fill: #ffffff"></path> </g> <path d="M400,432H96v16h304c8.8,0,16-7.2,16-16v-16C416,424.8,408.8,432,400,432z" style="fill: #cad1d8"></path></svg>'
    svg = BeautifulSoup(svg_icon, 'html.parser')
    a = soup.new_tag('a',
                     href=href,
                     title='Download',
                     download=None
                     )
    a['style'] = 'margin-left: 10px;'
    a['class'] = 'md-content__icon pdf-download-btn'
    i = soup.new_tag('i')

    i['class'] = 'fa fas fa-download'
    small = soup.new_tag('small')
    a.append(i)
    small.append(svg)
    a.append(small)
    nav = soup.find('div', **{'role': 'dialog'})
    if nav:
        nav.insert_after(a)
    else:
        head_title = soup.find('div', {"class": "md-header__title"})
        head_title.insert_after(a)
    return str(soup)


def gen_address(config):
    soup = BeautifulSoup('<body></body>',
                         'html5lib'
                         )
    address = soup.new_tag('address')
    p = soup.new_tag('p')
    for k, line in {'author': config['author'],
                    'company': config['company']}.items():
        if line:
            sp = soup.new_tag('p', **{'class': k})
            sp.append("{}".format(line))
            p.append(sp)
    address.append(p)
    if config['copyright']:
        span = soup.new_tag('p',
                            id="copyright"
                            )
        span.append(config['copyright'])
        address.append(span)
    return address


def is_external(href: str):
    return href.startswith('http://') or href.startswith('https://')
