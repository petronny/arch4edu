#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = ['libsearpc']
pre_build = aur_pre_build
post_build = aur_post_build

from lilac2.lilacyaml import load_lilac_yaml
from pathlib import Path

def download_repo_depends(path='/tmp'):
    conf = load_lilac_yaml(Path('.'))
    if 'repo_depends' in conf:
        run_cmd()

if __name__ == '__main__':

    import sys
    download_repo_depends()
    sys.exit()
    single_main(build_prefix)
