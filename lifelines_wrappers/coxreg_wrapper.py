from lifelines import CoxPHFitter
from sklearn.base import BaseEstimator
from pandas import read_json, to_json


class CoxRegression(BaseEstimator):
    def __init__(self, duration_column=None, prediction_type='survival', event_column=None, include_likelihood=False,
                 strata=None, alpha=0.95, tie_method='Efron', penalizer=0.0):
        self.alpha = alpha
        self.tie_method = tie_method
        self.penalizer = penalizer

        self.duration_column = duration_column
        self.event_column = event_column
        self.estimator = None

        self.include_likelihood = include_likelihood
        self.strata = strata
        self.prediction_type = prediction_type
        self.is_fitted = False

    def fit(self, X, y, **fit_params):
        X_ = X.copy()
        X_[self.duration_column] = y

        params = self.get_params()
        est = CoxPHFitter(**params)

        est.fit(X_, duration_col=self.duration_column, event_col=self.event_column, strata=self.strata, **fit_params)
        self.estimator = est
        self.is_fitted = True

        return self

    def check_fitted_model(self):
        if not self.is_fitted:
            raise Exception("ERROR: Model is not fitted.")

    def predict(self, X):
        self.check_fitted_model()


        if self.prediction_type == 'survival':
            prediction = self.estimator.predict_survival_function(read_json(X, orient='split'))
        else:
            prediction = self.estimator.predict_expectation(read_json(X, orient='split'))[0].values

        return to_json(prediction, orient='split')

    def print_summary(self):
        self.check_fitted_model()
        self.estimator.print_summary()

    def information(self):
        self.check_fitted_model()
        self.print_summary()

    def get_params(self, deep=True):
        return {"alpha": self.alpha, "tie_method": self.tie_method, "penalizer": self.penalizer}
