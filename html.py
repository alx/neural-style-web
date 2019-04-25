import glob
import os.path
from dominate import document
from dominate.tags import *
from dominate.util import raw

# Mandatory endslash to avoid absolute/relative path issue with img src
repo = "/opt/platform/data/images/"

outputs = glob.glob(os.path.join(repo, '*.jpg'))
files = sorted([w.replace(repo, '') for w in outputs])
inputs = list(set([f.split('_')[0] for f in files]))

previous = ''

with document(title='') as doc:

    with doc.head:
        meta(charset="utf-8")
        meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
        link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css", integrity="sha384-ggoyr0ixcbmqv3xipma34md+dh/1fq784/j6cy/ijtquohcwr7x9jvorxt2mzw1t", crossorigin="anonymous")

    with div(_class='container-fluid') as container:
        for i in inputs:

            with div(_class='item row') as row:

                with div(_class='original col-2') as col:
                    div(img(src="original/{0}.jpg".format(i)), _class='output')

                with div(_class='neural col-10') as col:
                    for f in files:
                        current = f.split('_')[0]
                        if f.split('_')[0] == i and f.split('_')[1] != i:
                            div(img(src=f), _class='output')

        script(src="https://code.jquery.com/jquery-3.3.1.slim.min.js", integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo", crossorigin="anonymous")
        script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js", integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1", crossorigin="anonymous")
        script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js", integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM", crossorigin="anonymous")

with open('index.html', 'w') as f:
    f.write(doc.render())
