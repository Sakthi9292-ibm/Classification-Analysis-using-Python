# Classification-Analysis-using-Python

1.Logistic Regression Analysis 

Logisctic Regression is Applicable when we are working with catogorical variable. 

when the y  takes values zero and one, Logistic regression assumes our dataset follows logistic (sigmoid function) which is a "S" Shaped curve

where y is 

                  y = 1/(1+e^-x)
                  
 so , we need to covert our model dataset in the above form to determine the value of y ,such that , y takes value from 0 to 1 
 
 
 y = a +b1x1+b2x2+.....+bnxn
 
 in order to follow logit function , p should be between 0 and 1 
 
  p = e^y / (1+e^y)  
 
  
  # Bayes Therom 
  
  Navies- Bayes classifieris wased o*(p(s|male)* the bayes therom which determines the probablilty of an event in the presence of the other eent
  
  
  
  
  P(H|E) =P(E|H)*P(H)/P(E)
  
  P(H/E) = probaility of H given E 
  
  p(E/H) = Probability of E given H 
  
  
  
  for eg :  finding the probability of finding a person is male of female based on the height , weight , shoe size is given 
  
  
  p(Males|h,w,s) = p(male)*(p(h|male)*(p(w|male)*(p(s|male)
  
  
 where p(h|male) - follows the normal distribution which is proportional to the guassian density function 
 
 
https://en.wikipedia.org/wiki/Normal_distribution where u can find the formula for it . using this , by sending the values of height, weight , shoe size, we will be able to get the probalilty for male 


simillarly for female. based on the comparison , we can conclude the prediction 



# Decision Tree 

As name conveys , it a tree based structure. where key lies in finding the root node and child nodes below it. 

To find the root node , we need to calculate the totol entropy and then Information gain for each feature and select the feature with highest IG as a root node


once root node is selected , then follow the same procedure for finding the successive nodes below it 

E0 = Sum(-pi log2(pi)) 

where pi - probalility of the event ( yes or no) from total obseratvation . if i takes two values , i will be 2 


IG  for a feature 

      IG = E0 - sum(Ni/n)Si
      
      
       where Ni is Number of the event occurence of the feature , total observation, 
       Si is the entropy of the event 
       
 follow the procedure til decision arrives at each branch 
 
 
 
 Please find the Python code attached for those classifiers 










 
 
 
 
 
