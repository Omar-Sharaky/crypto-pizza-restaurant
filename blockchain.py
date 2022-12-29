import json
import os
import hashlib
# For timestamp
import datetime
#getting diretory of the blockchain folder 
BLOCKCHAIN_DIR='blockchain/'

#function to get the hash of the previous block
def get_hash(prev_block):
    # rb means opening the file in binary format
    with open(BLOCKCHAIN_DIR+prev_block, 'rb') as f:
        content=f.read()
    return hashlib.sha256(content).hexdigest()

#function to check integrity of the blocks
def check_integrity():
    #listing files sorted in the blockchain
    files= sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    


    for file in files[1:]:
        with open(BLOCKCHAIN_DIR+file)as f:
            block=json.load(f)
            #getting the variable of the hash and filename of previous blcok
        prev_hash=block.get('prev_block').get('hash')
        prev_filename=block.get('prev_block').get('filename')
        #getting the hash of the pervious file using the same hashing function (algorithm)
        actual_hash=get_hash(prev_filename)
        #comparing the prev_hash wuth actual hash to check if any modification has occurred 
        if prev_hash==actual_hash:
            #not modified
            res='ok'
        else:
            #modified
            res='was Changed'
            #changed a feature in the function
        print('block:', prev_filename, ",result:",res)
        
    
#Writing block of each order confirmed 
def write_block(OrderNO, UserName, amount):
    #getting number of blocks
    blocks_count=len(os.listdir(BLOCKCHAIN_DIR))
    prev_block=str(blocks_count)
    #data instide each block
        #Orderno, Username, amount VALUES are retrived from the views.py with each confirm_order function
        #Prev hash and prev filename are computed each single time  
    data={
        "OrderNO":OrderNO,
        "UserName":UserName,
        "amount":amount,
        'timestamp': str(datetime.datetime.now()),
        "prev_block":{
            "hash":get_hash(prev_block),
            "filename":prev_block
        }

    }
    #creating file name   #16,17,etc
    current_block=BLOCKCHAIN_DIR+ str(blocks_count+1)
    #writing data into the file 
    with open(current_block,'w')  as f:
        json.dump(data,f,indent=4, ensure_ascii=False)
        f.write('\n')

def main():
  
    check_integrity()

if __name__=='__main__':
    main()