#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['libsearpc', 'ccnet-server']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import download_repo_depends
    download_repo_depends()
    makechrootpkg_args = []
    for i in Path('~/repo_depends').rglob('*.pkg.tar*'):
        makechrootpkg_args += ['-I', i]

    single_main(build_prefix, makechrootpkg_args=makechrootpkg_args)
