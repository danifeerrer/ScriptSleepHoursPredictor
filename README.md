<h1> Sleep </h1>
This project uses a dataset on sleep health and lifestyle factors to analyze the relationship between sleep duration and various independent variables such as stress level, physical activity level, and quality of sleep. It utilizes the scikit-learn library to perform linear regression and make predictions based on user input.

Getting Started

To run the project, follow the steps below:

Clone the repository to your local machine:

git clone https://github.com/danifeerrer/SleepHoursPredictor
        
Install the required dependencies. You can use the following command to install the necessary libraries:

pip install pandas matplotlib scikit-learn

Download and prepare the data:

Download the dataset file from the link provided or specify the path to your own dataset file.
Update the data_root variable in the code to point to the dataset file.

Visualize the data:

The code generates scatter plots to visualize the relationship between sleep duration and the independent variables.
Run the code to see the scatter plots.

Train the model:

The code uses the LinearRegression model from scikit-learn to train the model.
The independent variables (X) and dependent variable (Y) are selected from the dataset.
The model is trained using the fit() function.

Make predictions:

The code prompts the user to input their perceived stress level, physical activity level, and quality of sleep.
Based on the user input, the model predicts the estimated sleep duration using the predict() function.
The predicted sleep duration is displayed as output.

Dependencies
        
pandas
matplotlib
scikit-learn

        
Dataset
        
The dataset used for this project is stored in the file Sleep_health_and_lifestyle_dataset.csv. It contains information on sleep duration and various lifestyle factors.
