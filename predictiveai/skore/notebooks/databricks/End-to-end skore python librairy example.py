# Databricks notebook source
!pip install skrub skore
!pip install -U scikit-learn

# COMMAND ----------

import skore

project = skore.open("my_project", create=True)

# COMMAND ----------

    from skrub.datasets import fetch_employee_salaries

    datasets = fetch_employee_salaries()
    df, y = datasets.X, datasets.y

# COMMAND ----------

    from skrub import TableReport

    table_report = TableReport(df)
    table_report

# COMMAND ----------

project.put("Input data summary", table_report)


# COMMAND ----------

# MAGIC %md
# MAGIC ## Modelling
# MAGIC In a first attempt, we define a rather complex predictive model that uses a linear model as a base estimator.

# COMMAND ----------

import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, SplineTransformer
from sklearn.linear_model import RidgeCV
from skrub import DatetimeEncoder, ToDatetime, DropCols


def periodic_spline_transformer(period, n_splines=None, degree=3):
    if n_splines is None:
        n_splines = period
    n_knots = n_splines + 1  # periodic and include_bias is True
    return SplineTransformer(
        degree=degree,
        n_knots=n_knots,
        knots=np.linspace(0, period, n_knots).reshape(n_knots, 1),
        extrapolation="periodic",
        include_bias=True,
    )


categorical_features = [
    "gender",
    "department_name",
    "division",
    "assignment_category",
    "employee_position_title",
    "year_first_hired",
]
datetime_features = "date_first_hired"

date_encoder = make_pipeline(
    ToDatetime(),
    DatetimeEncoder(resolution="day", add_weekday=True, add_total_seconds=False),
    DropCols("date_first_hired_year"),
)

date_engineering = make_column_transformer(
    (periodic_spline_transformer(12, n_splines=6), ["date_first_hired_month"]),
    (periodic_spline_transformer(31, n_splines=15), ["date_first_hired_day"]),
    (periodic_spline_transformer(7, n_splines=3), ["date_first_hired_weekday"]),
)

feature_engineering_date = make_pipeline(date_encoder, date_engineering)

preprocessing = make_column_transformer(
    (feature_engineering_date, datetime_features),
    (OneHotEncoder(drop="if_binary", handle_unknown="ignore"), categorical_features),
)

model = make_pipeline(preprocessing, RidgeCV(alphas=np.logspace(-3, 3, 100)))
model

# COMMAND ----------

# MAGIC %md
# MAGIC In the diagram above, we can see what how we performed our feature engineering:
# MAGIC
# MAGIC For categorical features, we use a OneHotEncoder to transform the categorical features. From the previous data exploration using a TableReport, from the “Stats” tab, one may have looked at the number of unique values and observed that we have feature with a large cardinality. In such cases, one-hot encoding might not be the best choice, but this is our starting point to get the ball rolling.
# MAGIC
# MAGIC Then, we have another transformation to encode the date features. We first split the date into multiple features (day, month, and year). Then, we apply a periodic spline transformation to each of the date features to capture the periodicity of the data.
# MAGIC
# MAGIC Finally, we fit a RidgeCV model.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Model evaluation using skore.CrossValidationReport
# MAGIC #### First model
# MAGIC Now, we want to evaluate this complex model via cross-validation (with 5 folds). For that, we use skore’s CrossValidationReport to investigate the performance of our model.

# COMMAND ----------

from skore import CrossValidationReport

report = CrossValidationReport(estimator=model, X=df, y=y, cv_splitter=5)
report.help()

# COMMAND ----------

# MAGIC %md
# MAGIC We observe that the cross-validation report detected that we have a regression task and provides us with some metrics and plots that make sense for our specific problem at hand.
# MAGIC
# MAGIC To accelerate any future computation (e.g. of a metric), we cache once and for all the predictions of our model. Note that we don’t necessarily need to cache the predictions as the report will compute them on the fly (if not cached) and cache them for us.

# COMMAND ----------

import warnings

with warnings.catch_warnings():
    # catch the warnings raised by the OneHotEncoder for seeing unknown categories
    # at transform time
    warnings.simplefilter(action="ignore", category=UserWarning)
    report.cache_predictions(n_jobs=3)

# COMMAND ----------

# MAGIC %md
# MAGIC To not lose this cross-validation report, let’s store it in our skore project.

# COMMAND ----------

project.put("Linear model report", report)


# COMMAND ----------

# MAGIC %md
# MAGIC We can now have a look at the performance of the model with some standard metrics.

# COMMAND ----------

report.metrics.report_metrics(aggregate=["mean", "std"])


# COMMAND ----------

# MAGIC %md
# MAGIC ### Second model
# MAGIC Now that we have our first baseline model, we can try an out-of-the-box model: skrub’s TableVectorizer that makes the feature engineering for us. To deal with the high cardinality of the categorical features, we use a TextEncoder that uses a language model and an embedding model to encode the categorical features.
# MAGIC
# MAGIC Finally, we use a HistGradientBoostingRegressor as a base estimator that is a rather robust model.

# COMMAND ----------

from skrub import TableVectorizer, TextEncoder
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.pipeline import make_pipeline

model = make_pipeline(
    TableVectorizer(high_cardinality=TextEncoder()),
    HistGradientBoostingRegressor(),
)
model

# COMMAND ----------

# MAGIC %md
# MAGIC Let’s compute the cross-validation report for this model.

# COMMAND ----------

report = CrossValidationReport(estimator=model, X=df, y=y, cv_splitter=5, n_jobs=3)
report.help()

# COMMAND ----------

# MAGIC %md
# MAGIC We cache the predictions for later use.

# COMMAND ----------

report.cache_predictions(n_jobs=3)

# COMMAND ----------

# MAGIC %md
# MAGIC We store the report in our skore project.

# COMMAND ----------

project.put("HGBDT model report", report)

# COMMAND ----------

# MAGIC %md
# MAGIC We can now have a look at the performance of the model with some standard metrics.
# MAGIC
# MAGIC

# COMMAND ----------

report.metrics.report_metrics(aggregate=["mean", "std"])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Investigating the models
# MAGIC At this stage, we might not been careful and have already overwritten the report and model from our first attempt. Hopefully, because we stored the reports in our skore project, we can easily retrieve them. So let’s retrieve the reports.

# COMMAND ----------

linear_model_report = project.get("Linear model report")
hgbdt_model_report = project.get("HGBDT model report")

# COMMAND ----------

# MAGIC %md
# MAGIC Now that we retrieved the reports, we can make further comparison and build upon some usual pandas operations to concatenate the results.

# COMMAND ----------

import pandas as pd

results = pd.concat(
    [
        linear_model_report.metrics.report_metrics(aggregate=["mean", "std"]),
        hgbdt_model_report.metrics.report_metrics(aggregate=["mean", "std"]),
    ]
)
results

# COMMAND ----------

# MAGIC %md
# MAGIC In addition, if we forgot to compute a specific metric (e.g. mean_absolute_error()), we can easily add it to the report, without re-training the model and even without re-computing the predictions since they are cached internally in the report. This allows us to save some potentially huge computation time.

# COMMAND ----------

from sklearn.metrics import mean_absolute_error

scoring = ["r2", "rmse", mean_absolute_error]
scoring_kwargs = {"response_method": "predict"}
scoring_names = ["R2", "RMSE", "MAE"]
results = pd.concat(
    [
        linear_model_report.metrics.report_metrics(
            scoring=scoring,
            scoring_kwargs=scoring_kwargs,
            scoring_names=scoring_names,
            aggregate=["mean", "std"],
        ),
        hgbdt_model_report.metrics.report_metrics(
            scoring=scoring,
            scoring_kwargs=scoring_kwargs,
            scoring_names=scoring_names,
            aggregate=["mean", "std"],
        ),
    ]
)
results

# COMMAND ----------

# MAGIC %md
# MAGIC Finally, we can even get the individual EstimatorReport for each fold from the cross-validation to make further analysis. Here, we plot the actual vs predicted values for each fold.
# MAGIC
# MAGIC

# COMMAND ----------

from itertools import zip_longest
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=2, nrows=3, figsize=(12, 18))
for split_idx, (ax, estimator_report) in enumerate(
    zip_longest(axs.flatten(), linear_model_report.estimator_reports_)
):
    if estimator_report is None:
        ax.axis("off")
        continue
    estimator_report.metrics.plot.prediction_error(kind="actual_vs_predicted", ax=ax)
    ax.set_title(f"Split #{split_idx + 1}")
    ax.legend(loc="lower right")
plt.tight_layout()

# COMMAND ----------

# MAGIC %md
# MAGIC Cleanup the project
# MAGIC Let’s clear the skore project (to avoid any conflict with other documentation examples).

# COMMAND ----------

project.clear()