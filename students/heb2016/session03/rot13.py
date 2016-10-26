

def rot13(response):
        encryp_response=''
        row=0
        while row <= len(response)-1:
            if row==0:
                encryp_respons=response[row]
            if alpha.rfind(response[row]) ==-1:            
                encryp_response= encryp_response+response[row]
                

            elif alpha.rfind(response[row])< (26-13-1):
                encryp_response = encryp_response+alpha[response.rfind(response[row])+13]
            elif alpha.rfind(response[row])>= (26-13-1):
                encryp_response= encryp_response+alpha[13-(26-response.rfind(response[row]))]
            print(response[row], row, alpha.rfind(response[row]), encryp_response)
            row+=1
        print("Encryped text is: ", encryp_response)
        return(encryp_response) 




alpha='abcdefghijklmnopqrstuvwxyz'

def main():
    print ('Please type a new encryption text')
    response = input("===> ")
    print(response)
    rot13(response)
    
    return()


if __name__=="__main__":

    main()
    
