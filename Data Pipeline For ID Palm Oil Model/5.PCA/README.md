
In this case, we use Principal Component Analysis (PCA) because we are working with weather data from multiple regions within a small country, 
which increases the likelihood of overlapping features and multicollinearity. 

PCA helps to address these issues by transforming the data into a set of orthogonal (uncorrelated) components, thereby reducing multicollinearity 
and capturing the most important variance in the data.

At the end of the PCA process, we use a scree plot to determine the number of principal components to retain. Including all PCA 
components in a model might not be beneficial, so the scree plot helps us decide how many components to keep for optimal performance.
