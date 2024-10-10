import os
import time
import uuid

from azure.cognitiveservices.vision.customvision.prediction import \
    CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import \
    CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import (
    ImageFileCreateBatch, ImageFileCreateEntry, Region)
from msrest.authentication import ApiKeyCredentials

# Replace with your Custom Vision details
PREDICTION_KEY = "edac2b4b742942c3aa3f436178fa9655"
ENDPOINT = "https://southeastasia.api.cognitive.microsoft.com/"
PROJECT_ID = "af94bb94-91da-45fd-b114-040b2cac9c88"
PUBLISHED_NAME = "melanomaDetection"


