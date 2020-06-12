#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['libsearpc']
pre_build = aur_pre_build
post_build = aur_post_build

import os
from pathlib import Path
from lilac2.lilacyaml import load_lilac_yaml

def download_repo_depends(package=None):
    if package:
        path = Path('..') / package
    else:
        path = Path('.')

    _repo_depends = []
    try:
        conf = load_lilac_yaml(path)
        if 'repo_depends' in conf:
            _repo_depends = conf['repo_depends']
    except FileNotFoundError:
        pass

    for i in _repo_depends:
        if type(i) is tuple:
            pkgbase, pkgname = i
        else:
            pkgbase, pkgname = i, i

        try:
            run_cmd(['download-package-from-artifact.sh', 'petronny/arch4edu', pkgbase, pkgname, '~/repo_depends', os.environ['TOKEN']])
        except:
            run_cmd(['download-package-from-repo.sh', pkgbase, 'arch4edu', 'x86_64', '~/repo_depends'])

        download_repo_depends(i)

if __name__ == '__main__':
    download_repo_depends()

    makechrootpkg_args = []
    for i in Path('~/repo_depends').rglob('*.pkg.tar*'):
        makechrootpkg_args += ['-I', i]

    single_main(build_prefix, makechrootpkg_args=makechrootpkg_args)
