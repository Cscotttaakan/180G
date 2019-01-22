from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt
import xlrd
import matplotlib.patches as mpatches
import matplotlib.ticker as plticker


file_location = "/Users/craigscott/180G/BioLabDataClean.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)

for j in range(first_sheet.ncols):
    ser = [first_sheet.cell_value(i,j) for i in range(98)]

    fig, ax1 = plt.subplots()


# create some normal random noisy data
# ser = 50*np.random.rand() * np.random.normal(10, 10, 100) + 20
# plot normed histogram
    #plt.hist(ser, density=True)
    ax1.hist(ser)
    ax1.set_xlabel('Reaction Time (s)')
    ax1.set_ylabel('Frequency')
    plt.title('Craig/Yhoshua Reaction Times for ' + str(j + 1) + ' LED ')
     # this locator puts ticks at regular intervals
    ax1.xaxis.set_major_locator(plticker.MultipleLocator(base=0.2))



# find minimum and maximum of xticks, so we know
# where we should compute theoretical distribution
    ax2 = ax1.twinx()

    xt = plt.xticks()[0]
    xmin, xmax = min(xt), max(xt)
    lnspc = np.linspace(xmin, xmax, len(ser))

# lets try the normal distribution first
    #m, s = stats.norm.fit(ser) # get mean and standard deviation  
    #pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
    m, s = stats.norm.fit(ser) # get mean and standard deviation  
    pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
    #plt.legend(['Mean = ' + str(m), 'Sigma = ' + str(s)])
    mean = mpatches.Patch( label='Mean = ' + str(round(m, 5)) + ' s')
    stdev = mpatches.Patch( label='Sigma = ' + str(round(s, 5)))
    plt.legend(handles=[mean, stdev])


    ax2.plot(lnspc, pdf_g, label="Norm", color='tab:red') # plot it
    fig.tight_layout()
   # plt.plot(lnspc, label="Norm") # plot it




    plt.savefig('normaldistribution' + str(j) + '.png')
    ax1.clear()
    ax2.clear()
    fig.clear()
    plt.clf()
    plt.cla()
    plt.close()
