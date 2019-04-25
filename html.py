import glob
import os.path
from dominate import document
from dominate.tags import *

repo = "/opt/platform/data/images"
outputs = glob.glob(os.path.join(repo, '*.jpg'))

with document(title='') as doc:
    h1('---===xxx')
    for path in outputs:
        div(img(src=path.replace(repo, '')), _class='output')

with open('index.html', 'w') as f:
    f.write(doc.render())
