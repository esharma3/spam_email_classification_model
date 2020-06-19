from joblib import load
from preprocess import prep_data
import time
import os


###############################################################################
#                           MODEL PREDICTIONS                                 #
###############################################################################

def predict(s):

    X_string = prep_data(s)

    # loading the model
    spam_classifier = load(os.path.join("model", "svm_spam_classifier.joblib"))

    # predicting
    spam_classifier_pred = spam_classifier.predict(X_string["clean_text"])

    if spam_classifier_pred == 1:
        result = "Spam"
    else:
        result = "Not Spam"

    return result


###############################################################################
#                                   MAIN                                      #
###############################################################################

if __name__ == "__main__":

    t = time.time()
    string = """We have filled the role and unfortunately, we will not be moving forward with your candidacy. Thank you again for your application, and time. We are a fast growing company, and our roles are constantly changing. Watch our job openings at Careers for future opportunities.
                We wish you the best in your endeavors. """
    print(string)
    print(predict(string))
    print(f"Preprocessing Time: {time.time() - t} seconds")
