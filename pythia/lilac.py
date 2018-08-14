#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'arch4edu-x86_64'
depends = ['fastjet', 'hempc', 'lhapdf']

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if line.startswith('depends='):
        print(line)
        print('makedepends=("fastjet" "hepmc" "lhapdf" "root")')
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
