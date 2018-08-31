from setuptools import setup, Extension

lyra2re2_hash_module = Extension('lyra2re2_hash',
                               sources = [
										  'lyra2re2module.c',
                                          'Lyra2RE.c',
										  'Sponge.c',
										  'Lyra2.c',
										  'sha3/blake.c',
										  'sha3/groestl.c',
										  'sha3/keccak.c',
										  'sha3/cubehash.c',
										  'sha3/bmw.c',
										  'sha3/skein.c'],
                               include_dirs=['.', './sha3'])

lyra2re_hash_module = Extension('lyra2re_hash',
                               sources = [
										  'lyra2remodule.c',
                                          'Lyra2RE.c',
										  'Sponge.c',
										  'Lyra2.c',
										  'sha3/blake.c',
										  'sha3/groestl.c',
										  'sha3/keccak.c',
										  'sha3/cubehash.c',
										  'sha3/bmw.c',
										  'sha3/skein.c'],
                               include_dirs=['.', './sha3'])


setup (name = 'lyra2re2_hash',
       version = '1.0.0',
       description = 'Binding for Bitglo lyra2v2 proof of work hashing.',
       ext_modules = [lyra2re2_hash_module, lyra2re_hash_module])

