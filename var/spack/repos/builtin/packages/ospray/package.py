# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install embree
#
# You can edit this file again by typing:
#
#     spack edit embree
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os

class Ospray(CMakePackage):

    homepage = "https://www.ospray.org/"
    url      = "https://github.com/ospray/ospray"

    version('1.4.0', git='https://github.com/ospray/ospray',
            tag='v1.4.0')
    depends_on('ispc')
    depends_on('embree')
    depends_on('intel-tbb')
    flag_handler = CMakePackage.build_system_flags


    def cmake_args(self):
        args = []
        spec = self.spec

        ispc_path = os.path.join(self.spec['ispc'].prefix.bin, "ispc")
        embree_dir = self.spec['embree'].prefix

        args.append(''.join(["-DISPC_EXECUTABLE=", ispc_path]))
        args.append("".join(["-Dembree_DIR=", embree_dir]))
        return args
