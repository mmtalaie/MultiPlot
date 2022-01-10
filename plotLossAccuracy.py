import pandas as pd
from MultyPlot import MultiPlotter

file_name = "data.csv"
trainLoss = "Train loss"
validLoss = "Valid loss"
curAcc = "Current_accuracy"
bestAcc = "Best_accuracy"
curNrm = "Current_norm_ED"
bestNrm = "Best_norm_ED"


# plt.suptitle("Model Name")

df = pd.read_csv(file_name)
iter = []
f = 0
for i in list(df[validLoss]):
    if f == 0:
        iter.append(1)
    else:
        iter.append(f + 2000)
    f += 2000

print(df.info())

plot = MultiPlotter(1, 2, "superTitle")
plot.addPlotToSubPlot(
    1,
    iter,
    list(df[validLoss]),
    "Validation loss",
    "red",
    "Loss",
    "Itertation",
    "Loss",
    grid=True,
)
plot.addPlotToSubPlot(1, iter, list(df[trainLoss]), "Train loss", "gray")

plot.addPlotToSubPlot(
    2,
    iter,
    list(df[curAcc]),
    "acc",
    "green",
    "Accuracy",
    "Itertation",
    "Accuracy",
    isPercent=True,
    grid=True,
)
plot.show()
# ax = plt.subplot(1, 2, 1)
# plt.title("Validation Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
# valLoss = list(df[validLoss])
# plt.plot(iter, valLoss, color="red", label="loss")

# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
# ax.legend(
#     loc="upper center", bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5
# )


# crAccuracy = list(df[curAcc])
# plt.subplot(1, 2, 2)
# plt.plot(iter, crAccuracy, color="green")
# plt.xlabel("Iteration")
# plt.ylabel("Accuracy")
# plt.title("Valication Accuracy")
# plt.grid(True)
# plt.show()
