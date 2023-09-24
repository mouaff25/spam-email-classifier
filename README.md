# Spam Email Classifier

This repository contains a Spam Email Classifier, which is a machine learning model trained to classify emails as either spam or legitimate (ham). The model has been optimized for the F-beta score with a beta value of 0.5, slightly prioritizing precision over recall.

## Dataset
The model was trained on the [Spam Email Dataset](https://www.kaggle.com/datasets/mfaisalqureshi/spam-email) from Kaggle. This dataset contains a collection of labeled email samples, making it suitable for training a classification model.

## Model
The classifier is based on logistic regression, a widely used algorithm for binary classification tasks. It has been fine-tuned to achieve high accuracy in distinguishing between spam and ham emails, with a focus on minimizing false positives while maintaining good overall performance.

## Usage

To use this Spam Email Classifier, follow these steps:

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/mouaff25/spam-email-classifier.git
   cd spam-email-classifier
    ```

2. **Install Dependencies:**
    Ensure that you have Python 3.10 installed on your system. Then, install the required dependencies using pip:
    ```shell
    pip install -r requirements.txt
    ```

3. **Run the Gradio App:**
    Run the Gradio app using the following command:
    ```shell
    python app.py
    ```
    This will start a local server, and you can access the app by opening a web browser and navigating to `http://localhost:7860`.

4. **Classify Emails:**
    You can now classify emails as either spam or ham by entering the email text into the text box and clicking the "Submit" button. The model will then classify the email and display the result as a probability value between 0 and 1.

5. **Enjoy!**
    Use the Spam Email Classifier to quickly identify and categorize emails in your dataset or for individual emails.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/mouaff25/spam-email-classifier/blob/main/LICENSE) file for details.
