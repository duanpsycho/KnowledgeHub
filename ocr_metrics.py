def ocr_metrics(reference, result):
    """
    Function for return metrics about OCR tests, for validate our OCR service

    :param reference: Raw text, which is the text that we are testing
    :param result: Text after OCR
    :return: Accuracy and Precision metrics

    NLTK lib need SET object type to calculate Precision.
    For Accuracy, might be SET, but a List is better, because needs to be 2 lists with same length
    """

    # Import NLTK metric class
    from nltk.metrics import accuracy, precision

    # Return results after comparison
    if len(reference) == len(result):
        print("Accuracy: {0:.2f}%".format(accuracy(reference, result)*100))
        print("Precision: {0:.2f}%".format(precision(set(reference), set(result))*100))
    else:
        print("Is not possible to calculate accuracy, texts doesn't have the same length. "
              "\nExpected: {0} \nResult: {1}".format(len(reference), len(result)))
        print("Precision: {0:.2f}%".format(precision(set(reference), set(result)) * 100))


original = "Oi, eu sou o Goku!"
ocr_result = "Oi, eu sou 0 Goku!!"

ocr_metrics(original, ocr_result)
