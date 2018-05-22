# coding: utf-8
__author__ = "João Marcos S. e Araújo"
__email__ = "marcosjoao37@hotmail.com.br"

from sys import exit
import json

"""
*dda = Dicionário de Arquivos
Dicionário com o nome de todas as extensões de elementos do dda*.
"""


class Config:
    def __init__(self):
        try:
            fileDict = open("user_config.json", "r")
        except:
            print("Can't open the JSON file\nMaking a default JSON for the user...")
            try:
                fileDict = open("user_config.json", "w")
                default = """{
	"dataTypes":[
		{"name":"Photos_", "types":["jpg", "png", "bmp", "jpeg",
		"gif"]},
		{"name":"Compacted_", "types":["rar", "zip", "7zip",
		"tar.gz", "tar.gx", "7z", "gzip", "tar"]},
		{"name":"Binaries_", "types":["exe", "run", "msi",
		"app", "apk", "deb", "jar", "ipa"]},
		{"name":"Scripts_", "types":["sh", "py", "java", "bat",
		"c", "cs", "php", "vb", "vbs", "cpp", "sql", "js", "ts"]},
		{"name":"Documents_", "types":["doc", "docx", "txt",
		"html", "odt", "cad", "pdf", "xlsx", "xls",
		"csv", "tsv", "ppt", "pptx", "epub", "docm",
		"dot", "dotx", "xps", "json", "csv", "xml"]},
		{"name":"Musics_", "types":["mp3", "wav", "flac", "aac"]},
		{"name":"Videos_", "types":["wmv", "mp4", "mkv", "rmvb",
		"flv", "3gp", "avi", "mov", "mpg"]},
		{"name":"Dev_", "types":["mobileprovision", "p12", "keystore"]}
	]
}"""
                fileDict.write(default)
            except:
                print("Can't write the JSON file on disk... Exiting...")
                exit(0)
        finally:
            fileDict.close()

    def updateJsonData(self, dictData):
        jsonUpdated = "{\"dataTypes\":["

        for keyName in dictData:
            keyValueFormatted = ""
            for value in dictData[keyName]:
                keyValueFormatted += "\"" + value + "\","
            keyValueFormatted = keyValueFormatted[0:-1]
            jsonUpdated += "{\"name\":\"" + keyName + \
                "\", \"types\":[" + keyValueFormatted + "]},"
        jsonUpdated = jsonUpdated[0:-1]
        jsonUpdated += "]}"
        fileDict = open("user_config.json", "w")
        result = fileDict.write(jsonUpdated)

        if(result > 0):
            return True
        else:
            return False

    def loadJsonFile(self):
        fileDict = open("user_config.json", "r")
        jsonData = json.load(fileDict)
        return jsonData

    def loadDataTypes(self):
        jsonData = self.loadJsonFile()
        fileDict = {}
        for typeData in jsonData["dataTypes"]:
            fileDict[typeData["name"]] = typeData["types"]
        return fileDict
