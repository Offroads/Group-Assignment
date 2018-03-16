import os
import fileHandler
import math

dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
os.chdir(dir_path)
posTrainPath = os.getcwd() + "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
negTrainPath = os.getcwd() + "\\Data\\train\\neg\\"
posTrainFiles = fileHandler.getfilelist(posTrainPath)  # list of files
negTrainFiles = fileHandler.getfilelist(negTrainPath)  # list of files
posWords = fileHandler.getwords(posTrainFiles)  # list of words
negWords = fileHandler.getwords(negTrainFiles)  # list of words
posFrequency = fileHandler.makeWordFrequencyDict(
	posWords)  # dictionary with frequency of words found in positive reviews
negFrequency = fileHandler.makeWordFrequencyDict(
	negWords)  # dictionary with frequency of words found in negative reviews
posProbability = posTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # baseline prob
negProbability = negTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # .50ish?
dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
os.chdir(dir_path)
posReviewPath = os.getcwd() + "\\Data\\test\\pos\\1_10.txt"  # positive review
negReviewPath = os.getcwd() + "\\Data\\test\\neg\\0_2.txt"  # negative review


def makeClassPrediction(path, wordCountDict, priorProb):
	"""
	This function will predict if the review is positive or negative, depending on what is given as arguments
	:param path: the path to the txt file
	:param wordCountDict: the positive or negative review wordcounts
	:param priorProb: the prior probability for positive or negative review, should be around 0.50
	:return: a float with 2 decimals
	"""
	countedText = fileHandler.getwords(path = path)  # get the words from the file
	countedText = fileHandler.makeWordFrequencyDict(countedText)  # make a dict with word frequency in given file
	prediction = 0  # declare prediction
	for word in countedText:  # go through every word
		if word in wordCountDict:  # skip those words we don't have seen before
			prediction += (wordCountDict[word]*(countedText[word] + 1))  # multiply word frequency
	prediction = priorProb*prediction  # multiply prior probability
	return round(math.log10(prediction), 2)  # return float with 2 decimals


def finalPrediction(posPrediction, negPrediction):
	"""
	Function decides if the prediction is positive or negative
	:param posPrediction: float number
	:param negPrediction:  float number
	:return: string
	"""
	if posPrediction > negPrediction:
		return "positive"
	else:
		return "negative"


def testingPredictions():
	"""
	This function allow us to test quickly what the predictions are
	"""
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	posPrediction = makeClassPrediction(posReviewPath, posFrequency, posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = makeClassPrediction(posReviewPath, negFrequency, negProbability)
	print(negPrediction)
	prediction = finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	posPrediction = makeClassPrediction(negReviewPath, posFrequency, posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = makeClassPrediction(negReviewPath, negFrequency, negProbability)
	print(negPrediction)
	prediction = finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")


testingPredictions()  # running the test
# def finalPrediction(text):
#
# 	posPrediction = makeClassPrediction(text, posFrequency, posProbability, testDictionary)
#
# 	negPrediction = makeClassPrediction(text, negFrequency, negProbability, testDictionary)
#
# 	if negPrediction > posPrediction:
# 		return -1
# 	return 1
#
# print("For this review: {0}".format(reviews[0][0]))
# print("")
# print("The predicted label is ", make_decision(reviews[0][0]))
# print("The actual label is ", reviews[0][1])
#
#
#
