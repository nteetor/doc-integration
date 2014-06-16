
The goal of this project was to create a program that could, based on semantic analysis, properly integrate
text back into the larger body of text from which it was pulled.

This project was built entirely offline and thus is not as github friendly as could be. 

A set of just under 17,000 Wikipedia articles was selected from a much larger set of articles. Each of the selected articles needed to have at least 600 words. This minimum was put in place to help ensure each article had multiple paragraphs and was content rich.

For each article/file the program would randomly select a paragraph, remove it from the text, and use each of the three similarity functions to place the paragraph back into the file text.

The similarirty functions worked as follows: given the removed paragraph and two consecutive paragraphs from the article they calculated a similarity score. If a score was high enough the program determined that the removed paragraph belonged, i.e. was originally in between, the two paragraphs. This result along with semantic composition of the article was written to a CSV file for analysis.

Analysis of the results was done in R, see the RStuff.R file. The writeup gives a much better description and explanation of the project and the similarity functions. It can be found publicly through my Google drive by following this link: [final writeup](https://drive.google.com/file/d/0B0ncyoo8Ec15a0lYNlVIU2VJa2M/edit?usp=sharing).

===============

A document integration project. Taking a paragraph from a text, can the program insert the paragraph, correctly, back into the text.
