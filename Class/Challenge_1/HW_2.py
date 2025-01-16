# HW - 2 - OOP - Classes - What vs How 


"""
1) Task:
○ What: Sum from 1 to N in 2 ways
○ How: Explain 2 approaches to implement above task

A:
- first to calculate sum from 1 to N we can initialize variable with init_val=0 and
loop from i=1 to N and increment the variable with i 

- secend if the numbers from 1 to N we can calculate it with mathemitical equation sum = ( N * (N+1) ) / 2

- the first approaches take O(N) time complexity but the mathemitical equation take O(1) time complexity

"""

"""
2) Snapseed is an app for Image Manipulation (e.g. crop, rotate, draw, etc)
    ○ It is available for Android, IOS, IPAD
    ○ In terms of what & how: provide some insights
        ■ E.g. method to fill color in rectangle?
        ■ E.g. method to read image from device?
    ○ Imagine we found a bug in some function
        ■ Or faster way to do it
        ■ How to structure our app code base
                to do the minimum code changes?

A:
1. Functional Insights for Snapseed

Image Manipulation Features: Highlighting its main features like cropping, rotating, drawing, adding filters.
Filling a Rectangle with Color: Which algorithms or libraries might be used.
Reading an Image from the Device: Which APIs are used for reading images.


2. Handling Bugs or Optimization

Identify a function that has a bug or is inefficient.
Suggest a faster or more efficient way to perform that operation such as optimizing algorithms or leveraging native librarie.


3. Codebase Structuring

Modular Architecture: Dividing the app into reusable and independent modules.
Abstract Layers: Using interfaces or abstract classes for core functionalities, making it easier to swap implementations.
Dependency Injection: To decouple components and allow seamless updates.
Testing and Versioning: Unit testing critical components and maintaining version control for smooth updates.

"""