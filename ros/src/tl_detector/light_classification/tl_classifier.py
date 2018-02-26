from styx_msgs.msg import TrafficLight
from ml_classifier import MLClassifier

class TLClassifier(object):
    def __init__(self, model_path=None, labels_path=None):
        #TODO load classifier
        self.classifier = MLClassifier(model_path, labels_path)
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        return self.classifier.get_classification(image)
