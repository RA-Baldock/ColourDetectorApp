# ColourDetectorApp
## A visual aid using machine learning and computer vision to classify rudimentary colours from RGB pixel values in real-time using a standard USB camera.
### Thorne, J. & Baldock, R.A.* (2023)
*School of Pharmacy and Biomedical Science, University of Portsmouth, Portsmouth, PO1 2DT, UK. 

**Overview**

Colourblindness, a common visual impairment affecting approximately 300 million people globally, is characterized by difficulties in perceiving certain colours. This condition, often stemming from genetic factors, impacts individuals across various demographic groups, with a higher prevalence among males of Northern European descent. Colourblind individuals encounter challenges in tasks ranging from daily activities like distinguishing traffic lights to professional activities or laboratory work, where colour differentiation is crucial. This disparity underscores the importance of technological interventions to create more equitable opportunities for those with colour vision deficiencies.

Advancements in technology, particularly in the realms of machine learning and computer vision, offer promising avenues to address the obstacles faced by colourblind individuals. By harnessing the capabilities of these technologies, it becomes possible to provide real-time assistance to users, allowing them to perceive and distinguish colours accurately. Such solutions hold the potential to significantly enhance the independence for individuals with colour vision deficiencies. Furthermore, the integration of technology in this context emphasizes the broader societal commitment to inclusivity and accessibility. 

Here we develop a *ColourDetectorApp* using machine learning and computer vision to classify rudimentary colours using RGB pixel values obtained through a standard USB camera. By leveraging logistic regression algorithms, the app accurately interprets these values and provides real-time colour labels. Critically, we hope to see this technology developed further to promote equitable opportunities for colourblind individuals.

**Data Processing**
The colour names dataset was downloaded from Kaggle (available from: https://www.kaggle.com/datasets/avi1023/color-names). The dataset contains colour labels and RGB values for 1298 colours. The dataset was simplified by subsetting for colour labels containing key labels to be classified in the final model (i.e. 'blue', 'red', 'green', 'white', 'grey', 'yellow', 'pink', 'orange', 'purple', 'black'). The simplified dataset contained 311 colour labels and associated RGB values. The distribution of classes in the resulting dataset are not evenly distributed. In some cases, a specific colour label and associated RGB value may only feature once. To overcome this, random oversampling using the imbalanced-learn python library was used to avoid introducing bias into the algorithm. Random oversampling artificially increases the representation of minority classes through the duplication of instances. After oversampling, a dataset of 860 colours were then used to train and test the algorithm. A training and testing dataset was created by splitting the data. 80% of the data are contained within the training set, while a 20% holdout set was assigned to the testing set. The Scikit-Learn python library was used to train the machine learning algorithm. 

**Results**

A logistic regression model was trained on the training dataset. Once trained, the model was used to predict colour classifications on the holdout dataset. Classification accuracy of the model is shown in the confusion matrix below. 

<img width="349" alt="image" src="https://github.com/RA-Baldock/ColourDetectorApp/assets/79604468/67258e43-9630-43ce-8c0a-29af9007af4e">

Figure 1 – A confusion matrix showing the accuracy of predicted classes on the testing dataset.

<img width="301" alt="image" src="https://github.com/RA-Baldock/ColourDetectorApp/assets/79604468/5b5772d3-fde9-4628-b8b4-24308f37c2e4">

Figure 2 - Classification report of model accuracy.

