# Rock Type Classification applying Neural Network (Machine Learning)  
**Author by**: Pham Tien Duc  
![](../IMG/Untitled.png)  
In this project, I made the decision to analyze the data from the drilled wells and use machine learning to forecast the facies (lithology rock type) in the oil and gas field and to make predictions for other wells based on the model. Facies is a crucial predictor of where oil and gas are located, and there are challenges when there aren't enough data from rock sample. Using additional data and a machine learning technique is one of the best ways to interpret for Facie lithology rock type:  
* **Project Overview:** One of the most crucial responsibilities for geoscientists working on development and exploratory projects is the characterization of facies. The physical, chemical, and biological conditions that a unit underwent throughout the sedimentation process are reflected in the sedimentary facies. In this project, I will analyze the data from 4 wells and the well log information to create a model that will predict the facies-lithology rock type for further wells.
* **Problem Proposition:** In this study, machine learning algorithms (Neural Networks) are trained to predict facies from well log data using data from continuous logs (NPHI, RHOB, VCL, DT & and discrete log: Facies), in order to create a model for future facies forecast for another well without facies interpretation.
* **Metrics:** As a classification strategy in this research, we employed performance metrics including recall, accuracy, and F1-Score.  
<ul>My research concludes following step:
   <ul>
   <li>Exploratory Data Analysis</li>
   <li>Data processing</li>
   <li>Apply the classic machine learning with ANN neural network method</li>
   <li>Then, before modeling, we undertake feature engineering, scale the data, and discover and remove outliers to <strong>enhance the performance</strong>.</li>
   </ul> 
</ul>  

## Exploratory Data Analysis (EDA)   
**Dataset:** [Wells log](https://github.com/seg/tutorials-2016/tree/master/1610_Facies_classification)  
This well log file has over 27000 lines of data in it, including data on density porosity, bulk density, spontaneous potential, gamma rays, and resistivity. Small deep learning models can be trained and experimented with using the data.   
This is done in order to anticipate the litho-facies and gain significant insights from current well data.  
**Data Visualization**
![](../IMG/Visualizing%20data.png)
![](../IMG/Visualizing%20data%203.png)
As a result, it's critical to consider some of the following queries to provide more light on the issues:  
* The relationship between the additional factor and the litho-facies?  
* Which litho-facies' volume proportion is each?

**Remvove missing data**  
Remove abnormalities or characteristics about the data or input that need to be addressed have been identified.
 ![](../IMG/Remove%20Mising%20Data.png) 
**Question 1: The relationship between the additional factor and the litho-facies?**  
In order to determine which value has a better correlation with litho-facies, a scatter plot and a heatmap specifically were made to provide an answer.  
This will be a helpful factor to consider when choosing a model's features in the following modeling stage.  
![](../IMG/Untitled%20(1).png)  
We can see the strong association between GR, VCL, PHI, and Litho-Facies.

**Question 2: Which litho-facies volume proportion is each?**  
It will be necessary to analyze each facies' volume in order to determine which litho-facies make up the majority of our dataset and to use that information in modeling.  
Since there are more chances to reserve hydrocarbons in the oil and gas industry when there is more sand present, this analyst can provide us with a clear picture of our reservoir in the field or in the most recent dataset.  
The bar chart will enable you to observe the various volume fractions of sand and shale as shown below:  
![](../IMG/Untitled%20(2).png)  
As can be seen, shale outperforms sand in terms of worldwide statistics.  
## Data Preprocessing  
The data process and data engineering must be made in order to:  
* Scale data by utilizing a reliable scaler, then transform  
* Utilized the isolation forest technique for outlier detection and removal.  
Along with the issue of having insufficient data for rock samples to feed the model (Wells formation), the data imbalance between well types (Shale and Sand) is a major issue.

There are some additional data from the [National Geological and Geophysical Data Preservation Program](https://www.usgs.gov/programs/national-geological-and-geophysical-data-preservation-program/well-log-data)
## Methodology  
This study employs an artificial neural network (ANN) technique for categorization. The post's conclusion provides a summary of the outcomes of this strategy.  
![](../IMG/Accuracy%20Evaluation.png)
With this as a [guide](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html), the aforementioned algorithms were simple to build.  
Scikit-Learn created this library. An estimator for classification in scikit-learn is a Python object that carries out the operations fit(X_train, y_train) and predicts(X_test).    
![](../IMG/Data%20Split.png)
Divide the datasets in a ratio of 70:30 between training and test data.  
![](../IMG/7030.png)  
**Outlier Detection: Isolation Forest**
![](../IMG/Outlier%20Detection%20Isolation%20Forest%201.png)
![](../IMG/Outlier%20Detection%20Isolation%20Forest%202.png)
## Hyperparameter tuning  
The loop method, the number of interactions, and the number of layers were adjusted to reach a high level of accuracy on the training set as follows:   
And from The Multi-Layer Perceptron ( A Neural Network Implementation in Sklearn) library of sklearn with grid search cv to find out the best parameter apply for model  
In addition, from the Sklearn Multi-Layer Perceptron (A Neural Network Implementation) package, use grid search cv to choose the optimal parameter to apply for the model. 
![](../IMG/Tuning%20Hyperparameters.png) 
![](../IMG/Multi-Layer%20Perceptron.png)  
**Observations**  
- After applying the tuning method in hyperparameters, we could improve the metrics containing accuracy and F1_score
- For more information about the comparison between Accuracy and F1_score  

## Result  
![](../IMG/Result.png)  
The performance of these machine learning models is summarized using the confusion metrics, the litho-facies prediction plot in the blind well test to compare with the test data, and the plot of the density of real train/test value versus prediction.  
The key performance metrics used in this study are classification metrics such as precision, recall, and F1-Score were used to validate the model, these metrics come from the concepts of True Positive, True Negative, False Positive, and False Negative.  
Since Shale and Sand have different distributions, the F1 score is more helpful than accuracy (particularly if your class has an uneven distribution). 
  
![](../IMG/Untitled%20(5).png)  
![](../IMG/Untitled%20(6).png)   
**Here are the formulas for four measures that can be used to determine whether a model is appropriate or not:**   
Actual and predicted comparison chart  
![](../IMG/Untitled%20(7).png)  
## Conclusion
1. According to the blind test, with the well using the model compared with actual data in the test well, we can observe the precision is an excellent match with the real data. 
2. As a result, it will be a good strategy to apply for predicting facies in other wells with a lack of data and the unbalanced data, based on the ANN model.  
3. Good match based on train/test/predict values from the density visualization.  
4. We may focus on two crucial areas in the following phases to enhance the outcomes: integrate more samples of data into the models, fine-tune model parameters, and use more ML approaches to compare  
## Improvement  
In the phases that follow, we might concentrate on two critical areas to **improve the results**:  
Adding more samples of data to the models, fine-tuning model parameters, and using more ML algorithms for comparison.  
I'll give a quick summary of the attributes of our model here:  
- Include more data samples in the models.  
- Fine-tune model parameters  
- Use more ML approaches to compare  
## Acknowledgements
* For more information about comparison between Accuracy and F1_score, you can follow this link (https://medium.com/analytics-vidhya/accuracy-vs-f1-score-6258237beca2)
* A Neural Network Implementation in Sklearn (<https://scikit-learn.org/stable/modules/neural_networks_supervised.html#mlp-tips>)
* You can find more information about Robust Scaler in this link (<https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html>)

**Thank you for taking the time to read my article, I hope it does not waste your time.**
