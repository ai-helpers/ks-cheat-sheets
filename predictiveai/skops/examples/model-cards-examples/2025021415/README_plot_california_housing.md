
# Model description

Gradient boosting regressor trained on California Housing dataset

The model is a gradient boosting regressor from sklearn. On top of the standard
features, it contains predictions from a KNN models. These predictions are calculated
out of fold, then added on top of the existing features. These features are really
helpful for decision tree-based models, since those cannot easily learn from geospatial
data.

## Intended uses & limitations

This model is meant for demonstration purposes

## Training Procedure

[More Information Needed]

### Hyperparameters

<details>
<summary> Click to expand </summary>

| Hyperparameter                                | Value                                                        |
|-----------------------------------------------|--------------------------------------------------------------|
| cv                                            |                                                              |
| estimators                                    | [('knn@5', Pipeline(steps=[('select_cols',<br />                 ColumnTransformer(transformers=[('long_and_lat', 'passthrough',<br />                                                  ['Longitude', 'Latitude'])])),<br />                ('knn', KNeighborsRegressor())]))]                                                              |
| final_estimator__alpha                        | 0.9                                                          |
| final_estimator__ccp_alpha                    | 0.0                                                          |
| final_estimator__criterion                    | friedman_mse                                                 |
| final_estimator__init                         |                                                              |
| final_estimator__learning_rate                | 0.1                                                          |
| final_estimator__loss                         | squared_error                                                |
| final_estimator__max_depth                    | 3                                                            |
| final_estimator__max_features                 |                                                              |
| final_estimator__max_leaf_nodes               |                                                              |
| final_estimator__min_impurity_decrease        | 0.0                                                          |
| final_estimator__min_samples_leaf             | 1                                                            |
| final_estimator__min_samples_split            | 2                                                            |
| final_estimator__min_weight_fraction_leaf     | 0.0                                                          |
| final_estimator__n_estimators                 | 500                                                          |
| final_estimator__n_iter_no_change             |                                                              |
| final_estimator__random_state                 | 0                                                            |
| final_estimator__subsample                    | 1.0                                                          |
| final_estimator__tol                          | 0.0001                                                       |
| final_estimator__validation_fraction          | 0.1                                                          |
| final_estimator__verbose                      | 0                                                            |
| final_estimator__warm_start                   | False                                                        |
| final_estimator                               | GradientBoostingRegressor(n_estimators=500, random_state=0)  |
| n_jobs                                        |                                                              |
| passthrough                                   | True                                                         |
| verbose                                       | 0                                                            |
| knn@5                                         | Pipeline(steps=[('select_cols',<br />                 ColumnTransformer(transformers=[('long_and_lat', 'passthrough',<br />                                                  ['Longitude', 'Latitude'])])),<br />                ('knn', KNeighborsRegressor())])                                                              |
| knn@5__memory                                 |                                                              |
| knn@5__steps                                  | [('select_cols', ColumnTransformer(transformers=[('long_and_lat', 'passthrough',<br />                                 ['Longitude', 'Latitude'])])), ('knn', KNeighborsRegressor())]                                                              |
| knn@5__verbose                                | False                                                        |
| knn@5__select_cols                            | ColumnTransformer(transformers=[('long_and_lat', 'passthrough',<br />                                 ['Longitude', 'Latitude'])])                                                              |
| knn@5__knn                                    | KNeighborsRegressor()                                        |
| knn@5__select_cols__n_jobs                    |                                                              |
| knn@5__select_cols__remainder                 | drop                                                         |
| knn@5__select_cols__sparse_threshold          | 0.3                                                          |
| knn@5__select_cols__transformer_weights       |                                                              |
| knn@5__select_cols__transformers              | [('long_and_lat', 'passthrough', ['Longitude', 'Latitude'])] |
| knn@5__select_cols__verbose                   | False                                                        |
| knn@5__select_cols__verbose_feature_names_out | True                                                         |
| knn@5__select_cols__long_and_lat              | passthrough                                                  |
| knn@5__knn__algorithm                         | auto                                                         |
| knn@5__knn__leaf_size                         | 30                                                           |
| knn@5__knn__metric                            | minkowski                                                    |
| knn@5__knn__metric_params                     |                                                              |
| knn@5__knn__n_jobs                            |                                                              |
| knn@5__knn__n_neighbors                       | 5                                                            |
| knn@5__knn__p                                 | 2                                                            |
| knn@5__knn__weights                           | uniform                                                      |

</details>

### Model Plot

<style>#sk-container-id-13 {/* Definition of color scheme common for light and dark mode */--sklearn-color-text: black;--sklearn-color-line: gray;/* Definition of color scheme for unfitted estimators */--sklearn-color-unfitted-level-0: #fff5e6;--sklearn-color-unfitted-level-1: #f6e4d2;--sklearn-color-unfitted-level-2: #ffe0b3;--sklearn-color-unfitted-level-3: chocolate;/* Definition of color scheme for fitted estimators */--sklearn-color-fitted-level-0: #f0f8ff;--sklearn-color-fitted-level-1: #d4ebff;--sklearn-color-fitted-level-2: #b3dbfd;--sklearn-color-fitted-level-3: cornflowerblue;/* Specific color for light theme */--sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));--sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));--sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));--sklearn-color-icon: #696969;@media (prefers-color-scheme: dark) {/* Redefinition of color scheme for dark theme */--sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));--sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));--sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));--sklearn-color-icon: #878787;}
}#sk-container-id-13 {color: var(--sklearn-color-text);
}#sk-container-id-13 pre {padding: 0;
}#sk-container-id-13 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;
}#sk-container-id-13 div.sk-dashed-wrapped {border: 1px dashed var(--sklearn-color-line);margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: var(--sklearn-color-background);
}#sk-container-id-13 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }`but bootstrap.min.css set `[hidden] { display: none !important; }`so we also need the `!important` here to be able to override thedefault hidden behavior on the sphinx rendered scikit-learn.org.See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;
}#sk-container-id-13 div.sk-text-repr-fallback {display: none;
}div.sk-parallel-item,
div.sk-serial,
div.sk-item {/* draw centered vertical line to link estimators */background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));background-size: 2px 100%;background-repeat: no-repeat;background-position: center center;
}/* Parallel-specific style estimator block */#sk-container-id-13 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 2px solid var(--sklearn-color-text-on-default-background);flex-grow: 1;
}#sk-container-id-13 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: var(--sklearn-color-background);position: relative;
}#sk-container-id-13 div.sk-parallel-item {display: flex;flex-direction: column;
}#sk-container-id-13 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;
}#sk-container-id-13 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;
}#sk-container-id-13 div.sk-parallel-item:only-child::after {width: 0;
}/* Serial-specific style estimator block */#sk-container-id-13 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: var(--sklearn-color-background);padding-right: 1em;padding-left: 1em;
}/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*//* Pipeline and ColumnTransformer style (default) */#sk-container-id-13 div.sk-toggleable {/* Default theme specific background. It is overwritten whether we have aspecific estimator or a Pipeline/ColumnTransformer */background-color: var(--sklearn-color-background);
}/* Toggleable label */
#sk-container-id-13 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.5em;box-sizing: border-box;text-align: center;
}#sk-container-id-13 label.sk-toggleable__label-arrow:before {/* Arrow on the left of the label */content: "▸";float: left;margin-right: 0.25em;color: var(--sklearn-color-icon);
}#sk-container-id-13 label.sk-toggleable__label-arrow:hover:before {color: var(--sklearn-color-text);
}/* Toggleable content - dropdown */#sk-container-id-13 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;/* unfitted */background-color: var(--sklearn-color-unfitted-level-0);
}#sk-container-id-13 div.sk-toggleable__content.fitted {/* fitted */background-color: var(--sklearn-color-fitted-level-0);
}#sk-container-id-13 div.sk-toggleable__content pre {margin: 0.2em;border-radius: 0.25em;color: var(--sklearn-color-text);/* unfitted */background-color: var(--sklearn-color-unfitted-level-0);
}#sk-container-id-13 div.sk-toggleable__content.fitted pre {/* unfitted */background-color: var(--sklearn-color-fitted-level-0);
}#sk-container-id-13 input.sk-toggleable__control:checked~div.sk-toggleable__content {/* Expand drop-down */max-height: 200px;max-width: 100%;overflow: auto;
}#sk-container-id-13 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";
}/* Pipeline/ColumnTransformer-specific style */#sk-container-id-13 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {color: var(--sklearn-color-text);background-color: var(--sklearn-color-unfitted-level-2);
}#sk-container-id-13 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: var(--sklearn-color-fitted-level-2);
}/* Estimator-specific style *//* Colorize estimator box */
#sk-container-id-13 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {/* unfitted */background-color: var(--sklearn-color-unfitted-level-2);
}#sk-container-id-13 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {/* fitted */background-color: var(--sklearn-color-fitted-level-2);
}#sk-container-id-13 div.sk-label label.sk-toggleable__label,
#sk-container-id-13 div.sk-label label {/* The background is the default theme color */color: var(--sklearn-color-text-on-default-background);
}/* On hover, darken the color of the background */
#sk-container-id-13 div.sk-label:hover label.sk-toggleable__label {color: var(--sklearn-color-text);background-color: var(--sklearn-color-unfitted-level-2);
}/* Label box, darken color on hover, fitted */
#sk-container-id-13 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {color: var(--sklearn-color-text);background-color: var(--sklearn-color-fitted-level-2);
}/* Estimator label */#sk-container-id-13 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;
}#sk-container-id-13 div.sk-label-container {text-align: center;
}/* Estimator-specific */
#sk-container-id-13 div.sk-estimator {font-family: monospace;border: 1px dotted var(--sklearn-color-border-box);border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;/* unfitted */background-color: var(--sklearn-color-unfitted-level-0);
}#sk-container-id-13 div.sk-estimator.fitted {/* fitted */background-color: var(--sklearn-color-fitted-level-0);
}/* on hover */
#sk-container-id-13 div.sk-estimator:hover {/* unfitted */background-color: var(--sklearn-color-unfitted-level-2);
}#sk-container-id-13 div.sk-estimator.fitted:hover {/* fitted */background-color: var(--sklearn-color-fitted-level-2);
}/* Specification for estimator info (e.g. "i" and "?") *//* Common style for "i" and "?" */.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {float: right;font-size: smaller;line-height: 1em;font-family: monospace;background-color: var(--sklearn-color-background);border-radius: 1em;height: 1em;width: 1em;text-decoration: none !important;margin-left: 1ex;/* unfitted */border: var(--sklearn-color-unfitted-level-1) 1pt solid;color: var(--sklearn-color-unfitted-level-1);
}.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {/* fitted */border: var(--sklearn-color-fitted-level-1) 1pt solid;color: var(--sklearn-color-fitted-level-1);
}/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {/* unfitted */background-color: var(--sklearn-color-unfitted-level-3);color: var(--sklearn-color-background);text-decoration: none;
}div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {/* fitted */background-color: var(--sklearn-color-fitted-level-3);color: var(--sklearn-color-background);text-decoration: none;
}/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {display: none;z-index: 9999;position: relative;font-weight: normal;right: .2ex;padding: .5ex;margin: .5ex;width: min-content;min-width: 20ex;max-width: 50ex;color: var(--sklearn-color-text);box-shadow: 2pt 2pt 4pt #999;/* unfitted */background: var(--sklearn-color-unfitted-level-0);border: .5pt solid var(--sklearn-color-unfitted-level-3);
}.sk-estimator-doc-link.fitted span {/* fitted */background: var(--sklearn-color-fitted-level-0);border: var(--sklearn-color-fitted-level-3);
}.sk-estimator-doc-link:hover span {display: block;
}/* "?"-specific style due to the `<a>` HTML tag */#sk-container-id-13 a.estimator_doc_link {float: right;font-size: 1rem;line-height: 1em;font-family: monospace;background-color: var(--sklearn-color-background);border-radius: 1rem;height: 1rem;width: 1rem;text-decoration: none;/* unfitted */color: var(--sklearn-color-unfitted-level-1);border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}#sk-container-id-13 a.estimator_doc_link.fitted {/* fitted */border: var(--sklearn-color-fitted-level-1) 1pt solid;color: var(--sklearn-color-fitted-level-1);
}/* On hover */
#sk-container-id-13 a.estimator_doc_link:hover {/* unfitted */background-color: var(--sklearn-color-unfitted-level-3);color: var(--sklearn-color-background);text-decoration: none;
}#sk-container-id-13 a.estimator_doc_link.fitted:hover {/* fitted */background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-13" class="sk-top-container" style="overflow: auto;"><div class="sk-text-repr-fallback"><pre>StackingRegressor(estimators=[(&#x27;knn@5&#x27;,Pipeline(steps=[(&#x27;select_cols&#x27;,ColumnTransformer(transformers=[(&#x27;long_and_lat&#x27;,&#x27;passthrough&#x27;,[&#x27;Longitude&#x27;,&#x27;Latitude&#x27;])])),(&#x27;knn&#x27;,KNeighborsRegressor())]))],final_estimator=GradientBoostingRegressor(n_estimators=500,random_state=0),passthrough=True)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-41" type="checkbox" ><label for="sk-estimator-id-41" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;StackingRegressor<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.StackingRegressor.html">?<span>Documentation for StackingRegressor</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>StackingRegressor(estimators=[(&#x27;knn@5&#x27;,Pipeline(steps=[(&#x27;select_cols&#x27;,ColumnTransformer(transformers=[(&#x27;long_and_lat&#x27;,&#x27;passthrough&#x27;,[&#x27;Longitude&#x27;,&#x27;Latitude&#x27;])])),(&#x27;knn&#x27;,KNeighborsRegressor())]))],final_estimator=GradientBoostingRegressor(n_estimators=500,random_state=0),passthrough=True)</pre></div> </div></div><div class="sk-serial"><div class="sk-item"><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><label>knn@5</label></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-serial"><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-42" type="checkbox" ><label for="sk-estimator-id-42" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;select_cols: ColumnTransformer<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.4/modules/generated/sklearn.compose.ColumnTransformer.html">?<span>Documentation for select_cols: ColumnTransformer</span></a></label><div class="sk-toggleable__content fitted"><pre>ColumnTransformer(transformers=[(&#x27;long_and_lat&#x27;, &#x27;passthrough&#x27;,[&#x27;Longitude&#x27;, &#x27;Latitude&#x27;])])</pre></div> </div></div><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-43" type="checkbox" ><label for="sk-estimator-id-43" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">long_and_lat</label><div class="sk-toggleable__content fitted"><pre>[&#x27;Longitude&#x27;, &#x27;Latitude&#x27;]</pre></div> </div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-44" type="checkbox" ><label for="sk-estimator-id-44" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">passthrough</label><div class="sk-toggleable__content fitted"><pre>passthrough</pre></div> </div></div></div></div></div></div></div><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-45" type="checkbox" ><label for="sk-estimator-id-45" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;KNeighborsRegressor<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.KNeighborsRegressor.html">?<span>Documentation for KNeighborsRegressor</span></a></label><div class="sk-toggleable__content fitted"><pre>KNeighborsRegressor()</pre></div> </div></div></div></div></div></div></div></div></div><div class="sk-item"><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label fitted sk-toggleable"><label>final_estimator</label></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-46" type="checkbox" ><label for="sk-estimator-id-46" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;GradientBoostingRegressor<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.4/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html">?<span>Documentation for GradientBoostingRegressor</span></a></label><div class="sk-toggleable__content fitted"><pre>GradientBoostingRegressor(n_estimators=500, random_state=0)</pre></div> </div></div></div></div></div></div></div></div></div></div></div>

## Evaluation Results

Metrics are calculated on the test set

| Metric                  |        Value |
|-------------------------|--------------|
| Root mean squared error | 44273.5      |
| Mean absolute error     | 30079.9      |
| R²                      |     0.805954 |

## Dataset description

California Housing dataset
--------------------------

**Data Set Characteristics:**

:Number of Instances: 20640

:Number of Attributes: 8 numeric, predictive attributes and the target

:Attribute Information:
    - MedInc        median income in block group
    - HouseAge      median house age in block group
    - AveRooms      average number of rooms per household
    - AveBedrms     average number of bedrooms per household
    - Population    block group population
    - AveOccup      average number of household members
    - Latitude      block group latitude
    - Longitude     block group longitude

:Missing Attribute Values: None

This dataset was obtained from the StatLib repository.
https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

The target variable is the median house value for California districts,
expressed in hundreds of thousands of dollars ($100,000).

This dataset was derived from the 1990 U.S. census, using one row per census
block group. A block group is the smallest geographical unit for which the U.S.
Census Bureau publishes sample data (a block group typically has a population
of 600 to 3,000 people).

A household is a group of people residing within a home. Since the average
number of rooms and bedrooms in this dataset are provided per household, these
columns may take surprisingly large values for block groups with few households
and many empty houses, such as vacation resorts.

It can be downloaded/loaded using the
:func:`sklearn.datasets.fetch_california_housing` function.

.. topic:: References

    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
      Statistics and Probability Letters, 33 (1997) 291-297

# How to Get Started with the Model

[More Information Needed]

# Model Card Authors

Benjamin Bossan

# Model Card Contact

benjamin@huggingface.co
