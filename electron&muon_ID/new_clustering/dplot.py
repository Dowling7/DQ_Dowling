import numpy as np
import matplotlib.pyplot as plt


def show_cluster(x,y,eng):
    x_bins = np.linspace(-150, 150, 50)
    y_bins = np.linspace(-150, 150, 50)
    bin_means = binned_statistic_2d(x, y, eng, statistic='mean',bins=[x_bins, y_bins])
    im = plt.imshow(np.flip(bin_means.statistic.T,0), extent=(-150, 150, -150, 150), aspect='auto')
    #cax = plt.axes([.95, .15, .075, .7])
    #plt.colorbar(cax=cax)
    plt.colorbar(im, label='Energy deposite/GeV')
    #plt.clim(0.,1.)
    plt.xlabel('EMCal x Position/cm')
    plt.ylabel('EMCal y Position/cm')
    plt.show()

def showe_clusters_ctr():
    # Generate random data points in two clusters
    np.random.seed(0)
    cluster1 = np.random.randn(100, 2) + np.array([5, 5])
    cluster2 = np.random.randn(100, 2) + np.array([10, 10])

    # Combine the data points into one dataset
    data = np.vstack([cluster1, cluster2])

    # Pre-defined cluster centers
    initial_centers = np.array([
        [5, 5],    # Center 1
        [10, 10],   # Center 2
        [9, 9]
    ])

    # Initialize K-means with pre-defined centers
    kmeans = KMeans(n_clusters=initial_centers.shape[0], init=initial_centers, n_init=1)
    kmeans.fit(data)

    # Get cluster assignments for each data point
    cluster_assignments = kmeans.labels_

    # Get the final cluster centers
    final_centers = kmeans.cluster_centers_

    # Plot the data points and cluster centers
    plt.scatter(data[:, 0], data[:, 1], c=cluster_assignments, cmap='rainbow')
    plt.scatter(final_centers[:, 0], final_centers[:, 1], marker='X', s=200, c='black', label='Final Centers')
    plt.scatter(initial_centers[:, 0], initial_centers[:, 1], marker='o', s=200, c='red', label='Initial Centers')
    plt.legend()
    plt.title('K-means Clustering with Pre-defined Centers')
    plt.show()


def emcal_page(x, y, eng):
    x_bins = np.linspace(-150, 150, 50)
    y_bins = np.linspace(-150, 150, 50)
    bin_means = binned_statistic_2d(x, y, eng, statistic='mean', bins=[x_bins, y_bins])
    
    fig, ax = plt.subplots()
    im = ax.imshow(np.flip(bin_means.statistic.T, 0), extent=(-150, 150, -150, 150), aspect='auto')
    plt.colorbar(im, ax=ax, label='Energy Deposit/GeV')
    ax.set_xlabel('EMCal x Position/cm')
    ax.set_ylabel('EMCal y Position/cm')
    
    return fig

def pdf_tuples():
    pdf_filename = 'Aee_9_emcal_plots.pdf'
    pdf_pages = PdfPages(pdf_filename)
    for i in range(len(x)):
        fig = emcal_eng(x[i],y[i],eng[i])
        pdf_pages.savefig(fig)
        plt.close(fig)  
    pdf_pages.close()


