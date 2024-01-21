def integrate():
    try:
        fin = open("modules/app_init.py", "r")
        app_init = fin.read()
        fin.close()


        fin = open("modules/index.py", "r")
        app_index = fin.read()
        fin.close()

        fin = open("modules/app_run.py", "r")
        app_run = fin.read()
        fin.close()

        combine_file_content = app_init + app_index + app_run
        fout = open("demo.py", "w")
        fout.write(combine_file_content)
        fout.close()


    except Exception as e:
        print(str(e))

integrate()