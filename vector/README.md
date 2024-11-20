### VECTOR

>  This exercise is good fro practicing method overloading. It implements a `Vector` class. This class will be a matrix with size 1xN or Nx1 where N is any positive number.
>
>This class has defined the methods for the operators `+ - * /` which will apply the corresponding operation for each pair of numbers from the two vectors. Dot product and transpose operations are also possible with Vector.dot() and vector.T().

> ### Methods:
> * **operator \+:**     
 Takes two vectors with same shape. The elements of the new vector will be: `new[i] = right[i] + left[i]`  
> * **operator \-:**     
 Takes two vectors with same shape. The elements of the new vector will be: `new[i] = right[i] - left[i]`  
> * **operator \*:**     
> Takes two vectors with same shape. The elements of the new vector will be: `new[i] = right[i] * left[i]`  
> * **operator \/:**     
Takes two vectors with same shape. The elements of the new vector will be: `new[i] = right[i] / left[i]`  
> 
> * **vector.T():**
 This method transposes a vector. If vector.shape equals to `n x m` then the after calling this method vector.shape will equal `m x n`. Notice that n or m are equal 1.
>
>* **Vector.dot(vector1, vector2):**
> This is a static method. It will receive two vectors with same shape it will call normal addition on them and then will return the sum of all the elements in the new vector. So result = sum(leftVector + rightVecotr)