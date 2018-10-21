# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from subprocess import Popen, PIPE
from stream import *
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    import argparse
    parser = argparse.ArgumentParser(description='pystream')
    parser.add_argument('--STREAM_ARRAY_SIZE', action='store',
                        dest='STREAM_ARRAY_SIZE', type=int,
                        default=10000000)
    parser.add_argument('--NTIMES', action='store', dest='NTIMES', type=int,
                        default=10)
    parser.add_argument('--OFFSET', action='store', dest='OFFSET', type=int,
                        default=0)
    parser.add_argument('--STREAM_TYPE', action='store', dest='STREAM_TYPE',
                        default='double')
    parser.add_argument('--test', nargs="*", default=['all'])
    args = parser.parse_args()

    desc = {'vector': 'Pure Python vectorized',
            }

    testlist = ['vector',]
    tests = []

    if 'all' in args.test:
        tests = testlist

    for test in args.test:
        if test in testlist:
            tests.append(test)

    output = main(args, tests, desc)
    checktick()
    return '<html><body>' + output + '</body></html>'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
