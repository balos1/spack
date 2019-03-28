# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install sundials-regression
#
# You can edit this file again by typing:
#
#     spack edit sundials-regression
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
from spack import *

class SundialsRegression(Package):
    """Installs the packages needed to run the sundials regression suite"""

    homepage = "https://computation.llnl.gov/projects/sundials"
    url = "https://computation.llnl.gov/projects/sundials/download/sundials-2.7.0.tar.gz"
    maintainers = ['cswoodward', 'gardner48', 'balos1']

    version('4.1.0', sha256='280de1c27b2360170a6f46cb3799b2aee9dff3bddbafc8b08c291a47ab258aa5', url_for_version='https://computation.llnl.gov/projects/sundials/download/sundials-4.1.0.tar.gz')

    variant('cuda', default=False)
    variant('int64', default=False)
    variant('double', default=True)
    variant('superlu-dist', default=True)

    depends_on('cuda', when='+cuda')
    depends_on('netlib-lapack@3.8.0')
    depends_on('openmpi@3.1.2')
    depends_on('hypre@2.14.0~int64', when='~int64')
    depends_on('hypre@2.14.0+int64', when='+int64')
    depends_on('petsc@3.10.3~int64', when='~int64~superlu-dist')
    depends_on('petsc@3.10.3+int64', when='+int64~superlu-dist')
    depends_on('raja@:0.7.0', when='+cuda')
    depends_on('suite-sparse@5.3.0')
    depends_on('superlu-dist~int64@develop', when='~int64+superlu-dist')
    depends_on('superlu-dist+int64@develop', when='+int64+superlu-dist')

    def install(self, spec, prefix):
        # Prevent the error message
        #      ==> Error: Install failed for sundials-regression. Nothing was installed!
        #      ==> Error: Installation process had nonzero exit code : 256
        with open(os.path.join(spec.prefix, 'bundle-package.txt'), 'w') as out:
            out.write('This is a bundle\n')
            out.close()
