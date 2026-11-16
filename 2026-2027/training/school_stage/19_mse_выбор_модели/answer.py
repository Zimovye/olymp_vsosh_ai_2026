teaching = [(-0.5, -0.75), (0, -0.5), (0.5, 1.25), (1, 1.5)]
verification = [(2, 5.0), (3, 11.5), (4, 14.0)]

model_1_info = {"name": "Model 1", "errors": [], "MSE": 0}
model_2_info = {"name": "Model 2", "errors": [], "MSE": 0}
model_3_info = {"name": "Model 3", "errors": [], "MSE": 0}
model_4_info = {"name": "Model 4", "errors": [], "MSE": 0}
for x, y in teaching:
    model_1_pred = 2 * x
    model_1_info["errors"].append((y - model_1_pred) ** 2)

    model_2_pred = x + 0.5
    model_2_info["errors"].append((y - model_2_pred) ** 2)

    model_3_pred = (x + 2) ** 2 / 2 - 2
    model_3_info["errors"].append((y - model_3_pred) ** 2)

    model_4_pred = (x + 1) ** 2 - 1
    model_4_info["errors"].append((y - model_4_pred) ** 2)

model_1_info["MSE"] = sum(model_1_info["errors"]) / len(model_1_info["errors"])
model_2_info["MSE"] = sum(model_2_info["errors"]) / len(model_2_info["errors"])
model_3_info["MSE"] = sum(model_3_info["errors"]) / len(model_3_info["errors"])
model_4_info["MSE"] = sum(model_4_info["errors"]) / len(model_4_info["errors"])

best_teaching = min(
    [model_1_info, model_2_info, model_3_info, model_4_info], key=lambda x: x["MSE"]
)
print(f"Для обучающего набора лучшая модель: {best_teaching['name']}")

for x, y in verification:
    model_1_pred = 2 * x
    model_1_info["errors"].append((y - model_1_pred) ** 2)

    model_2_pred = x + 0.5
    model_2_info["errors"].append((y - model_2_pred) ** 2)

    model_3_pred = (x + 2) ** 2 / 2 - 2
    model_3_info["errors"].append((y - model_3_pred) ** 2)

    model_4_pred = (x + 1) ** 2 - 1
    model_4_info["errors"].append((y - model_4_pred) ** 2)

model_1_info["MSE"] = sum(model_1_info["errors"]) / len(model_1_info["errors"])
model_2_info["MSE"] = sum(model_2_info["errors"]) / len(model_2_info["errors"])
model_3_info["MSE"] = sum(model_3_info["errors"]) / len(model_3_info["errors"])
model_4_info["MSE"] = sum(model_4_info["errors"]) / len(model_4_info["errors"])

best_teaching_and_verification = min(
    [model_1_info, model_2_info, model_3_info, model_4_info], key=lambda x: x["MSE"]
)
print(
    f"Для точек из обоих наборов сразу лучшая модель: {best_teaching_and_verification['name']}"
)
