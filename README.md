# NeuroDetect: Brain Tumor Detection Desktop App

NeuroDetect is an innovative desktop application designed to aid in the early detection of brain tumors through the analysis of CT Scan or MRI images.

**Note:** NeuroDetect is designed to assist medical professionals and individuals in the initial assessment of brain tumor presence based on imaging data. It is not intended to replace a comprehensive medical evaluation by qualified healthcare professionals. Always consult a medical expert for accurate diagnosis and treatment recommendations.

## Overview

NeuroDetect provides a user-friendly interface for the following key features:

- Import patient scan images.
- Analyze and predict brain tumor presence.
- Display the prediction results.

## Getting Started

These instructions will help you set up and run the NeuroDetect application on your local machine.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python
- OpenCV
- Numpy
- Pillow
- Tkinter
- Tensorflow

You can install these dependencies using the following command:

```bash
pip install opencv-python numpy pillow tk tensorflow
```

## Installation
1. Clone the repository to your local machine:

```
git clone https://github.com/AshkanYaghubi/NeuroDetect
```

2. Navigate to the project directory:

```
cd NeuroDetect
```

## Usage
1. Run the NeuroDetect application:

```
python main.py
```

2. The application will open with the following features:
- Import Patient Scan: Click the button to select a CT Scan or MRI image for analysis.
- Predict: Click the Predict button to analyze the selected image and predict the presence of a brain tumor.

3. View the prediction result displayed in the application.

## Built With

- Python
- OpenCV - Computer Vision Library
- Numpy - Numerical Computing Library
- Pillow - Python Imaging Library
- Tkinter - GUI Library
- Tensorflow - Deep Learning and Machine Learning Framework

## Future Work

As part of ongoing development, the NeuroDetect project aims to enhance its capabilities and reliability. The following are planned future works:

### 1. Addressing False Negatives

In future iterations, we will focus on minimizing false negatives in the brain tumor classification process. Specifically, we aim to ensure that the additional binary classification model, designed to reduce false negatives, produces results that are statistically incoherent with those of the base model. By running rigorous statistical tests, we intend to validate that false negatives from both models have no common patterns, reinforcing the effectiveness of their combined application in preventing occurrences of false negatives.

### 2. Continuous Improvement

We are committed to ongoing research and development to incorporate the latest advancements in machine learning and medical imaging. Continuous refinement of the models, exploration of new techniques, and adaptation to emerging technologies will be integral to the NeuroDetect project's mission of providing accurate and reliable brain tumor detection.

### 3. Community Engagement

We welcome contributions from the open-source community to collaboratively improve and expand NeuroDetect's capabilities. Feel free to contribute through bug fixes, feature enhancements, or by sharing insights and feedback.


## License
 This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
