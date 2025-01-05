# import joblib

# # Load the scaler
# scaler = joblib.load('scaling.pkl')  # Replace with your scaler file path
# print("Number of features expected by StandardScaler:", scaler.n_features_in_)

# if hasattr(scaler, 'feature_names_in_'):
#     print("Features expected by StandardScaler:", scaler.feature_names_in_)
# else:
#     print("Feature names not stored in StandardScaler.")

import joblib

# Load the model
model = joblib.load('regmodel.pkl')  # Replace with your model file path

# Check if feature names are stored
if hasattr(model, 'feature_names_in_'):
    print("Features expected by model:", model.feature_names_in_)
else:
    print("Feature names not stored in model.")