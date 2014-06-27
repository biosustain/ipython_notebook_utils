# Copyright 2014 Novo Nordisk Foundation Center for Biosustainability, DTU.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
from IPython.display import HTML, Javascript, display


class ProgressBar():
    def __init__(self, size=100):
        self.progress = 0
        self.size = size
        self.id = "progress-bar-%s" % str(uuid.uuid4())

    def start(self, width='50%'):
        style = "width:%s;" % width
        html = HTML("<progress id='%s' value='0' max='%i' style='%s'></progress>" % (self.id, self.size, style))
        display(html)

    def increment(self, i=1):
        p = self.progress + i
        self._update(p)

    def set(self, progress):
        p = progress
        self._update(p)

    def _update(self, p):
        if p <= self.size:
            js = Javascript("jQuery('#%s').val('%i')" % (self.id, p))
            display(js)
            self.progress = p
        else:
            raise RuntimeError("Already reached 100%")