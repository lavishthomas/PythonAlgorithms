'''
/** * find path [operand_expression...] * *

  Implement Linux find command as an API.

  The API will support finding files that:
  * - Files that have a given size requirement.
  * - Files with a certain naming pattern.

  * Simple example use cases:
  * - Find all files over 5 MB somewhere under a directory.
  * - Find all XML files somewhere under a directory.

  * * Create a library which allows this to be done easily.
  Keep in mind that these are just 2 uses cases
  and that the library should be flexible and extendable. */


  Assuming the following interface is given

  class File {
    List<File> listFiles() {} 
    List<String> list() {} path
    String getName() {}
    int getSize() {}
    boolean isDirectory() {}
 }
 '''
# directory = '\etc\usr'
size = ['>5000','<1000'] ## > 5000
filters = ['*.csv', '*.xml' ]
# directory = new File() 

find(directory, size , filters,  )
### 
 
find(directory -> File object, size_list= None, filter_list= None):
    
    file_list = []
    
    child_of_current = directory.listFiles()
        
    ### child_of_current []
    
    for child in child_of_current:
        if (isDirectory()):
            
            new_children = find(child, size , filter_list)
            file_list.extend(new_children)
            
        else
            size = child.getSize() 
            ### current files size
            for sizes in size_list:
                if sizes[0] == '<' and size < sizes [1:]
                    file_list.append(child)
            for filterr in filter_list:
                if filename = reg(filterr):
                    file_list.append(child)
        
    
     ## gives current dire
    
