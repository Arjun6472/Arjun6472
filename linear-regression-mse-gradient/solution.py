import numpy as np


def mse_gradient(
    input: np.ndarray,
    weight: np.ndarray,
    bias: np.ndarray | None,
    target: np.ndarray,
) -> tuple[np.ndarray, np.ndarray | None]:
    prediction = input @ weight.T
    if bias is not None:
        prediction += bias
    element_count = prediction.size
    grad_prediction = (2.0 / element_count) * (prediction - target)
    grad_weight = grad_prediction.T @ input
    grad_bias = None if bias is None else grad_prediction.sum(axis=0)
    return grad_weight, grad_bias
        
    """
    input:  shape (batch_size, in_features)
    weight: shape (out_features, in_features)
    bias:   shape (out_features,), or None
    target: shape (batch_size, out_features)

    Returns:
        grad_weight: same shape as weight
        grad_bias: same shape as bias, or None if bias is None
    """
    # TODO: Implement the gradient formulas derived in Theory.
    # Do not use an autograd library -- these are the manual derivatives.
    pass
