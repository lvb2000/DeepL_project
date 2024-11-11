import matplotlib.pyplot as plt
import pandas as pd

def smooth_data(data,alpha=0.01):
    return data.ewm(alpha=alpha).mean()
def clip_data(data,length=1000):
    data = data.drop(columns=["run_id"])
    # drop all rows with step values > length
    data = data[data["step"]<=length]
    return data
def read_data(file_name):
    data = pd.read_csv(file_name)
    return data

def biggest_difference(ids,data):
    arr = []
    for id in ids:
        d = data[data["run_id"]==id]
        d = clip_data(d,100000)
        print(d.shape)
        arr.append(d)
    # get only row values
    arr = [d["value"].values for d in arr]
    # comput absolute difference between arr[0] and arr[1]
    diff = [abs(arr[0]-arr[1]) for arr in zip(*arr)]
    # get index of max difference
    max_index = diff.index(max(diff))
    return max_index

if __name__ == "__main__":
    ZOOM = False
    f,ax = plt.subplots()
    f.set_figwidth(10)
    f.set_figheight(5)
    data=read_data("plots/minatar_seaquest_return.csv")
    data_drop=data.drop(columns=["key"])
    data_drop=data_drop.drop(columns=["timestamp"])
    unqiue_run_ids = data_drop["run_id"].unique()
    #biggest_difference(unqiue_run_ids,data_drop)
    # flip unique ideas
    #unqiue_run_ids = unqiue_run_ids[::-1]
    labels = ["vanilla DreamerV2","pretrained DreamerV2","pretrained DreamerV2 RSMM fixed"]
    # Create inset axes for zooming
    if ZOOM:
        ax_inset = ax.inset_axes([0.2, 0.5, 0.35, 0.35],xlim=(0, 1000), ylim=(1, 5), xticklabels=[], yticklabels=[])
    for index,ids in enumerate(unqiue_run_ids):
        data_run = data_drop[data_drop["run_id"]==ids]
        data_clip = clip_data(data_run,100000)
        data_index = data_clip.set_index("step")
        data_smooth = smooth_data(data_index)
        plt.plot(data_smooth,label=labels[index])
        if ZOOM:
            # Plot data in inset axes
            data_inset = clip_data(data_run,5000)
            data_inset_index = data_inset.set_index("step")
            data_inset_smooth = smooth_data(data_inset_index)
            ax_inset.plot(data_inset_smooth, label=labels[index])
            ax_inset.set_ylim([1, 5])
            ax_inset.set_xlim([0, 5000])
            ax_inset.vlines(1000, 2.4, 4.5, colors='r', linestyles='--', lw=1)
            ax.indicate_inset_zoom(ax_inset, edgecolor="red",linestyle='--')

    # Configure Plot
    plt.xlabel("Training Steps", fontsize='18')
    plt.ylabel("Agent Policy Return", fontsize='18')
    plt.legend(fontsize='15')
    plt.savefig("metrics.png")
    plt.close()