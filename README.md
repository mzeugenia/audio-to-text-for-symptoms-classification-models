![Alt text](https://github.com/mzeugenia/speech-recognition/blob/main/figures/intro_figure.png)

# SympToMatch
## Unleashing the power of AI to match patients with the right care

## Table of Contents
<!--ts-->
1. [Project Description](#project-description)
2. [Goal](#goal)
3. [Approach](#approach)
4. [Data Source](#data-source)
5. [Model Training](#model-training)
6. [Evaluation](#evaluation)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)
<!--te-->



## Project Description

SympToMatch is a project that utilizes the capabilities of artificial intelligence to match patients with the appropriate medical care based on their reported symptoms. The project aims to automate the initial query handling process in the telenursing service by accurately transcribing and understanding spoken queries from callers seeking medical advice or information.

## Goal

The goal of this project is to develop a robust system that can classify audio recordings containing ailment descriptions into severe and mild categories. Additionally, the system should be able to match each ailment with the corresponding medical specialization. By automating these processes, the project aims to enhance the efficiency and effectiveness of the telenursing service.

## Approach

The project follows the following approach:

1. Collecting audio files from Kaggle: The audio files used in this project are sourced from Kaggle's Medical Speech Transcription and Intent dataset (link).

2. Transcribing audio into text: The audio recordings are transcribed using automatic speech recognition (ASR) techniques to convert them into text format.

3. Labeling data into severe and mild: The transcribed text data is labeled into two classes: severe and mild, representing the severity level of the ailments described in the recordings.

4. Training Model_1: A supervised machine learning classification algorithm is trained using the labeled data to discriminate ailment descriptions by severity.

5. Labeling data assigning ailments to 12 different medical specializations: The transcribed text data is further labeled by assigning the ailments to 12 distinct medical specializations, including dermatology, gastroenterology, psychology, orthopedics, rheumatology, general, cardiology, ophthalmology, wound care, otorhinolaryngology, emergency (ER), and physiatry.

6. Training Model_2: Another supervised machine learning classification algorithm is trained using the labeled data to assign ailments into the 12 specified medical specialization classes.

7. Testing Model_1 and Model_2: The trained models are evaluated on unseen data to assess their performance in accurately classifying and matching ailment descriptions.

## Data Source

The audio data used in this project is obtained from Kaggle's Medical Speech Transcription and Intent dataset. The dataset provides audio recordings along with their corresponding transcriptions and labels.

## Model Training

Two models, Model_1 and Model_2, are trained as part of this project:

1. Model_1: This model is trained to classify ailment descriptions based on severity into two classes: severe and mild.
2. Model_2: This model is trained to assign ailments to one of the 12 different medical specializations.
Both models are trained using supervised machine learning algorithms, leveraging the labeled data.

## Evaluation

The performance of Model_1 and Model_2 is evaluated using unseen data. The evaluation metrics include accuracy, precision, recall, and F1-score to measure the models' classification and matching capabilities.

## Usage

To use the SympToMatch system, follow the steps below:

1. Obtain the necessary audio data containing ailment descriptions.
2. Preprocess the audio data by transcribing it into text format.
3. Apply Model_1 to classify the ailment descriptions into severe and mild.
4. Use Model_2 to assign the ailments to the appropriate medical specialization.
5. Analyze the results and make use of the matched medical specialization information for further processing.

## Contributing

Contributions to the SympToMatch project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Commit and push your changes to your fork.
5. Submit a pull request describing the changes you've made.

## License

This project is licensed under the MIT License.
