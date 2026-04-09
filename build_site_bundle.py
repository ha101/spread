from pathlib import Path
import shutil


BASE_PATH = Path(__file__).parent
DIST_PATH = BASE_PATH / 'dist'
PUBLIC_FILES = [
    'index.html',
    'benchmark_data.js',
    'futures_data.js',
]
OPTIONAL_FILES = [
    'CNAME',
]


def main():
    if DIST_PATH.exists():
        shutil.rmtree(DIST_PATH)
    DIST_PATH.mkdir(parents=True)

    for name in PUBLIC_FILES:
        source = BASE_PATH / name
        if not source.exists():
            raise FileNotFoundError(f'Missing required public file: {source}')
        shutil.copy2(source, DIST_PATH / name)

    for name in OPTIONAL_FILES:
        source = BASE_PATH / name
        if source.exists():
            shutil.copy2(source, DIST_PATH / name)

    (DIST_PATH / '.nojekyll').write_text('')
    print(f'Built site bundle in {DIST_PATH.name}')


if __name__ == '__main__':
    main()
