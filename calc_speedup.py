import matplotlib.pyplot as plt

def show_speedup():
    N = [4, 8, 16, 32, 64]
    P = [2, 4, 8, 16, 32]
    speedup = [
        [1.9829787234042553, 1.9904761904761905, 2.002070393374741, 2.0, 1.9801980198019802],
        [3.949152542372881, 3.96584440227704, 3.9958677685950414, 4.0, 3.992015968063872],
        [7.62684124386252, 7.798507462686567, 7.926229508196721, 7.956204379562044, 7.968127490039841],
        [14.427244582043345, 15.144927536231883, 15.571658615136876, 15.740072202166065, 15.873015873015873],
        [16.124567474048444, 21.479958890030833, 27.239436619718308, 29.261744966442954, 30.627871362940276]
    ]

    for i, p in enumerate(P):
        plt.subplot(2, 2, 3)
        plt.plot(N, speedup[i], label=f'P = {p}')

    plt.xlabel('Cantidad de N')
    plt.ylabel('Speedup')
    plt.title('Speedup vs Cantidad de Cuerpos (N)')
    plt.legend()
    #plt.show()
    