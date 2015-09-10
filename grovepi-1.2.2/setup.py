from distutils.core import setup
setup(
  name = 'grovepi',
  packages = ['grovepi'], 
  version = '1.2.2',
  description = 'This is the python library for GrovePi, which is an open source platform for connecting Grove Sensors to the Raspberry Pi',
  author = 'Dexter Industries',
  author_email = 'john@dexterindustries.com',
  url = 'https://github.com/DexterInd/GrovePi',
  download_url = 'https://codeload.github.com/DexterInd/GrovePi/legacy.tar.gz/1.2.2', # I'll explain this in a second
  keywords = ['raspberry pi', 'grove', 'grovepi','sensors'],
  classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Environment :: Console',
  'Intended Audience :: Developers',
  'Intended Audience :: Education',
  'Programming Language :: Python :: 2.7',
  ],
)