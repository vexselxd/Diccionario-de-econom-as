while True:
    economy_dict = {
                "Liberal": "Vela de que el Estado tenga poca o nula intervencion en la economia",
                "Intervencionista": "Vela por que el Estado intervenga en la economia",
                "Autocrata": "Vela de que el Estado se vuelva autosuficiente y no depender de nadie"
                }
    
    economy = input("Escribe un tipo de economia que quieras ver.(Liberal, Intervencionista o Autocrata, con mayusculas!)")
    
    if economy in economy_dict.keys():
        print(economy_dict[economy])
    else:
        print("Lo siento no tengo registrada ese tipo de economia")
        
