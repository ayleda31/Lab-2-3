import os
import time
import sys

try:
    buffer=10000
    #buffer=int(input('Введите количество символов:'))          #можем ввести buffer с клавиатуры
    with open ('text.txt',encoding='utf-8') as f:
        text=f.read(buffer)
        if text=='':                                            #если файл пуст, то просим...
            print("\nДобавьте текст в файл.")
            sys.exit()
                            
        start = time.time()
        print("\n-----Результат работы программы-----\n-----Локальное время",time.ctime(),"-----")
        print()
        gl=['a','e','i','o','u','y']
        GL=['A','E','I','O','U','Y']
        
        while text:
            txt=text.split(' ')
            for i in range(len(txt)-1):
                for j in range(len(gl)):
                    if txt[i][0]==gl[j]:
                        txt[i]=txt[i].replace(txt[i][0], GL[j])
                    
            txt=' '.join(txt)         
            print(txt)                                          #выводим редактированный текст
            text=f.read(buffer)                                 #считываем файл

        finish = time.time()
        result = finish - start                                 #определяем время и память работы программы
        print("\nProgram time: "+ str(result) +" seconds.")
        print("Program size: "+ str(os.path.getsize('lab-2-3.py')) +" bytes.")
    
except ValueError:
    print("\nэто не слово")

except FileNotFoundError:
    print("\nФайл text.txt не найден в директории проекта.\nДобавьте файл в директорию или переименуйте существующий файл.")
