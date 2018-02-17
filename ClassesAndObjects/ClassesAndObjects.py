#!/usr/bin/python

class DatabaseAccess:
    mDbQuery = "Test";

    #Constructor for the Database Class
    def __init__(self,str):
      self.mDbQuery = "Test Value changed from constructor"

    def DisplayValue(self):
        print self.mDbQuery;



        
mDao = DatabaseAccess("test");
mDao.DisplayValue();
print(hasattr(mDao,"mDbQuery"));

print(getattr(mDao,"mDbQuery"));

print(mDao.mDbQuery);

setattr(mDao,"mDbQuery","Value Changed");

__del__();


