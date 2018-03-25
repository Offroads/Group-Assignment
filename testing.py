import os
import time

import predictor as predict


def testingPredictions():
	"""
	This test tests what the predictions are for a positive and negative test review
	"""
	startTime = time.time()
	print("Running testingPredictions...")
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	posReviewPath = os.getcwd() + "\\Data\\test\\pos\\1_10.txt"  # positive review
	negReviewPath = os.getcwd() + "\\Data\\test\\neg\\0_2.txt"  # negative review
	trainingData = predict.getInitializedTrainData()
	posFrequency = trainingData["posFreq"]
	negFrequency = trainingData["negFreq"]
	posProbability = trainingData["posProb"]
	negProbability = trainingData["negProb"]
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path = posReviewPath, wordCountDict = posFrequency,
												priorProb = posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path = posReviewPath, wordCountDict = negFrequency,
												priorProb = negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path = negReviewPath, wordCountDict = posFrequency,
												priorProb = posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path = negReviewPath, wordCountDict = negFrequency,
												priorProb = negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def testingTestDataProcessing():
	"""
	This test checks that getIntitializedTestData() returns something
	"""
	startTime = time.time()
	print("Running testingTestDataProcessing...")  # running the test
	if predict.getIntitializedTestData() is not None:
		print("Data was processed")
	else:
		print("Something went wrong")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def testPredicTestReviews():
	"""
	This test will try to predict all the test reviews.
	Accuracy of the test and duration of test is printed.
	"""
	startTime = time.time()
	print("Running testPredicTestReviews...")
	results = predict.predictTestReviews()
	print(results)
	numberOfReviews = 25000
	print(str((results["correctPredictions"] - numberOfReviews)/numberOfReviews*(100)*-1) + "% is the error rate ")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def main():
	"""
	The main method for testing, it executes the following tests.
	"""
	testPredicTestReviews()  # running test
	print()
	testingTestDataProcessing()  # running test
	print()
	testingPredictions()  # running test


main()
