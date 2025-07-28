def evaluate_model(mse, threshold=50):
    """
    Evaluate the model performance.
    Args:
        mse (float): The model's mean squared error.
        threshold (float): The maximum allowed MSE to pass.
    Returns:
        bool: True if the model passes the evaluation.
    """
    if mse < threshold:
        print(f"✅ Model passed evaluation: MSE {mse:.4f} < {threshold}")
        return True
    else:
        print(f"❌ Model failed evaluation: MSE {mse:.4f} >= {threshold}")
        return False
