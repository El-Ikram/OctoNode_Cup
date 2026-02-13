# GNNs Mini Competition: GitHub Social Network Classification
<p align="center">What if we could predict user characteristics just by looking at how they connect with others?</p>

## 💢Problem Description
The goal of this challenge is to perform binary node classification on a real-world GitHub social network graph. In this graph, each node represents a GitHub user, and edges represent social connections between users.

Your task is to build a model that leverages both node features and graph structure to predict whether a given GitHub user is primarily a Web Developer or a Machine Learning Developer.

Task Type:
* Node Classification
* Binary Classification
* Graph-Based Learning with GNNs
* Each node = one label:\
 1 → Web Developer.\
 0 → Machine Learning Developer.

## 🛢️Dataset
The GitHub Social Network dataset represents a real-world developer network where nodes correspond to GitHub users and edges represent social connections between them (such as following relationships). Each user is associated with feature information derived from their public activity, repositories, or profile characteristics.

The dataset contains:
* musae_git_edges.csv → Graph edges (source, target).

* musae_git_features.json → Node feature vectors.

* train_target.csv → Training labels.

* test_target.csv → Test nodes (labels hidden).

Graph Statistics:
* Nodes: ~37K.
* Edges: ~289K.
* Features: 128-dimensional node features.
* Task: Binary classification.

The GitHub Social Network dataset used in this challenge is publicly available through the Stanford Network Analysis Project (SNAP).\
🔗 **Dataset link:**  [Dataset](https://snap.stanford.edu/data/github-social.html)

## <img width="40" height="40" alt="image" src="https://github.com/user-attachments/assets/6e05cfef-3064-4d6d-bf4b-ea9259f21e11" />Evaluation Metric

The challenge is evaluated using **Macro F1-score**.

The F1-score is defined as:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Where:

- Precision = TP / (TP + FP)  
- Recall = TP / (TP + FN)

For binary classification, we compute the F1-score independently for each class and then average them:

Macro F1 = (F1_class_0 + F1_class_1) / 2

### Why Macro F1?

- Ensures balanced performance across classes  
- Prevents majority-class bias  
- Standard metric in graph node classification research  

Submissions will be ranked by **Macro F1-score on the hidden test set**. Higher Macro F1 values indicate better overall classification quality across all classes.

## ⚠️Constraints
To ensure fair competition:
1. No External Data, only the data provided for this challenge may be used.
2. No external node features, it must be derived solely from the given dataset.
3. No pretrained embeddings or models, all models must be trained from scratch using the provided data.
4. Keep your model simple and interpretable (deeper is not always better).
   
Think of this as a “from-scratch GNN challenge”, no shortcuts, no pretrained magic, just pure graph learning✨
