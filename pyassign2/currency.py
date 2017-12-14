
# coding: utf-8

# In[11]:


"""currency.py: This python checks money exchanging rates.

__author__ = "Kow Pu Ern"
__pkuid__  = "1700094617"
__email__  = "newbieern2@hotmail.com"
"""

from urllib.request import urlopen

#This function locates a string in a list
def index_lookup(arr,item):
    return [i for i,a in enumerate(arr) if a==item]

#This function removes unwanted characters in output string
def remove(s):
    a = "b" + "'" + '"'
    b = ""
    for eachChar in s:
        if eachChar not in a:
            b = b + eachChar
    return b

#Currenct exchanging function
def exchange(currency_from, currency_to, amount_from):    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from, currency_to, amount_from))
    doc_line1 = doc.read()
    doc.close()
    doc_list = doc_line1.split()
    n = index_lookup(doc_list,b'"to"')
    m = int(n[0]) + 2
    output_raw = str(doc_list[m])
    output_curr = remove(output_raw)
    return(output_curr)

#Testing functions.
def test_A():
    assert (exchange('USD','EUR','130') == str(108.95235))
    
def test_B():
    assert (exchange('TWD','MYR','100') == str(14.060022109734))

def testall():
    test_A()
    test_B()
    print("All tests passed")
    
#Main timeline
def main():
    a = input()
    b = input()
    c = input()
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)
    print (exchange(a,b,c))

if __name__ == '__main__':
    testall()
    main()

