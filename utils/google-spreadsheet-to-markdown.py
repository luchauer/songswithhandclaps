import gspread
from slugify import slugify

gc = gspread.login('ekallevig@gmail.com', 'appspecificpasswordhere')
ss = gc.open_by_key('1QHjlLByqBR1GqJDD8R7sW81bY0rHXVV_iOOODijhmZg')
worksheet = ss.sheet1
all_vals = worksheet.get_all_values()
for ridx,row in enumerate(all_vals):
    md = '---\n'
    for cidx,cell in enumerate(row):
        if cell:
            md += all_vals[0][cidx] + ': ' + cell + '\n'
    md += '---\n'
    filename = '_posts/2015-05-20-' + slugify(row[0]) + '-by-' + slugify(row[1]) + '.md'
    fo = open(filename, 'w')
    fo.write(md)
    fo.close()
    print md
