# class Banckaccount:
#     def __init__(self):
#         self.__blance = 10 

#     def __get_ammount(self):
#         return self.__balance

# obj = Banckaccount()
# print(obj.__get_ammount())



# wap to deffrent to publice ,protcat,privet

# publice is al all code publice showing 
# protcat is a cover code is another code is no join us 
# priver is privet mode


class A:
    def __init__(self, name,):
     self.name = name
     
       
obj = A("ram")
print(obj.name)


class B:
   def __init__(self,gender):
      self._gender = gender

   def get_gender(self):
      return self._gender

obj = B("meal")
print(obj._gender)


class C:
   def __init__(self,food):
      self.__food = food

   def get_food(self):
      return self.__food
   
   
      

obj = C("rice")
print(obj.get_food())