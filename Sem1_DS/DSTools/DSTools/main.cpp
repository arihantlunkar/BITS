//
//  main.cpp
//  DSTools
//
//  Created by Arihant Lunkar on 06/03/23.
//

#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <bitset>
using namespace std;

void calculateChiSquareTestForIndependence()
{
    int r = 2;  // number of distinct values in an attribute/feature
    int c = 2; // number of classes (distinct values) in Y
    double arr[2][2] = {{209,280}, {225,248}};
    double newArr[2][2];
    //int degreeOfFreedom = (r-1)*(c-1); // look at chart
    //double significanceLevelAlpha = 0.05;
    
    double totalSum=0;
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            totalSum+=arr[i][j];
        }
    }
    double chiSquare = 0.0;
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            double sumRow=0, sumCol=0;
            for(int k=0;k<c;++k)
                sumCol+=arr[i][k];
            for(int k=0;k<r;++k)
                sumRow+=arr[k][j];
            newArr[i][j] = (sumCol*sumRow)/totalSum;
            printf("%f(%f)\t", arr[i][j], newArr[i][j]);
            chiSquare+= (((arr[i][j]-newArr[i][j])*(arr[i][j]-newArr[i][j]))/newArr[i][j]);
        }
        printf("\n");
    }
    printf("%f", chiSquare);
    
    // if chiSquare > tabularChiSquare, or
    // pvalue < significanceLevelAlpha, then
    
    // we reject null hypothesis (i.e, 2 variables are independent) and accept alternate hyphothiss (i.e, 2 variabless are dependent and are related);
}

void informationGainCalulator()
{
    int r = 2; // number of distinct values in an attribute/feature
    int c = 2; // number of classes (distinct values) in Y
    double arr[2][2] = {{2, 0}, {0, 1}};
    double totalSum=0;
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            totalSum+=arr[i][j];
        }
    }
    printf("TOTAL SUM: %f ", totalSum);
    double infoD = 0.0;
    for(int i=0;i<c;++i)
    {
        double iColSum = 0.0;
        for(int j=0;j<r;++j)
        {
            iColSum += arr[j][i];
        }
        printf("iColSum %f, totalSum %f => -%f/%f*log2(%f/%f)\n",iColSum, totalSum, iColSum, totalSum, iColSum, totalSum);
        infoD += ((-iColSum/totalSum)*log2(iColSum/totalSum));
    }
    printf("infoD %f\n", infoD);
    
    double infoDCurr = 0.0;
    double splitInfo = 0.0;
    for(int j=0;j<r;++j)
    {
        double sumCol=0, infoCurr = 0.0, temp1 = 0.0;
        for(int k=0;k<c;++k)
            sumCol+=arr[j][k];
        for(int k=0;k<c;++k)
        {
            double temp = arr[j][k] != 0 ? ((-arr[j][k]/sumCol)*log2(arr[j][k]/sumCol)) : 0.0;
            infoCurr += temp;
            printf("I(%d,%d) => -%f/%f*log2(%f/%f) = %f\n", j, k, arr[j][k], sumCol, arr[j][k], sumCol, temp);
        }
        printf("I(%d) = %f*(%f/%f)\n", j, infoCurr, sumCol, totalSum);
        infoDCurr += (infoCurr * (sumCol/totalSum));
        temp1 = ((-sumCol/totalSum)*log2(sumCol/totalSum));
        printf("SplitInfo(%d) = -%f/%f*log2(%f/%f) = %f\n", j, sumCol, totalSum, sumCol, totalSum, temp1);
        splitInfo += temp1;
    }
    printf("infoDCurr %f\n", infoDCurr); // minimum
    printf("Gain => %f - %f = %f\n", infoD, infoDCurr, (infoD-infoDCurr)); // should be maximum
    printf("SplitInfo => %f\n", splitInfo); // should be minimum
    printf("GainRatio => %f/%f = %f\n", (infoD-infoDCurr), splitInfo, (infoD-infoDCurr)/splitInfo); // should be maximum
}

void giniIndexCalulator()
{
    int r = 2; // number of distinct values in an attribute/feature {high}, {low,medium}
    int c = 2; // number of classes (distinct values) in Y
    double arr[2][2] = {{3,0}, {4,3}};
    
    double gini = 0.0, temp = 0.0;
    
    double totalSum=0;
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            totalSum+=arr[i][j];
        }
    }
    for(int i=0;i<c;++i)
    {
        double sumRow=0;
        for(int k=0;k<r;++k)
            sumRow+=arr[k][i];
        printf("(%f/%f)^2\n", sumRow, totalSum);
        temp += ((sumRow/totalSum)*(sumRow/totalSum));
    }
    gini = 1 - temp;
    printf("Gini = 1 - %f = %f\n", temp, gini);
    double giniAsked = 0.0;
    for(int i=0;i<r;++i)
    {
        double sumCol=0, temp1=0, giniCurr = 0;
        for(int k=0;k<c;++k)
            sumCol+=arr[i][k];
        for(int k=0;k<c;++k)
        {
            printf("(%f/%f)^2\n", arr[i][k], sumCol);
            temp1 +=((arr[i][k]/sumCol)*(arr[i][k]/sumCol));
        }
        giniCurr = 1 - temp1;
        printf("GiniTemp = 1 - %f = %f\n", temp1, giniCurr);
        printf("GiniCurr = (%f/%f)*%f\n", sumCol, totalSum, giniCurr);
        giniAsked += ((sumCol/totalSum)*giniCurr);
    }
    printf("GiniAsked = %f\n", giniAsked); // should be minimum
    printf("DeltaGini(Gain) = %f\n", gini - giniAsked); // should be maximum
}

void confusionMatrixCalculator()
{
    // ACTUAL/PREDICTION
    // TRUE+ (diabetes and test data also has diabetes)    FALSE- (diabetes but test data say no diabetes)
    // FALSE+ (no diabetes but test data say diabetes)    TRUE- (no diabetes and test data also say no diabetes)
    
    // 7 1 3
    // 8 2 2
    // 9 3 1
    double TP = 18;
    double FN = 0;
    double FP = 1;
    double TN = 10;
    double precision = TP/(TP + FP);
    double recall = TP/(TP + FN);
    double beta = 0.5;
    printf("Classifier Accuracy = %f\n" , ((TP+TN)/(TP+TN+FN+FP)) * 100 );
    printf("Classification Error/ Misclassification rate = %f\n" , 1 - ((TP+TN)/(TP+TN+FN+FP)) );
    printf("True positive rate (TPR) or Recall/sensitivity = %f,%f percent\n" , TP/(TP + FN), 100*(TP/(TP + FN)) );  // does not tell anything abt FP -> limitation
    printf("True negative rate (TNR) or specificity = %f,%f percent\n" , TN/(TN + FP), 100*(TN/(TN + FP)) );
    printf("False positive rate (FPR) = %f,%f percent\n" , FP/(TN + FP), 100*(FP/(TN + FP)) );
    printf("False negative rate (FNR) = %f,%f percent\n" , FN/(TP + FN), 100*(FN/(TP + FN)) );
    printf("Precision = %f\n" , TP/(TP + FP) ); // does not tell anything abt FN -> limitation (use F1 score)
    printf("F measure (F1 or F-score) = %f\n" , (2*precision*recall)/(precision+recall)); // harmonic mean of precision and recall
    printf("F beta measure = %f,%f percent with beta = %f\n" , ((1+(beta*beta))*precision*recall)/((precision*beta*beta)+recall), 100*((1+(beta*beta))*precision*recall)/((precision*beta*beta)+recall), beta);
    // Eg: precision is more imp than recall -> spam filter why? because FP is more imp than FN
    // Eg: recall is more imp than precision -> cancer detection why? because FN is more imp than FP
}


void associationRulesCalulator()
{
    vector<vector<string>> transactions =
    {
        {"C", "M", "B", "Ch", "T"},
        {"M", "Ch", "S"},
        {"M", "C", "B"},
        {"M", "S", "Ch", "T"},
        {"C", "M", "B", "T"},
        
        {"S", "Ch", "M", "C"},
        {"C", "T", "B", "Ch"},
        {"C", "M", "Ch"},
        {"C", "B", "Ch"},
        {"M", "C", "Ch", "T"}
    };
    
    vector<string> itemset = {"S", "Ch"};
    
    size_t n = itemset.size();
    int num_masks = (1 << n);

    // Brute force
    // total rules  = 3^d - 2^(d+1) + 1 where d is number of items in supermarket => computantionally expensive
    
    // Better approach
    // Step1:
    // frequent itemset generation; say items are A, B, C
    // then 000, 001, 010, 011, 100, 101, 110, 111 => C, B, BC, A, AC, AB, ABC are frequent itemset => total possible combinations are 2^d - 1; removing null;  why 2 = > bipartioning
    // calculate support count for each frequent itemset  .. i.e, count number of times frequent item set occured in transacations .. if support count >= min support count then use it .. Note:= support count != support ()
    
    // Alternatively we can use apriori principle to find frequent item set:
    // if an item set is not frequent (ie., support count < min support count) then all its superset would be not frequent... so we can exclude then process is called pruning ..
    // eg say AB is not frequent then ABC would also be not frequent
    // eg say B is not frequent then B, BC, AB, ABC would not be frequent
    // Similarly the confidence of {ABC->A} >= {BC->A} >= {C->A} >= {AC->A} .. so we can exclude then process is called pruning
    
    // Maximal frequent itemset:  An itemset is maximal frequent if none of its supersets (all) are frequent.
    // Closed Itemset: An itemset is closed if none of its immediate supersets have same support count same as Itemset.
    
    // # Step2
    // Create assoication rules for individual frequent itemset. {A} -> {B}
    // And the rule which has high confidence i.e, C>=min threshold C should be used for telling useful information
    
    // Time Complexity = O(#n * 2^d * width) => #n is number of transactions, and width is max size of a particular transaction
    
    
    
    
    for (int i = 1; i < num_masks - 1; i++) {
        for (int j = 1; j < num_masks - 1; j++) {
            if (i & j) {
                continue;
            }

            bitset<3> left(i);
            bitset<3> right(j);

            vector<string> left_items;
            vector<string> right_items;

            for (int k = 0; k < n; k++) {
                if (left[k]) {
                    left_items.push_back(itemset[k]);
                }
                if (right[k]) {
                    right_items.push_back(itemset[k]);
                }
            }
            
            if(left_items.size() != 0 && right_items.size() != 0)
            {
                int transactionsContainingBothXandY = 0;
                int transactionsContainingOnlyX = 0;
                int transactionsContainingOnlyY = 0;
                for(auto products : transactions)
                {
                    bool allLeftFound = true, allRightFound = true;
                    for(auto left_item : left_items)
                    {
                        if (find(products.begin(), products.end(), left_item) == products.end())
                        {
                            allLeftFound = false;
                        }
                    }
                    for(auto right_item : right_items)
                    {
                        if (find(products.begin(), products.end(), right_item) == products.end())
                        {
                            allRightFound = false;
                        }
                    }
                    if(allRightFound && allLeftFound)
                    {
                        ++transactionsContainingBothXandY;
                    }
                    if(allLeftFound)
                    {
                        ++transactionsContainingOnlyX;
                    }
                    if(allRightFound)
                    {
                        ++transactionsContainingOnlyY;
                    }
                }
                cout << "{";
                for (int k = 0; k < left_items.size(); k++) {
                    cout << left_items[k];
                    if (k < left_items.size() - 1) {
                        cout << ", ";
                    }
                }
                cout << "} -> {";
                for (int k = 0; k < right_items.size(); k++) {
                    cout << right_items[k];
                    if (k < right_items.size() - 1) {
                        cout << ", ";
                    }
                }
                // ", S => #(X U Y)/#TotalTransactions = "
                // ", C => #(X U Y)/#TransactionsContainingOnlyX = "
                // ", L => #(X U Y)/#TransactionsContainingOnlyX*#TransactionsContainingOnlyY = "
                // Lift 1 then X and Y are independent then S high and C high mean rule is not interesting
                // Lift > 1 positively related
                // Lift < 1 negitavely related
                cout << "} #(X U Y) = " << transactionsContainingBothXandY << ", #N = " << transactions.size() << ", S = " << double(transactionsContainingBothXandY)/double(transactions.size()) << ", C = " << double(transactionsContainingBothXandY)/double(transactionsContainingOnlyX) << ", L = " << double(transactionsContainingBothXandY)/(double(transactionsContainingOnlyX)*double(transactionsContainingOnlyY)) << endl;
                
                // Rule is interesting if S >= min support threshold and C >= min confidence threshold
            }
        }
    }
}

#include <float.h>
#include <map>

void calculateMean(const vector<vector<double>>& points, vector<double>& rpoint, int cluster)
{
    for(int j = 0; j < points[0].size(); ++j)
    {
        rpoint.push_back(0);
    }
    printf("New Mean of cluster %d : ", cluster);
    for(int i = 0; i < points.size(); ++i)
    {
        for(int j = 0; j < points[i].size(); ++j)
        {
            rpoint[j] += points[i][j];
        }
    }
    printf(" = ");
    for(int j = 0; j < points[0].size(); ++j)
    {
        rpoint[j] = rpoint[j]/points.size();
        printf("%f,", rpoint[j]);
    }
    printf("\n");
}

void kMeansCalculator()
{
    // all attributes numeric -> kMeans
    // all categorical + numeric -> k-medoids
    // all categorical -> kMode
    // if outliers in numeric -> kMedian (Mean sensitive to outliers)
    
    // limitations
    // does not work with non-spherical data
    // k is required
    
//    vector<vector<double>> arr = {{25,26,27,28}, {29,30,31,32},{33,34,35,36}, {1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20},{21,22,23,24}}; // records vs features
//    vector<vector<double>> centroids = {{25,26,27,28}, {29,30,31,32},{33,34,35,36}}; // clusters vs features
//
    vector<vector<double>> arr = {{72,185}, {56,170}, {60,168}, {68,179}, {72,182}, {77,188}, {70,180}, {84,183}}; // records vs features
    vector<vector<double>> centroids = {{72,185}, {56,170}}; // clusters vs features
    
    int numberOfIteration = 3;
    while(numberOfIteration > 0)
    {
        map<int, vector<vector<double>>> pointsInCluster;
        for(int i=0;i<arr.size();++i)
        {
            double euclideanDistance = DBL_MAX;
            int index = 0;
            for(int j=0;j<centroids.size();j++)
            {
                double dist = 0.0;
                printf("Cluster(%d) =>", j);
                for(int m=0;m<arr[0].size();++m)
                {
                    double temp = (arr[i][m] - centroids[j][m])*(arr[i][m] - centroids[j][m]);
                    printf("(%f - %f)^2 + ", arr[i][m], centroids[j][m]);
                    dist += temp;
                }
                printf(" = %f\n" , dist);
                if(dist < euclideanDistance)
                {
                    index = j;
                    euclideanDistance = dist;
                }
            }
            pointsInCluster[index].push_back(arr[i]);
            printf("Record %d belongs to cluster %d (total = %lu) with eucliedan distance = %f\n\n", i, index, pointsInCluster[index].size(), euclideanDistance);
        }
        
        vector<vector<double>> newCentroids;
        for(auto itr = pointsInCluster.begin(); itr != pointsInCluster.end(); ++itr)
        {
            vector<double> point;
            calculateMean(itr->second, point, itr->first);
            newCentroids.push_back(point);
        }
        --numberOfIteration;
        centroids.assign(newCentroids.begin(), newCentroids.end());
        printf("\n");
    }
}

void calculateBinning()
{
    int arr[] = {5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215}; // | 4, 8, 15, 21, 21, 24, 25, 28, 34 | 5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215
    const int n = sizeof(arr)/sizeof(int);
    const int noOfBins = 3;
    
    printf("Partition into equal frequency bins\n");
    for(int i = 0; i < n; ++i)
    {
        if(i != 0 && (i%(n/noOfBins)) == 0)
        {
            printf("\n");
        }
        printf("%d,", arr[i]);
    }
    printf("\nSmoothing by bin means\n");
    double sum = 0;
    int ctr = 0;
    for(int i = 0; i < n; ++i)
    {
        if(i != 0 && (i%(n/noOfBins)) == 0)
        {
            const double mean = sum /ctr;
            for(int j = 0; j < ctr; ++j)
            {
                printf("%f,", mean);
            }
            sum = 0;
            ctr = 0;
            printf("\n");
        }
        sum += arr[i];
        ++ctr;
    }
    for(int j = 0; j < ctr; ++j)
    {
        printf("%f,", sum /ctr);
    }
    
    printf("\n\n");
    printf("\nPartition into equal depth bins\n");
    const int max = arr[n-1];
    const int min = arr[0];
    const int w = (max - min) / noOfBins;
    printf("Max : %d, Min: %d, W = %d\n", max, min ,w);
    int k = 0;
    for(int i = 0; i < n; ++i)
    {
        if(arr[i] > arr[k] + w)
        {
            k = i;
            printf("\n");
        }
        printf("%d,", arr[i]);
    }
    printf("\nSmoothing by bin means\n");
    sum = 0;
    k = 0;
    ctr = 0;
    for(int i = 0; i < n; ++i)
    {
        if(arr[i] > arr[k] + w)
        {
            k = i;
            double mean = sum / ctr;
            for(int j = 0; j < ctr; ++j)
            {
                printf("%f,", mean);
            }
            sum = 0;
            ctr = 0;
            printf("\n");
        }
        sum += arr[i];
        ++ctr;
    }
    for(int j = 0; j < ctr; ++j)
    {
        printf("%f,", sum/ctr);
    }
    printf("\nSmoothing by bin boundary - replace each element by boundary element (either min/max)\n");
}

int myMatch(const vector<string>& left, const vector<string>& right)
{
    if(left.size()!=right.size()) return 0;
    
    int match = 0;
    for(int i=0;i<left.size();++i)
        if(left[i] == right[i])
            ++match;
    
    return match;
}

void proximityMatrixCalculator()
{
    //vector<vector<string>> data = {{"96", "A"},{"87", "B"},{"83", "B"},{"96", "A"}};
    
    vector<vector<string>> data = {{"Doctor"}, {"Data Scientist"}};
    
    double matrix[data.size()][data.size()];
    for(int i=0;i<data.size();++i)
    {
        for(int j=0;j<data.size();++j)
        {
            matrix[i][j] = 0.0;
            if(i>j)
            {
                double match = myMatch(data[i], data[j]);
                matrix[i][j] = ((data[0].size() - match)/data[0].size());
                printf("(%d,%d) TotalAttr %lu, Match %f, (%lu-%f)/%lu = %f\t\n", i, j, data[0].size(), match, data[0].size(), match, data[0].size(), matrix[i][j]);
            }
        }
        printf("\n");
    }
    printf("Dissimilarity Matrix\n");
    for(int i=0;i<data.size();++i)
    {
        for(int j=0;j<data.size();++j)
        {
            printf("%f\t",matrix[i][j]);
        }
        printf("\n");
    }
}

#include <cmath>

void calculateLinearLogisticRegression()
{
    vector<vector<double>> input = {{5.5, 6.7}, {5, 7}, {8, 6}, {9, 7}, {6, 8}, {7.5, 7.3}};
    vector<double> output = {1, 0, 1, 1, 0, 0};
    double alpha = 0.3;
    vector<double> parameters = {0.5, 0.5, 0.5};
    int counter = 1;
    while(counter < 11)
    {
        printf("Iteration %d\n", counter);
        vector<double> tmpParameters(parameters);
        for(int i = 0; i < tmpParameters.size(); ++i)
        {
            double totalCost = 0.0;
            for(int j = 0; j < input.size(); ++j)
            {
                double cost = 0.0;
                double predictedOutput = 0.0;
                double linearCombinarionValue = 0.0;
                printf("ThetaT*X(%d) = z =", j);
                for(int k = 0; k < tmpParameters.size(); ++k)
                {
                    linearCombinarionValue += (k == 0 ? parameters[k] : (parameters[k]*input[j][k-1]));
                    if(k==0)
                    {
                        printf(" Theta%d * x%d [%f*1]", k, k, parameters[k]);
                    }
                    else
                    {
                        printf(" + Theta%d * x%d [%f*%f]", k, k, parameters[k], input[j][k-1]);
                    }
                }
                printf(" = %f \n", linearCombinarionValue);
                //predictedOutput = linearCombinarionValue; // linear regression
                predictedOutput = 1/(1+exp(-linearCombinarionValue));
                printf("H(x(%d)) = 1/1+e^-ThetaT*X(%d) = %f\n", j, j, predictedOutput);
                cost = ((i==0 ? 1 : input[j][i-1])*(predictedOutput - output[j]));
                totalCost += cost;
                printf("(H(x(%d)) [%f] - y(%d) [%f])* [%f] = %f\n", j, predictedOutput, j, output[j], (i==0 ? 1 : input[j][i-1]), (predictedOutput - output[j]));
            }
            printf("TotalCost = %f\n", totalCost);
            tmpParameters[i] = tmpParameters[i] - ((alpha/output.size())*totalCost);
            printf("NewTheta[%d] = (%f - (%f/%d)*%f)  = %f\n\n", i, parameters[i], alpha, output.size(), totalCost, tmpParameters[i]);
        }
        printf("\n\n\n\n");
        ++counter;
        parameters = tmpParameters;
    }
}


int main(int argc, const char * argv[]) {
    //calculateLinearLogisticRegression();
    // insert code here...
    //calculateChiSquareTestForIndependence();
    informationGainCalulator();
    //giniIndexCalulator();
    //confusionMatrixCalculator();
    //associationRulesCalulator();
    //kMeansCalculator();
    //calculateBinning();
    //proximityMatrixCalculator();
    
    // story telling =
    // 1. visualization -> visual plots like bar chart, dashboard
    // 2. narrative -> arrange visualization in a story (structure your story : begin with explaning problem, objective and goal ... middle should be descrive approach and findings ... end should be open ended and give recommendation)
    // 3. context ->
    // who - target audienece
    // what - focus on imp aspect, which data elements to consider, ignore irrelavant aspect
    // how - how will u communicate (email, ppt, doc)
    
    
    
    return 0;
}
