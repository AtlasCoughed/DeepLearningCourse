import math


def batches(batch_size, features, labels):
    """
    Create batches of features and labels
    :param batch_size: The batch size
    :param features: List of features
    :param labels: List of labels
    :return: Batches of (Features, Labels)
    """
    output_files = []

    # Variable here (batch_size, features, labels)
    batchesLength = len(features)
    sample_size = len(features)
    for start_i in range(0, sample_size, batch_size):
        endLength = start_i + batch_size
        output_files.append([features[start_i: endLength], labels[start_i: endLength]])

    return output_files

