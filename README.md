<h1> Sleep Hours Predictor</h1>
This project uses a dataset on sleep health and lifestyle factors to analyze the relationship between sleep duration and various independent variables such as stress level, physical activity level, and quality of sleep. It utilizes the scikit-learn library to perform linear regression and make predictions based on user input.

<h1> Getting Started </h1>

To run the project, follow the steps below:

Clone the repository to your local machine:

git clone https://github.com/danifeerrer/SleepHoursPredictor
        
Install the required dependencies. You can use the following command to install the necessary libraries:

pip install pandas matplotlib scikit-learn

Download and prepare the data:

Download the dataset file from the link provided or specify the path to your own dataset file.
Update the data_root variable in the code to point to the dataset file.

<h2> Visualize the data </h2>

The code generates scatter plots to visualize the relationship between sleep duration and the independent variables.
Run the code to see the scatter plots.

<h2> Train the model </h2>

The code uses the LinearRegression model from scikit-learn to train the model.
The independent variables (X) and dependent variable (Y) are selected from the dataset.
The model is trained using the fit() function.

<h2> Make predictions </h2>

The code prompts the user to input their perceived stress level, physical activity level, and quality of sleep.
Based on the user input, the model predicts the estimated sleep duration using the predict() function.
The predicted sleep duration is displayed as output.

<h2> Dependencies </h2>
        
pandas
matplotlib
scikit-learn

        
<h2> Dataset </h2>
        
The dataset used for this project is stored in the file Sleep_health_and_lifestyle_dataset.csv. It contains information on sleep duration and various lifestyle factors.
