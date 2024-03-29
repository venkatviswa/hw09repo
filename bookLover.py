#!/usr/bin/env python3
import pandas as pd
class BookLover:
    def __init__(self,name,email,fav_genre,num_books=0,book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books=num_books
        self.book_list=book_list
    
    def add_book(self,book_name, rating):
        #print('adding book')
        result=self.book_list[self.book_list['book_name']==book_name]
        print(len(result))
        if len(result)==1:
            print('book already exists')
        else:
            print('book being added')
            new_book = pd.DataFrame({
                'book_name': book_name,
                'book_rating': rating
            },index=[book_name])
            self.book_list = pd.concat([self.book_list, new_book])
            self.num_books+=1

    def has_read(self,book_name):
        try:
            result=self.book_list[self.book_list['book_name']==book_name]
            print(len(result))
            if len(result)==1:
                return True
            else:
                return False
        except KeyError:
            print("book not found")
            return False

    def num_books_read(self):
        return self.num_books
    def fav_books(self):
        return(self.book_list[self.book_list['book_rating']>3])


if __name__=="__main__":
    bl=BookLover("venkat","venkat@virginia.edu","fiction")
    print(bl.email)
    #print(bl.book_list)
    bl.add_book('autobiography of a yogi',5)
    bl.add_book('autobiography of a yogi',4)
    #print(bl.book_list)
    print(bl.has_read('xyz'))
    print(bl.has_read('autobiography of a yogi'))
    print(bl.num_books_read())
    print(bl.fav_books())
    

        