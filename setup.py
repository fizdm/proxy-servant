from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='proxy-servant',
    version='1.0.0',
    description='proxy-servant is your best friend that will give you a working proxy every time you request it',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Dmitriy Popov',
    author_email='dpopov@fizdm.ru',
    keywords=['Proxy', 'Proxy Checker', 'Proxy Servant', 'Servant', 'Python 3'],
    url='https://github.com/FizzyShow/proxy_servant',
    download_url='https://pypi.org/project/proxy_servant/'
)

install_requires = [
    'aiohttp',
    'aiosocksy',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
