import glob
import os.path
from dominate import document
from dominate.tags import *
from dominate.util import raw

# Mandatory endslash to avoid absolute/relative path issue with img src
repo = "/opt/platform/data/images/"

outputs = glob.glob(os.path.join(repo, '*.jpg'))
files = [w.replace(repo, '') for w in outputs]
inputs = sorted(list(set([f.split('_')[0] for f in files])))

previous = ''

def filterInputFiles(file, i):
    split = file.split('_')
    return split[0] == i

def groupInputs(inputs):
    groups = {}
    for f in inputs:
        split = f.split('_')
        try:
            groups[split[1]].append(f)
        except KeyError:
            groups[split[1]] = [f]
    return groups.values()

with document(title='') as doc:

    with doc.head:
        meta(charset="utf-8")
        meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
        link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css", integrity="", crossorigin="anonymous")

    with div(_class='container-fluid') as container:
        for i in inputs:

            input_files = filter(lambda file: filterInputFiles(file, i), files)
            input_groups = groupInputs(input_files)

            with div(_class='item row') as row:

                with div(_class='original col-2') as col:
                    div(img(src="original/{0}.jpg".format(i), _class="img-fluid", title=f), _class='output')

                with div(_class='neural col-10') as col:
                    for group in input_groups:
                        with div(_class="row") as group_row:
                            for f in sorted(group, key=lambda f: f.split('_')[2]):
                                params = f.split('_')
                                div([
                                    img(src=f, _class="card-img-top", title=f),
                                    div([
                                        h5(params[1], _class="card-title"),
                                        p(params[2], _class="card-text")
                                    ], _class="card-body")
                                ], _class='card float-left', style="max-width:400px")

        script(src="https://code.jquery.com/jquery-3.3.1.slim.min.js", integrity="", crossorigin="anonymous")
        script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js", integrity="", crossorigin="anonymous")
        script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js", integrity="", crossorigin="anonymous")

with open('index.html', 'w') as f:
    f.write(doc.render())
