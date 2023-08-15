# ColourDetectorApp
## A visual aid using machine learning and computer vision to classify rudimentary colours from RGB pixel values in real-time using a standard USB camera.
### Thorne, J. & Baldock, R.A.* (2023)
*School of Pharmacy and Biomedical Science, University of Portsmouth, Portsmouth, PO1 2DT, UK. 

**Overview**

Colourblindness is a common visual impairment affecting approximately 8% of males and 0.5% of females [1]. It is characterized by difficulties in perceiving certain colours. This condition, often stemming from genetic factors, impacts individuals across various demographic groups [2]. Colourblind individuals encounter challenges in tasks ranging from daily activities like distinguishing traffic lights to professional activities or laboratory work, where colour differentiation is crucial. This disparity underscores the importance of technological interventions to create more equitable opportunities for those with colour vision deficiencies [3].

Advancements in technology, particularly in the realms of machine learning and computer vision, offer promising avenues to address the obstacles faced by colourblind individuals including aiding diagnosis [4]. By harnessing the capabilities of these technologies, it becomes possible to provide real-time assistance to users, allowing them to perceive and distinguish colours accurately. Such solutions hold the potential to significantly enhance the independence for individuals with colour vision deficiencies. Furthermore, the integration of technology in this context emphasizes the broader societal commitment to inclusivity and accessibility [5]. 

Here we develop a *ColourDetectorApp* using machine learning and computer vision to classify rudimentary colours using RGB pixel values obtained through a standard USB camera. By training a logistic regression algorithm, the app accurately interprets these values and provides real-time colour labels. Critically, we hope to see this technology developed further to promote equitable opportunities for colourblind individuals. 

**Data Processing**

The colour names dataset was downloaded from Kaggle (available from: https://www.kaggle.com/datasets/avi1023/color-names). The dataset contains colour labels and RGB values for 1298 colours. The dataset was simplified by subsetting for colour labels containing key labels to be classified in the final model (i.e. 'blue', 'red', 'green', 'white', 'grey', 'yellow', 'pink', 'orange', 'purple', 'black'). The simplified dataset contained 311 colour labels and associated RGB values. The distribution of classes in the resulting dataset are not evenly distributed. In some cases, a specific colour label and associated RGB value may only feature once. To overcome this, random oversampling using the imbalanced-learn python library was used to avoid introducing bias into the algorithm. Random oversampling artificially increases the representation of minority classes through the duplication of instances. After oversampling, a dataset of 860 colours were then used to train and test the algorithm. A training and testing dataset was created by splitting the data. 80% of the data are contained within the training set, while a 20% holdout set was assigned to the testing set. The Scikit-Learn python library was used to train the machine learning algorithm. 

**Results**

A logistic regression model was trained on the training dataset. Once trained, the model was used to predict colour classifications on the holdout 'testing' dataset. Classification accuracy of the model is shown in the confusion matrix below. 

<img width="349" alt="image" src="https://github.com/RA-Baldock/ColourDetectorApp/assets/79604468/67258e43-9630-43ce-8c0a-29af9007af4e">

Figure 1 – A confusion matrix showing the accuracy of predicted classes on the testing dataset.

<img width="301" alt="image" src="https://github.com/RA-Baldock/ColourDetectorApp/assets/79604468/5b5772d3-fde9-4628-b8b4-24308f37c2e4">

Figure 2 - Classification report of model accuracy.

**References**

1.	Jha, R., Khadka, S., Gautam, Y., Bade, M., Jha, M. J., Nepal, O. (2018). Prevalence Of Color Blindness In Undergraduates Of Kathmandu University. Journal of Nepal Medical Association, 214(56), 900-903. https://doi.org/10.31729/jnma.3913

2.	Neitz, J. and Neitz, M. (2011). The Genetics Of Normal and Defective Color Vision. Vision Research, 7(51), 633-651. https://doi.org/10.1016/j.visres.2010.12.002

3.	Cumberland, P., Rahi, J. S., & Peckham, C. S. (2004). Impact of congenital colour vision deficiency on education and unintentional injuries: findings from the 1958 British birth cohort. BMJ (Clinical research ed.), 329(7474), 1074–1075. https://doi.org/10.1136/bmj.38176.685208.F7 

4.	Wang, J., Wang, S., & Zhang, Y. (2023). Artificial intelligence for visually impaired. Displays, 77, 102391. https://doi.org/https://doi.org/10.1016/j.displa.2023.102391 

5.	R. Alashkar, M. ElSabbahy, A. Sabha, M. Abdelghany, B. Tlili and J. Mounsef, "AI-Vision Towards an Improved Social Inclusion," 2020 IEEE / ITU International Conference on Artificial Intelligence for Good (AI4G), Geneva, Switzerland, 2020, pp. 204-209, doi: 10.1109/AI4G50087.2020.9311049.  
