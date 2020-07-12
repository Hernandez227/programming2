# Files in C 

## Team members: 
[Erick Hernandez](https://github.com/Hernandez227/programming2)

[Eduardo Uicab](https://github.com/Eduardobricenio/programming2)


## One - dimensional
A one-dimensional array is a structured collection of components (often called array elements) that can be accessed individually by specifying the position of a component with a single index value. int number[50]; creates the number array which has 50 components, each capable of holding one int value.

## Multidimensional
 
 Is an array with more than two dimensions. Each element is defined by two subscripts, the row index and the column index. Multidimensional arrays are an extension of 2-D matrices and use additional subscripts for indexing.

# Concep of a data file 
The file system is the most viable aspect of an operating system.
It provides the mechanism for on line storage of and access to both data and programs of the operating system and all the users of the computer system.   The file system consists of two distinct parts: a collection of files, each storing related data, and directory structure, which organizes and provides information about all the files in the system.  Some file systems have a third part, partitions, which are used to separate physically or logically large collection of directories. 

## Text file

On a computer, every file is a long string of ones and zeros. Specifically, a file is a finite-length sequence of bytes, where each byte is an integer between 0 and 255 inclusive (represented in binary as 00000000 to 11111111). Files can be broadly classified as either binary or text. These categories have different characteristics and need different tools to work with such files.

## Binary file 
A binary file is a computer file that is not a text file.[1] The term "binary file" is often used as a term meaning "non-text file".[2] Many binary file formats contain parts that can be interpreted as text; for example, some computer document files containing formatted text, such as older Microsoft Word document files, contain the text of the document but also contain formatting information in binary form.




# How to create a file 

	FILE *fp;  
	fp = fopen ("file_name", "mode");
In the above syntax, the file is a data structure which is defined in the standard library.

fopen is a standard function which is used to open a file.

    If the file is not present on the system, then it is created and then opened.
    If a file is already present on the system, then it is directly opened using this function.

fp is a file pointer which points to the type file.

Whenever you open or create a file, you have to specify what you are going to do with the file. A file in 'C' programming can be created or opened for reading/writing purposes. A mode is used to specify whether you want to open a file for any of the below-given purposes. Following are the different types of modes in 'C' programming which can be used while working with a file. 

## File mode and description

* r : Open a file for reading. If a file is in reading mode, then no data is deleted if a file is already present on a system. 
* w : Open a file for writing. If a file is in writing mode, then a new file is created if a file doesn't exist at all. If a file is already present on a system, then all the data inside the file is truncated, and it is opened for writing purposes. 
* a : Open a file in append mode. If a file is in append mode, then the file is opened. The content within the file doesn't change. 
* r+ : Open for reading and writing from beginning 
* w+ : Open for reading and writing, overwriting a file 
* a+ : Open for reading and writing, appending to file 

In the given syntax, the filename and the mode are specified as strings hence they must always be enclosed within double quotes. 

## Example: 

	#include <stdio.h>
	int main() {
	FILE *fp;
	fp  = fopen ("data.txt", "w");
	}

Output: File is created in the same folder where you have saved your code. 

You can specify the path where you want to create your file

## Example: 
	#include <stdio.h>
	int main() {
	FILE *fp;
	fp  = fopen ("D://data.txt", "w");
	}

# How to close a file 
One should always close a file whenever the operations on file are over. It means the contents and links to the file are terminated. This prevents accidental damage to the file.
'C' provides the fclose function to perform file closing operation. The syntax of fclose is as follows: 

	fclose (file_pointer);

An example of this: 

	FILE *fp;
	fp  = fopen ("data.txt", "r");
	fclose (fp);

The fclose function takes a file pointer as an argument. The file associated with the file pointer is then closed with the help of fclose function. It returns 0 if close was successful and EOF (end of file) if there is an error has occurred while file closing. After closing the file, the same file pointer can also be used with other files. 

# Writing a file

In C, when you write to a file, newline characters '\n' must be explicitly added. The stdio library offers the necessary functions to write to a file:

  *  fputc(char, file_pointer): It writes a character to the file pointed to by file_pointer.
  * fputs(str, file_pointer): It writes a string to the file pointed to by file_pointer.
  *  fprintf(file_pointer, str, variable_lists): It prints a string to the file pointed to by file_pointer. The string can optionally include format specifiers and a list of variables variable_lists. 

The program below shows how to perform writing to a file in diferrents ways: 

## fputc() Function

	#include <stdio.h>
	int main() {
        int i;
        FILE * fptr;
        char fn[50];
        char str[] = "UPY\n";
        fptr = fopen("fputc_test.txt", "w"); // "w" defines "writing mode"
        for (i = 0; str[i] != '\n'; i++) {
            /* write to file using fputc() function */
            fputc(str[i], fptr);
        }
        fclose(fptr);
        return 0;
	    }


## fputs() Function

	#include <stdio.h>
	int main() {
        FILE * fp;
        fp = fopen("fputs_test.txt", "w+");
        fputs("This is an tutorial on fputs,", fp);
        fputs("We don't need to use for loop\n", fp);
        fputs("Easier than fputc function\n", fp);
        fclose(fp);
        return (0);
   	 }

## fprintf() Function 

	#include <stdio.h>
  	  int main() {
        FILE *fptr;
        fptr = fopen("fprintf_test.txt", "w"); // "w" defines "writing mode"
        /* write to file */
        fprintf(fptr, "Learning C with Guru99\n");
        fclose(fptr);
        return 0;
  	  }

# Reading data from a file 

There are three different functions dedicated to reading data from a file

*    fgetc(file_pointer): It returns the next character from the file pointed to by the file pointer. When the end of the file has been reached, the EOF is sent back.
*    fgets(buffer, n, file_pointer): It reads n-1 characters from the file and stores the string in a buffer in which the NULL character '\0' is appended as the last character.
*    fscanf(file_pointer, conversion_specifiers, variable_adresses): It is used to parse and analyze data. It reads characters from the file and assigns the input to a list of variable pointers variable_adresses using conversion specifiers. Keep in mind that as with scanf, fscanf stops reading a string when space or newline is encountered.

The following program demonstrates reading from fputs_test.txt file using fgets(),fscanf() and fgetc () functions respectively : 

	#include <stdio.h>
	int main() {
        FILE * file_pointer;
        char buffer[30], c;

        file_pointer = fopen("fprintf_test.txt", "r");
        printf("----read a line----\n");
        fgets(buffer, 50, file_pointer);
        printf("%s\n", buffer);

        printf("----read and parse data----\n");
        file_pointer = fopen("fprintf_test.txt", "r"); //reset the pointer
        char str1[10], str2[2], str3[20], str4[2];
        fscanf(file_pointer, "%s %s %s %s", str1, str2, str3, str4);
        printf("Read String1 |%s|\n", str1);
        printf("Read String2 |%s|\n", str2);
        printf("Read String3 |%s|\n", str3);
        printf("Read String4 |%s|\n", str4);

        printf("----read the entire file----\n");

        file_pointer = fopen("fprintf_test.txt", "r"); //reset the pointer
        while ((c = getc(file_pointer)) != EOF) printf("%c", c);

        fclose(file_pointer);
        return 0;
    	}

1.  In the above program, we have opened the file called "fprintf_test.txt" which was previously written using fprintf() function, and it contains "Learning C with Guru99" string. We read it using the fgets() function which reads line by line where the buffer size must be enough to handle the entire line.
2.    We reopen the file to reset the pointer file to point at the beginning of the file. Create various strings variables to handle each word separately. Print the variables to see their contents. The fscanf() is mainly used to extract and parse data from a file.
3. Reopen the file to reset the pointer file to point at the beginning of the file. Read data and print it from the file character by character using getc() function until the EOF statement is encountered
4.    After performing a reading operation file using different variants, we again closed the file using the fclose function.

## Interactive File Read and Write with getc and putc

These are the simplest file operations. Getc stands for get character, and putc stands for put character. These two functions are used to handle only a single character at a time.

Following program demonstrates the file handling functions in 'C' programming: 

	#include <stdio.h>
	int main() {
        FILE * fp;
        char c;
        printf("File Handling\n");
        //open a file
        fp = fopen("demo.txt", "w");
        //writing operation
        while ((c = getchar()) != EOF) {
            putc(c, fp);
        }
        //close file
        fclose(fp);
        printf("Data Entered:\n");
        //reading
        fp = fopen("demo.txt", "r");
        while ((c = getc(fp)) != EOF) {
            printf("%c", c);
        }
        fclose(fp);
        return 0;
  	  }
1.  In the above program we have created and opened a file called demo in a write mode.
2.    After a write operation is performed, then the file is closed using the fclose function.
3.   We have again opened a file which now contains data in a reading mode. A while loop will execute until the eof is found. Once the end of file is found the operation will be terminated and data will be displayed using printf function.
4.   After performing a reading operation file is again closed using the fclose function.


# Review of everything learned
## python 3

We first saw the basics of phon starting to see the variables and symbols of this new programming language for us.

## variables
A variable is a space to store modifiable data, in the memory of a computer. In Python, a variable is defined with the syntax:
variable_name = variable_value
Each variable has a name and a value, which defines, at the same time, the data type of the variable. There is a type of variable, called a constant, which is used to define fixed values, which

### Right
my_variable = 12

### Incorrect
MyVariable = 12
mivariable = 12

## Glossary

 - Text string (string):  my_cadena = "Hello World!"

- Comments: Comments on the same line of the code must be separated by two blank spaces. A single blank space must follow the # symbol. # Correct to = 15 # Age of Mary

- Tipos de datos complejos Python, posee además de los tipos ya vistos, 3 tipos más complejos, que admiten una colección de datos. Estos tipos son:
Tuplas
Listas
Diccionarios
Estos tres tipos, pueden almacenar colecciones de datos de diversos tipos y se diferencian por su sintaxis y por la forma en la cual los datos pueden ser manipulados.
- print (print): it serves to show in detail or that the programmer you want to capture
- - Lists: A list is similar to a tuple with the fundamental difference that it allows modifying the data once created: my_list = ['text string', 15, 2.8, 'other data', 25]
- While loop: This loop is in charge of executing the same action "while" a certain condition is met.
- For loop: The for loop, in Python, is the one that will allow us to iterate over a complex variable, of the list or tuple type.


~~~
== Same as 5 == 7 False
! = Other than red! = Green True
<Less than 8 <12 True
> Greater than 12> 7 True
<= Less than or equal to 12 <= 12 True
> = Greater than or equal to

~~~
























