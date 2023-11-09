# Textil Classification 

**Team**
- [Fernando Castro Mendieta](https://github.com/Fercho524)
- [Flor Arlette Vargas Soriano](https://github.com/FAVS07)
- Arturo Vázquez Lona 

## Part 01 Data Adquisition

Given diferent type of Mexican Textiles The task should be, group it using clustering algorithms. All the images was downloaded from Google and resized to 224x224.

![Textiles](/docs%20images/image.png)

The final non labeled dataset could be found here : https://www.mediafire.com/file/xgjtpj9pxbaly2q/UnlabeledData.zip/

## Part 02 Data Preprocessing

All the images was processed using the VGG16 Network, and the image embedding was taken from the penultimate layer. This vectors will be used on the classification process.

![Alt text](/docs%20images/image-1.png)

## Part 03 Clustering

In this part, we have now the embeddings, the algorithms applied here was the next:

- K-Means
- Hierarchical Clustering

And the results were:

![Alt text](/docs%20images/image-4.png)

## Part 04 Regression

The clustering algoritms was used to tag all the images, ideally with the labels defined at the time of downloading the data, and, with this tagged images, we can work as a supervised machine learning schema.

The algorithms used on this part were :

- Multiple Linear Regression
- Polynomial Regression
- Support Vector Regression
- Random Forest
- Decision Tree Regression

The results were

![Alt text](/docs%20images/image-6.png)

## Part 05 Classification 

This part is the same that the regression part, we use the non supervised tagged data as the correct labels to classify the textiles, and the used algorithms were:

- KNN
- Naive Bayes
- SVM with Linear Kernel
- SVM with Gaussian and Polynomial Kernel
- Random Forest
- Decision Tree

![Alt text](/docs%20images/image-7.png)

## More Information

More information about the process on the 
jupyter notebooks.