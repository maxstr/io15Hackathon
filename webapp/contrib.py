# fix module paths

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'libs'))

from libs import web