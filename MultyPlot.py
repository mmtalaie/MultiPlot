import matplotlib.pyplot as plt
import numpy as np


class MultiPlotter:
    def __init__(self, rows, colums, superTitle):
        self.rows = rows
        self.columns = colums
        self.subPlots = {}
        self.superTitle = superTitle

    def show(self):
        plt.suptitle(self.superTitle)
        for sub in self.subPlots:
            subPlot = self.subPlots[sub]
            box = subPlot.get_position()
            subPlot.set_position(
                [box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9]
            )
            subPlot.legend(
                loc="upper center",
                bbox_to_anchor=(0.5, -0.1),
                fancybox=True,
                shadow=True,
                ncol=5,
            )

        plt.show()

    def addPlotToSubPlot(
        self,
        index,
        x,
        y,
        ilabel,
        icolor,
        title="",
        xLabel="",
        yLabel="",
        annotateLast=True,
        isPercent=False,
        grid=False,
    ):

        if not (index in self.subPlots):
            self.subPlots[index] = plt.subplot(self.rows, self.columns, index)
        import matplotlib.ticker as ticker

        subplt = self.subPlots[index]
        subplt.spines["right"].set_visible(False)
        subplt.spines["top"].set_visible(False)
        if isPercent:
            subplt.yaxis.set_ticks(np.arange(0, 100, 10))
        subplt.tick_params(axis="y", labelrotation=20)
        if title != "":
            plt.title = title
        if xLabel != "":
            plt.xlabel(xLabel)
        if yLabel != "":
            plt.ylabel(yLabel)

        if grid:
            plt.grid(True)

        plt.plot(x, y, color=icolor, label=ilabel)
        if annotateLast:
            # slp = subplt.twinx()
            y = np.asarray(y)
            if isPercent:
                plt.annotate(
                    "%0.2f %%" % y[-1],
                    xy=(1, y[-1]),
                    xytext=(8, 0),
                    xycoords=("axes fraction", "data"),
                    textcoords="offset points",
                )
            else:
                plt.annotate(
                    "%0.2f " % y[-1],
                    xy=(1, y[-1]),
                    xytext=(8, 0),
                    xycoords=("axes fraction", "data"),
                    textcoords="offset points",
                )
