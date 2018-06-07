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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ispc
#
# You can edit this file again by typing:
#
#     spack edit ispc
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os

class Ispc(Package):
    """ispc is a compiler for a variant of the C programming language, with
    extensions for "single program, multiple data" (SPMD) programming. Under
    the SPMD model, the programmer writes a program that generally appears to
    be a regular serial program, though the execution model is actually that a
    number of program instances execute in parallel on the hardware."""

    homepage = "https://ispc.github.io/"
    url      = "https://github.com/ispc/ispc"

    version('1.9.1', git='https://github.com/ispc/ispc',
            tag='v1.9.1')

    depends_on('llvm')


    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('LLVM_HOME', self.spec['llvm'].prefix)
        spack_env.set('PATH',
                      ':'.join([self.spec['llvm'].prefix.bin,
                                os.environ['PATH']]))

    def install(self, spec, prefix):
        make()

        mkdir(prefix.bin)
        binfiles = ['ispc']
        for binfile in binfiles:
            print binfile
            install(binfile, prefix.bin)
