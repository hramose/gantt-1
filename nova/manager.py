# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Base class for managers of different parts of the system
"""

from nova import utils
from nova import flags

from twisted.internet import defer

FLAGS = flags.FLAGS
flags.DEFINE_string('db_driver', 'nova.db.api',
                    'driver to use for volume creation')


class Manager(object):
    """DB driver is injected in the init method"""
    def __init__(self, host=None, db_driver=None):
        if not host:
            host = FLAGS.host
        self.host = host
        if not db_driver:
            db_driver = FLAGS.db_driver
        self.db = utils.import_object(db_driver)  # pylint: disable-msg=C0103

    def periodic_tasks(self, context=None):
        """Tasks to be run at a periodic interval"""
        yield

    def init_host(self):
        """Do any initialization that needs to be run if this is a standalone
        service. Child classes should override this method."""
        pass
