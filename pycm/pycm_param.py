# -*- coding: utf-8 -*-

VERSION = "1.7"


OVERVIEW = '''
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.
'''



MATRIX_CLASS_TYPE_ERROR = "Input Matrix Classes Must Be Same Type"
MATRIX_FORMAT_ERROR = "Input Confusion Matrix Format Error"
MAPPING_FORMAT_ERROR = "Mapping Format Error"
MAPPING_CLASS_NAME_ERROR = "Mapping Classnames Error"
VECTOR_TYPE_ERROR = "Input Vectors Must Be List"
VECTOR_SIZE_ERROR = "Input Vectors Must Be The Same Length"
VECTOR_EMPTY_ERROR = "Input Vectors Are Empty"
CLASS_NUMBER_ERROR = "Number Of Classes < 2"



DOCUMENT_ADR = "http://www.pycm.ir/doc/index.html#"

PARAMS_DESCRIPTION = {
    "TPR": "sensitivity, recall, hit rate, or true positive rate",
    "TNR": "specificity or true negative rate",
    "PPV": "precision or positive predictive value",
    "NPV": "negative predictive value",
    "FNR": "miss rate or false negative rate",
    "FPR": "fall-out or false positive rate",
    "FDR": "false discovery rate",
    "FOR": "false omission rate",
    "ACC": "accuracy",
    "F1": "F1 Score - harmonic mean of precision and sensitivity",
    "MCC": "Matthews correlation coefficient",
    "BM": "Informedness or Bookmaker Informedness",
    "MK": "Markedness",
    "PLR": "Positive likelihood ratio",
    "NLR": "Negative likelihood ratio",
    "DOR": "Diagnostic odds ratio",
    "TP": "true positive/hit",
    "TN": "true negative/correct rejection",
    "FP": "false positive/Type 1 error/false alarm",
    "FN": "false negative/miss/Type 2 error",
    "P": "Condition positive or Support",
    "N": "Condition negative",
    "TOP": "Test outcome positive",
    "TON": "Test outcome negative",
    "POP": "Population",
    "PRE": "Prevalence",
    "G": "G-measure geometric mean of precision and sensitivity",
    "RACC": "Random Accuracy",
    "F0.5": "F0.5 Score",
    "F2": "F2 Score",
    "ERR": "Error Rate",
    "RACCU": "Random Accuracy Unbiased",
    "J": "Jaccard index",
    "NIR": "No Information Rate",
    "IS": "Information Score",
    "CEN": "Confusion Entropy",
    "MCEN": "Modified Confusion Entropy",
    "AUC": "Area under the ROC curve",
    "dInd": "Distance index",
    "sInd": "Similarity index",
    "DP": "Discriminant power",
    "Y": "Youden index",
    "PLRI": "Positive likelihood ratio interpretation",
    "DPI": "Discriminant power interpretation",
    "AUCI": "AUC value interpretation",
    "GI": "Gini index",
    "LS": "Lift score"}

PARAMS_LINK = {
    "TPR": "TPR-(True-positive-rate)",
    "TNR": "TNR-(True-negative-rate)",
    "PPV": "PPV-(Positive-predictive-value)",
    "NPV": "NPV-(Negative-predictive-value)",
    "FNR": "FNR-(False-negative-rate)",
    "FPR": "FPR-(False-positive-rate)",
    "FDR": "FDR-(False-discovery-rate)",
    "FOR": "FOR-(False-omission-rate)",
    "ACC": "ACC-(Accuracy)",
    "F1": "FBeta-Score",
    "F0.5": "FBeta-Score",
    "F2": "FBeta-Score",
    "MCC": "MCC-(Matthews-correlation-coefficient)",
    "BM": "BM-(Bookmaker-informedness)",
    "MK": "MK-(Markedness)",
    "PLR": "PLR-(Positive-likelihood-ratio)",
    "NLR": "NLR-(Negative-likelihood-ratio)",
    "DOR": "DOR-(Diagnostic-odds-ratio)",
    "TP": "TP-(True-positive)",
    "TN": "TN-(True-negative)",
    "FP": "FP-(False-positive)",
    "FN": "FN-(False-negative)",
    "P": "P-(Condition-positive)",
    "N": "N-(Condition-negative)",
    "POP": "POP-(Population)",
    "TOP": "TOP-(Test-outcome-positive)",
    "TON": "TON-(Test-outcome-negative)",
    "G": "G-(G-measure)",
    "ERR": "ERR-(Error-rate)",
    "RACC": "RACC-(Random-accuracy)",
    "RACCU": "RACCU-(Random-accuracy-unbiased)",
    "PRE": "PRE-(Prevalence)",
    "Overall ACC": "Overall_ACC",
    "Kappa": "Kappa",
    "Overall RACC": "Overall_RACC",
    "SOA1(Landis & Koch)": "SOA1-(Landis-&-Koch’s-benchmark)",
    "SOA2(Fleiss)": "SOA2-(Fleiss’-benchmark)",
    "SOA3(Altman)": "SOA3-(Altman’s-benchmark)",
    "SOA4(Cicchetti)": "SOA4-(Cicchetti’s-benchmark)",
    "TPR Macro": "TPR_Macro",
    "PPV Macro": "PPV_Macro",
    "TPR Micro": "TPR_Micro",
    "PPV Micro": "PPV_Micro",
    "Scott PI": "Scott's-Pi",
    "Gwet AC1": "Gwet's-AC1",
    "Bennett S": "Bennett's-S",
    "Kappa 95% CI": "Kappa-95%-CI",
    "Kappa Standard Error": "Kappa-95%-CI",
    "Chi-Squared": "Chi-squared",
    "Phi-Squared": "Phi-squared",
    "Cramer V": "Cramer's-V",
    "Chi-Squared DF": "Chi-squared-DF",
    "95% CI": "95%-CI",
    "Standard Error": "95%-CI",
    "Response Entropy": "Response-entropy",
    "Reference Entropy": "Reference-entropy",
    "Cross Entropy": "Cross-entropy",
    "Joint Entropy": "Joint-entropy",
    "Conditional Entropy": "Conditional-entropy",
    "KL Divergence": "Kullback-Liebler-divergence",
    "Lambda B": "Goodman-&-Kruskal's-lambda-B",
    "Lambda A": "Goodman-&-Kruskal's-lambda-A",
    "Kappa Unbiased": "Kappa-unbiased",
    "Overall RACCU": "Overall_RACCU",
    "Kappa No Prevalence": "Kappa-no-prevalence",
    "Mutual Information": "Mutual-information",
    "J": "J-(Jaccard-index)",
    "Overall J": "Overall_J",
    "Hamming Loss": "Hamming-loss",
    "Zero-one Loss": "Zero-one-loss",
    "NIR": "NIR-(No-information-rate)",
    "P-Value": "P-Value",
    "IS": "IS-(Information-score)",
    "CEN": "CEN-(Confusion-entropy)",
    "Overall CEN": "Overall_CEN",
    "MCEN": "MCEN-(Modified-confusion-entropy)",
    "Overall MCEN": "Overall_MCEN",
    "Overall MCC": "Overall_MCC",
    "RR": "RR-(Global-performance-index)",
    "CBA": "CBA-(Class-balance-accuracy)",
    "AUC": "AUC-(Area-under-the-ROC-curve)",
    "AUNU": "AUNU",
    "AUNP": "AUNP",
    "sInd": "sInd-(Similarity-index)",
    "dInd": "dInd-(Distance-index)",
    "RCI": "RCI-(Relative-classifier-information)",
    "DP": "DP-(Discriminant-power)",
    "Y": "Y-(Youden-index)",
    "PLRI": "PLRI-(Positive-likelihood-ratio-interpretation)",
    "DPI": "DPI-(Discriminant-power-interpretation)",
    "AUCI": "AUCI-(AUC-value-interpretation)",
    "GI": "GI-(Gini-index)",
    "LS": "LS-(Lift-index)"}

BENCHMARK_COLOR = {
    "Negligible": "Red",
    "Poor": "Red",
    "Limited": "Red",
    "Fair": "Orange",
    "Good": "Green",
    "Excellent": "Green",
    "Intermediate to Good": "Green",
    "Substantial": "Green",
    "Almost Perfect": "Green",
    "Moderate": "Green",
    "Slight": "Orange",
    "None": "White",
    "Very Good": "Green"}
