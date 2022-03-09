import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import argparse

def instance_fig(file_name):
    ###############################################
    # for instance1
    ###############################################
    df = pd.read_csv(file_name)
    df1 = df.loc[df['instance'] == 'i-1.txt']
    
    _df1 = df1.loc[df1['algorithm'] == 'round-robin']
    _df2 = df1.loc[df1['algorithm'] == 'ucb']
    _df3 = df1.loc[df1['algorithm'] == 'kl-ucb']
    _df4 = df1.loc[df1['algorithm'] == 'thompson-sampling']  
    _df5 = df1.loc[df1['algorithm'] == 'epsilon-greedy']

    #round-robin
    x = _df1['horizon'].unique()
    y1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_1 = _df1.loc[_df1["horizon"] == x[i]]
        y1[i] = df_1["REG"].mean(axis=0)
    plt.plot(x,y1)

    #epsilon 0.002
    _df_e2 = _df5.loc[_df5["epsilon"] == 0.002]
    y_e2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e2 = _df_e2.loc[_df_e2['horizon'] == x[i]]
        y_e2[i] = df_e2['REG'].mean(axis=0)
    plt.plot(x,y_e2)

    #epsilon 0.02
    _df_e1 = _df5.loc[_df5["epsilon"] == 0.02]
    y_e1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e1 = _df_e1.loc[_df_e1['horizon'] == x[i]]
        y_e1[i] = df_e1['REG'].mean(axis=0)
    plt.plot(x,y_e1)

    #epsilon 0.2
    _df_e0 = _df5.loc[_df5["epsilon"] == 0.2]
    y_e0 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e0 = _df_e0.loc[_df_e0['horizon'] == x[i]]
        y_e0[i] = df_e0['REG'].mean(axis=0)
    plt.plot(x,y_e0)

    #ucb
    y2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_2 = _df2.loc[_df2["horizon"] == x[i]]
        y2[i] = df_2["REG"].mean(axis=0)
    plt.plot(x,y2)

    #kl-ucb
    y3 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_3 = _df3.loc[_df3['horizon'] == x[i]]
        y3[i] = df_3['REG'].mean(axis=0)
    plt.plot(x,y3)
    
    #thomsan-sampling
    y4 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_4 = _df4.loc[_df4['horizon'] == x[i]]
        y4[i] = df_4['REG'].mean(axis=0)
    plt.plot(x,y4)


    plt.legend(["round-robin","epsilon-greedy with epsilon=0.002",
                 "epsilon-greedy with epsilon=0.02", 
                 "epsilon-greedy with epsilon=0.2", "ucb", "kl-ucb",
                  "thompson-sampling"],loc="upper left")
    plt.title("Instance1 - both axes in log scale")
    plt.xlabel("horizon")
    plt.ylabel("Regret")
    plt.yscale('log')
    plt.xscale('log')
    # plt.show()
    plt.savefig("instance1.png")
    plt.close()
   
    ###############################################
    # for instance2
    ###############################################
    df1 = df.loc[df['instance'] == 'i-2.txt']

    _df1 = df1.loc[df1['algorithm'] == 'round-robin']
    _df2 = df1.loc[df1['algorithm'] == 'ucb']
    _df3 = df1.loc[df1['algorithm'] == 'kl-ucb']
    _df4 = df1.loc[df1['algorithm'] == 'thompson-sampling']  
    _df5 = df1.loc[df1['algorithm'] == 'epsilon-greedy']

    #round-robin
    x = _df1['horizon'].unique()
    y1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_1 = _df1.loc[_df1["horizon"] == x[i]]
        y1[i] = df_1["REG"].mean(axis=0)
    plt.plot(x,y1)

    #epsilon 0.002
    _df_e2 = _df5.loc[_df5["epsilon"] == 0.002]
    y_e2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e2 = _df_e2.loc[_df_e2['horizon'] == x[i]]
        y_e2[i] = df_e2['REG'].mean(axis=0)
    plt.plot(x,y_e2)

    #epsilon 0.02
    _df_e1 = _df5.loc[_df5["epsilon"] == 0.02]
    y_e1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e1 = _df_e1.loc[_df_e1['horizon'] == x[i]]
        y_e1[i] = df_e1['REG'].mean(axis=0)
    plt.plot(x,y_e1)

    #epsilon 0.2
    _df_e0 = _df5.loc[_df5["epsilon"] == 0.2]
    y_e0 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e0 = _df_e0.loc[_df_e0['horizon'] == x[i]]
        y_e0[i] = df_e0['REG'].mean(axis=0)
    plt.plot(x,y_e0)

    #ucb
    y2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_2 = _df2.loc[_df2["horizon"] == x[i]]
        y2[i] = df_2["REG"].mean(axis=0)
    plt.plot(x,y2)

    #kl-ucb
    y3 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_3 = _df3.loc[_df3['horizon'] == x[i]]
        y3[i] = df_3['REG'].mean(axis=0)
    plt.plot(x,y3)

    #thomsan-sampling
    y4 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_4 = _df4.loc[_df4['horizon'] == x[i]]
        y4[i] = df_4['REG'].mean(axis=0)
    plt.plot(x,y4)


    plt.legend(["round-robin","epsilon-greedy with epsilon=0.002",
                 "epsilon-greedy with epsilon=0.02", 
                 "epsilon-greedy with epsilon=0.2", "ucb", "kl-ucb",
                  "thompson-sampling"],loc="upper left")
    plt.title("Instance2 - both axes in log scale")
    plt.xlabel("horizon")
    plt.ylabel("Regret")
    plt.yscale('log')
    plt.xscale('log')
    # plt.show()
    plt.savefig("instance2.png")
    plt.close()

    ###############################################
    # for instance3
    ###############################################
    df1 = df.loc[df['instance'] == 'i-3.txt']

    _df1 = df1.loc[df1['algorithm'] == 'round-robin']
    _df2 = df1.loc[df1['algorithm'] == 'ucb']
    _df3 = df1.loc[df1['algorithm'] == 'kl-ucb']
    _df4 = df1.loc[df1['algorithm'] == 'thompson-sampling']  
    _df5 = df1.loc[df1['algorithm'] == 'epsilon-greedy']

    #round-robin
    x = _df1['horizon'].unique()
    y1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_1 = _df1.loc[_df1["horizon"] == x[i]]
        y1[i] = df_1["REG"].mean(axis=0)
    plt.plot(x,y1)

    #epsilon 0.002
    _df_e2 = _df5.loc[_df5["epsilon"] == 0.002]
    y_e2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e2 = _df_e2.loc[_df_e2['horizon'] == x[i]]
        y_e2[i] = df_e2['REG'].mean(axis=0)
    plt.plot(x,y_e2)

    #epsilon 0.02
    _df_e1 = _df5.loc[_df5["epsilon"] == 0.02]
    y_e1 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e1 = _df_e1.loc[_df_e1['horizon'] == x[i]]
        y_e1[i] = df_e1['REG'].mean(axis=0)
    plt.plot(x,y_e1)

    #epsilon 0.2
    _df_e0 = _df5.loc[_df5["epsilon"] == 0.2]
    y_e0 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_e0 = _df_e0.loc[_df_e0['horizon'] == x[i]]
        y_e0[i] = df_e0['REG'].mean(axis=0)
    plt.plot(x,y_e0)

    #ucb
    y2 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_2 = _df2.loc[_df2["horizon"] == x[i]]
        y2[i] = df_2["REG"].mean(axis=0)
    plt.plot(x,y2)

    #kl-ucb
    y3 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_3 = _df3.loc[_df3['horizon'] == x[i]]
        y3[i] = df_3['REG'].mean(axis=0)
    plt.plot(x,y3)

    #thomsan-sampling
    y4 = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        df_4 = _df4.loc[_df4['horizon'] == x[i]]
        y4[i] = df_4['REG'].mean(axis=0)
    plt.plot(x,y4)


    plt.legend(["round-robin","epsilon-greedy with epsilon=0.002",
                 "epsilon-greedy with epsilon=0.02", 
                 "epsilon-greedy with epsilon=0.2", "ucb", "kl-ucb",
                  "thompson-sampling"],loc="upper left")
    plt.title("Instance3 - both axes in log scale")
    plt.xlabel("horizon")
    plt.ylabel("Regret")
    plt.yscale('log')
    plt.xscale('log')
    # plt.show()
    plt.savefig("instance3.png")
    plt.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    args = parser.parse_args()
    file_name = open(args.data, "r")
    
    instance_fig(file_name)

    file_name.close()

if __name__ == "__main__":
    main()   