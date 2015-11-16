Counting Islands
==============

You are required to develop an algorithm to count how many islands are in a given map. In order to simplfy the program, you are going to use a black and white based image represented by a matrix with 0s and 1s. The water in our map is represented by the 0s and the sand is represented by 1s. 

The following map representation has 4 islands.

|   | A | B | C | D | E | F | 
|---|---|---|---|---|---|---|
| **A** | 1 | 1 | 0 | 1 | 1 | 1 |
| **B** | 1 | 1 | 0 | 1 | 1 | 1 |
| **C** | 0 | 0 | 0 | 0 | 0 | 0 |
| **D** | 0 | 0 | 0 | 1 | 1 | 1 |
| **E** | 0 | 1 | 0 | 1 | 1 | 1 |
| **F** | 0 | 0 | 0 | 1 | 1 | 1 |

Therefore, the algorithm output should be 4.

Code snippet:

```java

    public int countIslands(int[][] map) {
      ...
      return numberOfIslands;
    }
```

*Note: No I/O is necessary, it is suitable to provide a test case which can be used to pass the matrix example.*

References:

[Beggining with Arrays and Matrices][1]

[1]: http://mathbits.com/MathBits/Java/arrays/Matrices.htm
