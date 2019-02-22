##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
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
from spack import *


class Luck(CMakePackage):
    homepage = "https://github.com/LLNL/hiop"
    url      = "https://github.com/LLNL/hiop"

    version('568c9ac6906', git='https://lc.llnl.gov/bitbucket/scm/topopt/luck.git',
            commit='568c9ac6906')
    version('develop', git='https://lc.llnl.gov/bitbucket/scm/topopt/luck.git',
            branch='master')

    depends_on('boost@1.57.0:')
    depends_on('cmake@3.9.0:', type='build')
    flag_handler = CMakePackage.build_system_flags

    def cmake_args(self):
        args = ["-DBLAS_LIBRARIES=/usr/tcetmp/packages/lapack/lapack-3.8.0-gcc-4.9.3/lib/libblas.so", "-DLAPACK_LIBRARIES=/usr/tcetmp/packages/lapack/lapack-3.8.0-gcc-4.9.3/lib/liblapack.so"]
        spec = self.spec

# necessary because ray can't find stuff
#-DBLAS_LIBRARIES=/usr/tcetmp/packages/lapack/lapack-3.8.0-gcc-4.9.3/lib/libblas.so \
#-DLAPACK_LIBRARIES=/usr/tcetmp/packages/lapack/lapack-3.8.0-gcc-4.9.3/lib/liblapack.so \

        return args
