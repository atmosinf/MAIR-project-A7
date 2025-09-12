class BaselineInform:
    def predict(self, data: list) -> list:
        """
        Predict the given data using the classification algorithm.
        """
        return ['inform' for _ in range(len(data))]
