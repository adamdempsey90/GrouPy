
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.image as image
get_ipython().magic('matplotlib inline')


# In[14]:

class Person(): 
    def __init__(self, name, img=None):
        self.name = name
        if img is not None:
            self.img = img
        
        self.partners = [self.name]
    
    def add_partner(self,person):
        if person.name not in self.partners:
            self.partners.append(person.name)
            person.partners.append(self.name)
            return True
        else:
            return False

    def clear_partners(self):
        self.partners = [self.name]
    def remove_last_partner(self):
        self.partners = self.partners[:-1]
    
    def check_availability(self,people):
        for person in people:
            if person.name not in self.partners:
                return True
        return False
    
    def __eq__(self,person):
        try:
            return self.name == person.name
        except AttributeError:
            return False
    def __neq__(self,person):
        return not self.__eq__(person)
    
    def __repr__(self):
        return self.name

class Pool():
    def __init__(self, people):
        """ Initialize a pool of players. """
        self.items = []
        self.pairs = []
        for person in people:
            self.push(person)
    
    def push(self,person):
        """ Add a new person to the stack."""
        self.items.append(person)
    def replace(self, person):
        """ Add a person into the stack at the bottom."""
        self.items = [person] + self.items
    def pop(self):
        """ Remove the last person added to the stack."""
        return self.items.pop()
    def size(self):
        """ How many players do we have left."""
        return len(self.items)
    def empty(self):
        """ Return True if everyone has been paired."""
        return self.size == 0
    def shuffle(self):
        import random
        random.shuffle(self.items)
    def compare(self, bachelor, bachelorette):
        return bachelorette.name in bachelor.partners
    def swap(self,bachelor):
        """ Look through the pairs and try to swap partners"""
        
        count = 0
        while count < len(self.pairs):
            pair = self.pairs.pop()
            if pair[0].name not in bachelor.partners and pair[1].check_availability(self.items):
                # Try to swap with the first person
                pair[0].remove_last_partner()
                pair[1].remove_last_partner()
                bachelor.add_partner(pair[0])
                self.push(pair[1])
                return bachelor, pair[0]
            if pair[1].name not in bachelor.partners and pair[0].check_availability(self.items):
                # Try to swap with the second person
                pair[0].remove_last_partner()
                pair[1].remove_last_partner()
                bachelor.add_partner(pair[1])
                self.push(pair[0])
                return bachelor, pair[1]
            self.pairs = [pair] + self.pairs
            count += 1
            
        # We've exausted all possible pairs
        return None
    def pair(self):
        bachelor = self.pop()
        count = 0
        tot = self.size()
        while count < tot:
            bachelorette = self.pop()
            if bachelor.add_partner(bachelorette):
                return bachelor, bachelorette
            else:
                self.replace(bachelorette)
                count += 1

        # If we've gotten here, we went through the whole stack
        return self.swap(bachelor)
    def pair_all(self):
        self.shuffle()
        while self.size() > 0:
            res = self.pair()
            if res is not None:
                self.pairs.append(res)
        
       
    def pairplot(self,people, axes=None):
        num = len(people)
        if axes is None:
            fig, axes = plt.subplots(1,num)
        for ax,person in zip(axes,people):
            ax.imshow(image.imread(person.img))
            ax.set_title(person.name)
            ax.axis('off')
    def show_all(self, **kwargs):
        figsize = kwargs.pop('figsize',(10,2*len(self.pairs)))
        fig,axes = plt.subplots(len(self.pairs),2,figsize=figsize)
        for ax,pair in zip(axes,self.pairs):
            self.pairplot(pair,axes=ax)
        plt.show()
    def __repr__(self):
        for item in self.items:
            print(item)
        return '{:d} participants'.format(self.size())

def next_round(people,**kwargs):
    pool = Pool(people)
    pool.pair_all()
    if len(pool.pairs) > 0:
        pool.show_all(**kwargs)
    else:
        print('Everyone has been paired up!')


# In[15]:

import glob
filenames = glob.glob('imgs/*')
names = [x.split('imgs/')[1].split('.')[0].title() for x in filenames]

people = [Person(name,img=fname) for name,fname in zip(names,filenames)]
for p in people:
    p.clear_partners()
pool = Pool(people)


# ## Round 1

# In[17]:

next_round(people)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 2

# In[296]:

next_round(people)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 3

# In[300]:

next_round(people)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 4

# In[298]:

next_round(people)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 5

# In[289]:

next_round(people,figsize=figsize)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 6

# In[290]:

next_round(people,figsize=figsize)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 7

# In[291]:

next_round(people,figsize=figsize)
for p in people:
    print(p.name + ': ', p.partners)


# ## Round 8

# In[292]:

next_round(people,figsize=figsize)
for p in people:
    print(p.name + ': ', p.partners)


# In[9]:

for i in range(len(people)-1):
    next_round(people)


# In[8]:

next_round(people)


# In[ ]:



