#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ryan Lin Xiang
# DATE CREATED:             14th Jan 2020                     
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
  
    
    # read pet images directory and save file names to the list filename_list
    filename_list = listdir(image_dir)
    
    #initiate dictionary results_dic
    results_dic = dict()
   
    #iterate through filename_list and format each filename in the way described above to that it can be later compared with the classifier output
    #strip filename by underline to rebuild it later 
    for file in filename_list:
        filename = file
        
        if not filename.startswith("."):
                        
            filename = file.split(".")[0]
            
            if "_" in filename:                       
                filename_lower_splitted = filename.strip().lower().split('_')
        
                label = ""
        
                #rebuild the stripped filename by replacing underline with space
                for word in filename_lower_splitted:
                    if word.isalpha(): #only alphabetic parts of the stripped filename are considered so that the file endings are removed
                        label += word + ' '
        
                label = label.strip()
            else:
                label = filename.strip().lower()
                                  
            #build key names of results_dic with the formatted labels
            if label not in results_dic: #avoid redundant key names
                results_dic[filename] = [label]        
                  
    return results_dic
