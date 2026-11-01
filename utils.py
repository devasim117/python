def getSqr(x):
    return x*x

def exceptionHandling():
    try:
        fileCount=0;
        with open("tes1t.txt","r") as file:
            fileCount=int(file.read())
        user = input("Enter you age")
        intError = int(user)
        fileCount += intError;
        print(f"your age is {fileCount}")
    except TypeError:
        print(f"a type error came")
    except ValueError:
        print(f"a value error came")
    except FileNotFoundError:
        print(f"File not found")


def filehandling():
    from pathlib import Path 
    import json
    import csv

    def writeJSONFile():
        current_dir = Path.cwd()
        # home_dir = Path.home()
        # print(f"directory {current_dir}")
        # print(f"directory {home_dir}")

        parentFolder=Path.cwd() / "jsonFiles"

        filePath = parentFolder / "data.json"

        print(filePath.exists())
        print(filePath.is_dir())
        print(filePath.is_file())

        if not filePath.exists():
            parentFolder.mkdir()
            print(f"Created folder: {parentFolder.name}/")

            with open(filePath, "w", encoding="utf-8") as file:
                jsonData = [
                    {
                        "name":"Danish",
                        "age":23,
                        "status":True
                    },                
                    {
                        "name":"Asim",
                        "age":25,
                        "status":True
                    }
                ]
                json.dump(jsonData, file, indent=4)
            print(f"File {filePath} created successfully")

            with open(filePath,"r", encoding="utf-8") as file:
                loaded_data = json.load(file)
                print(loaded_data)

        else:
            print(f"File already available")

    
    def writeCSVFile():
        parentFolder=Path.cwd() / "csvFiles"
        filePath = parentFolder / "data.csv"

        if not filePath.exists():
            parentFolder.mkdir()
            print(f"Created folder: {parentFolder.name}/")

            with open(filePath, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Id","Name", "Age"])
                writer.writerows([
                    [101, "Asim", "Tech"],
                    [102, "Saifi", "Design"]
                ])
                
            print(f"File {filePath} created successfully")

            with open(filePath,"r", encoding="utf-8") as file:
                loaded_data = csv.reader(file)
                for row in loaded_data:
                    print(row)

        else:
            print(f"File already available")
       
    writeJSONFile()
    writeCSVFile()

