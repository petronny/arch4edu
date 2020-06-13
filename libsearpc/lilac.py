#!/usr/bin/env python3
import os
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': None}]
build_prefix = os.path.expanduser('~/git/actions/action-extra-x86_64')
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
