import matplotlib.pyplot as plt
import numpy as np

def visualize_dft_matrix(mat : np.array):
    plt.figure(figsize=(15,20))
    plt.plot([0], "r", label="Real")
    plt.plot([1], "b", label="Imaginary")
    for i in range(mat.shape[0]):
        plt.plot(np.real(mat[i])/4 + 1*i, "or")
        plt.plot(np.imag(mat[i])/4 + 1*i, "ob")
        plt.plot(np.real(mat[i])/4 + 1*i, "r")
        plt.plot(np.imag(mat[i])/4 + 1*i, "b")
        plt.plot(1*i * np.ones(mat.shape[0]), "black")

    plt.xlabel("Column Indices")
    plt.ylabel("Row Indices")
    plt.title("Visualizing the DFT Matrix")

    plt.legend()
    plt.show()

def generate_gaussian_kernel(std, N):

    t2 = np.arange(-int(N/2),int(N/2))
    t2 = t2[(np.arange(N)+int(N/2)) % N]
    return np.exp(-(t2)**2/(2*std**2))/(np.sqrt(2*np.pi)*std)