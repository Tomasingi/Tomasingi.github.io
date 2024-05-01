import os

def write_links(path, links):
    with open(path, 'r+') as f:
        content = f.read()

        fstr = '<div id="links">'
        start = content.find(fstr)
        end = content.find('</div>', start)

        index = start - 1
        n_spaces = 0
        while (content[index] == ' '):
            n_spaces += 1
            index -= 1

        link_str = '\n' + ' ' * (n_spaces + 2) + ('\n' + ' ' * (n_spaces + 2)).join(links) + '\n' + ' ' * n_spaces
        content = content[:start+len(fstr)] + link_str + content[end:]

        f.seek(0)
        f.write(content)
        f.truncate()

def main():
    main_page = 'index.html'
    pages = [
        'Hjólaleiðir',
        'Reykjavík',
        'Stockholm',
        'İstanbul',
        'Göteborg',
    ]

    page_files = dict()

    for page_file in os.listdir('pages'):
        path = os.path.join('pages', page_file)
        with open(path, 'r') as f:
            lines = f.readlines()
            page_name = lines[0][4:-4]
            if page_name not in pages:
                raise ValueError(f'Page {page_name} not found in links.py')

            page_files[page_name] = page_file

    links = {
        'main': ['<a href="./index.html">Home</a>'] + [f'<a href="./pages/{page_files[page_name]}">{page_name}</a>' for page_name in pages],
        'pages': ['<a href="../index.html">Home</a>'] + [f'<a href="./{page_files[page_name]}">{page_name}</a>' for page_name in pages]
    }

    write_links(main_page, links['main'])

    for page_file in os.listdir('pages'):
        path = os.path.join('pages', page_file)
        write_links(path, links['pages'])


if __name__ == '__main__':
    main()