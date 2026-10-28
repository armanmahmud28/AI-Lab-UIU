import csv
import numpy as np
import matplotlib.pyplot as plt


# 1. Constants


SPLIT_SEED = 42
MAX_ITER = 500
LEARNING_RATES = [0.1, 0.01, 0.001, 0.0001]

DATASET_PATH = "dataset.csv"



# 2. Load Dataset


with open(DATASET_PATH, "r", encoding="utf-8-sig", newline="") as file:
    dataset = list(csv.reader(file))


print("Number of samples:", len(dataset))
print("Number of columns:", len(dataset[0]))

print("\nFirst 5 rows:")
for row in dataset[:5]:
    print(row)


# 3. Convert Dataset to NumPy Array


data = np.array(dataset, dtype=float)

# All columns except last = features
X = data[:, :-1]

# Last column = target
y = data[:, -1].astype(int)


print("\nX shape:", X.shape)
print("y shape:", y.shape)
print("Unique labels:", np.unique(y))


# 4. Train / Validation / Test Split


rng = np.random.default_rng(SPLIT_SEED)

# Shuffle indices
indices = rng.permutation(len(X))

n_total = len(X)

n_train = int(0.70 * n_total)
n_val = int(0.15 * n_total)

n_test = n_total - n_train - n_val


# Split indices
train_idx = indices[:n_train]

val_idx = indices[n_train:n_train + n_val]

test_idx = indices[n_train + n_val:]


# Create datasets
X_train = X[train_idx]
y_train = y[train_idx]

X_val = X[val_idx]
y_val = y[val_idx]

X_test = X[test_idx]
y_test = y[test_idx]


print("\nTraining samples  :", len(X_train))
print("Validation samples:", len(X_val))
print("Test samples      :", len(X_test))


# 5. Sigmoid Function


def sigmoid(z):

    return 1 / (1 + np.exp(-z))



# 6. Train Logistic Regression


def train_logistic_regression(X_train, y_train, lr, max_iter=500):

    # Add bias column
    X_train_bias = np.c_[X_train, np.ones(len(X_train))]

    # Randomly initialize theta between 0 and 1
    rng = np.random.default_rng(SPLIT_SEED)

    theta = rng.random(X_train_bias.shape[1])

    history = []

    N_train = len(X_train_bias)

    # Training iterations
    for itr in range(max_iter):

        total_loss = 0.0

        # Process each sample
        for i in range(N_train):

            X_i = X_train_bias[i]

            y_i = y_train[i]

            # Calculate z

            z = np.dot(X_i, theta)

            # Calculate prediction
            

            h = sigmoid(z)

            # Calculate log loss
            
            h = np.clip(h, 1e-15, 1 - 1e-15)

            loss = -y_i * np.log(h) - (1 - y_i) * np.log(1 - h)

            total_loss += loss

            # Calculate gradient

            dv = X_i * (h - y_i)

            
            # Update theta
            
            theta = theta - dv * lr

        # Average training loss
        average_loss = total_loss / N_train

        history.append(average_loss)

    return theta, history



# 7. Calculate Accuracy


def calculate_accuracy(X_data, y_data, theta):

    # Add bias
    X_data_bias = np.c_[X_data, np.ones(len(X_data))]

    correct = 0

    for i in range(len(X_data_bias)):

        X_i = X_data_bias[i]

        y_i = y_data[i]

        # Calculate z
        z = np.dot(X_i, theta)

        # Probability
        h = sigmoid(z)

        if h >= 0.5:
            prediction = 1
        else:
            prediction = 0

        # Check predictiong
        if prediction == y_i:
            correct += 1

    accuracy = correct * 100 / len(X_data)

    return accuracy


# 8. Train Using Different Learning Rates

results = []

best_lr = None
best_val_acc = -1
best_theta = None
best_history = None


for lr in LEARNING_RATES:

    print("\nTraining with learning rate:", lr)

    theta, history = train_logistic_regression(
        X_train,
        y_train,
        lr,
        MAX_ITER
    )

    # Validation accuracy
    val_acc = calculate_accuracy(
        X_val,
        y_val,
        theta
    )

    results.append((lr, val_acc))

    print("Validation Accuracy:", val_acc)

    # Check whether this is the best learning rate
    if val_acc > best_val_acc:

        best_val_acc = val_acc
        best_lr = lr
        best_theta = theta
        best_history = history


# 9. Learning Rate vs Validation Accuracy Table

print("\n==========================================")
print("Learning Rate vs Validation Accuracy: ")
print("==========================================")

print(f"{'Learning Rate':<20} {'Validation Accuracy'}")

for lr, val_acc in results:

    print(f"{lr:<20} {val_acc:.2f}%")


print("\nBest Learning Rate:", best_lr)
print("Best Validation Accuracy:", best_val_acc)


# ============================================================
# 10. Test Accuracy
# ============================================================

test_acc = calculate_accuracy(
    X_test,
    y_test,
    best_theta
)


print("\n==========================================")
print("Final Test Result")
print("==========================================")

print("Selected Learning Rate:", best_lr)
print("Test Accuracy:", test_acc)


    # 11. Plot Training Loss

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, MAX_ITER + 1),
    best_history
)

plt.xlabel("Iteration")

plt.ylabel("Training Loss")

plt.title(
    f"Training Loss vs Iteration "
    f"(Learning Rate = {best_lr})"
)

plt.grid(True)

plt.show()