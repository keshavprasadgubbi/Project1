# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os
  
# Function to rename multiple files 
def main(): 
    i = 378
      
    for filename in os.listdir("/Users/keshavaprasad/Desktop/Internship/Images-Landmarks/"): 
        dst ="Label" + str(i) + ".tif"
        src ='image_50/Labels_50/'+ filename 
        dst =''+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# DriverCode 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 