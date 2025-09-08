import os 
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"{filename}: created successfully")
            
    except FileExistsError:
        print(F'{filename} already exists')
        
    except Exception as E:
        print('An error occur')


def view_all_files():
    files = os.listdir()
    if not files:
        print('No file found')
    else:
        print('Files in directory')
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted')
    except FileNotFoundError:
        print('File not found')
        
    except Exception as e:
        print('An error Occured')
        
def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content of '{filename} :\n{content}")
    
    except FileNotFoundError:
        print(f"{filename} dosent exist")
        
    except Exception as e:
        print('An error occured')
          
        

def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print(f'content added to {filename} successfully')

    except FileNotFoundError:
        print(f"{filename} dosen't exist")
        
    except Exception as e:
        print('An error occured')
        

def main():
    while True:
        print('File Management App')
        print('1: Create')                 
        print('2: view all')
        print('3: Delete')
        print('4: read File')
        print('5: Edit FIle')
        print('6: Exit')
        
        choice = input('Enter your choice (1-6) = ')
        
        if choice == '1':
            filename = input("Enter the file-name to create = ")
            
        elif choice == '2':
            view_all_files()
        
        elif choice == '3':
            filename = input('Enter the name of file')
            delete_file(filename)
            
        elif choice == '4':
            filename = input('edit the file you want to edit')
            read_file(filename) 
            
        elif choice == '5':
            filename = input('edit the file you want ot edit') 
            edit_file(filename)
            
        elif choice == '6':
            print("closing the app")
            break
        else:
            print("Invalid Option") 
            



if __name__ == "__main__":
    main()
               
                     