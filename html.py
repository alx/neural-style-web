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
        link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css", integrity="", crossorigin="anonymous")

    with div(_class='container-fluid') as container:
        for i in inputs:

            with div(_class='item row') as row:

                with div(_class='original col-2') as col:
                    div(img(src="original/{0}.jpg".format(i), _class="img-fluid", title=f), _class='output')

                with div(_class='neural col-10 text-center') as col:
                    for f in files:
                        current = f.split('_')[0]
                        if f.split('_')[0] == i and f.split('_')[1] != i:
                            div(img(src=f, _class="img-fluid float-left", title=f, style="max-width:200px"), _class='output')

        script(src="https://code.jquery.com/jquery-3.3.1.slim.min.js", integrity="", crossorigin="anonymous")
        script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js", integrity="", crossorigin="anonymous")
        script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js", integrity="", crossorigin="anonymous")

with open('index.html', 'w') as f:
    f.write(doc.render())
