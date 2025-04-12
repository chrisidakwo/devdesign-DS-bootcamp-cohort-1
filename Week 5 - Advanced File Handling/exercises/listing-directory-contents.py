import os
import datetime

def listDirectoryContent(path):
    absolutePath = os.path.abspath(path)

    print(f'\nContents of {absolutePath}')
    print(f'\n{'Name':<50} {'Size':<10} {'Modified':<20} {'Type':<10}')
    print("-" * 90)

    directories = os.listdir(absolutePath)
    directories.sort()

    directories.remove('.DS_Store')
    directories.remove('.git')

    for item in directories:
        fullPath = os.path.join(path, item)

        # `os.path.getsize()`` returns the file or directory size (in bytes)
        size = os.path.getsize(fullPath)

        modTime = datetime.datetime.fromtimestamp(os.path.getmtime(fullPath))
        
        itemType = "Directory" if os.path.isdir(fullPath) else "File"
        
        # TODO: Provide link for datetime format
        print(f"{item:<50} {size:<10,} {modTime.strftime('%Y-%m-%d %H:%M'):<20} {itemType:<10}")

listDirectoryContent('')

