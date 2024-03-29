
import unittest
from bookLover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        result=bl.book_list.loc[bl.book_list['book_name']=='pride and prejudice']
        self.assertTrue(len(result)==1,'book was not found')
    
    def test_2_add_book(self):
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        bl.add_book('pride and prejudice',5)
        result=bl.book_list.loc[bl.book_list['book_name']=='pride and prejudice']
        self.assertTrue(len(result)==1,'book was added more than once')
                
    def test_3_has_read(self): 
            
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        self.assertTrue(bl.has_read("pride and prejudice"),"pride and prejudice not read")


        
    def test_4_has_read(self): 

            
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        self.assertFalse(bl.has_read("Titanic"),"Titanic was read")
        
    def test_5_num_books_read(self): 
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        bl.add_book('to kill a mocking bird',5)
        bl.add_book('1985',3)
        
        print(bl.num_books)
        self.assertTrue(bl.num_books==3,'number of books mismatch')

    def test_6_fav_books(self):
        bl=BookLover("venkat","venkat@virginia.edu","fiction")
        bl.add_book('pride and prejudice',5)
        bl.add_book('to kill a mocking bird',5)
        bl.add_book('1985',3)
        bl.add_book('october revolution',2)
        
        print(len(bl.fav_books()))
        self.assertTrue(len(bl.fav_books())==2,'favorite  books mismatch')       
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)