#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['libsearpc']
pre_build = aur_pre_build
post_build = aur_post_build

from pathlib import Path
from lilac2.lilacyaml import load_lilac_yaml

def download_repo_depends(package=None):
    if package:
        conf = load_lilac_yaml(Path('..') / package)
    else:
        conf = load_lilac_yaml(Path('.'))

    _repo_depends = []
    if 'repo_depends' in conf:
        repo_depends = conf['repo_depends']

    for i in repo_depends:
        run_cmd(['download-package-from-repo.sh', i, 'arch4edu', 'x86_64', '~/repo_depends'])
        download_repo_depends(i)

if __name__ == '__main__':
    import sys
    download_repo_depends()
    sys.exit()
    single_main(build_prefix)
