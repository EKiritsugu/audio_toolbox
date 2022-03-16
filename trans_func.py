from scipy import signal


def Mstft(Sig_ori , fft_len=2048 , lap_len=1024):
    # Sig_ori: nch, t
    # return : n_freq n_frame n_ch
    [M,_] = np.shape(Sig_ori)

    ##stft
    _,_,Zxx0 = signal.stft(Sig_ori[0,:] , nperseg=fft_len , noverlap=lap_len)
    a,b = np.shape(Zxx0)
    Sw = np.zeros((a,b,M) , dtype=complex)
    Sw[:,:,0] = Zxx0
    for i in range(1,M):
        f_list,_,Zxx = signal.stft(Sig_ori[i,:] , nperseg=fft_len , noverlap=lap_len)
        Sw[:,:,i] = Zxx

    return Sw

def Mistft(Sw , fft_len= 2048  ,lap_len = 1024):
    # Sw : n_freq n_frame n_ch
    # return: nch, t
    K = Sw.shape[2]
    ## istft
    _ , tmp = signal.istft(Y[:,:,0], nperseg=fft_len , noverlap=lap_len)
    St_hat = np.zeros((K , len(tmp)))
    St_hat[0,:] = np.real(tmp)
    for i in range(K):
        _ , tmp = signal.istft(Y[:,:,i], nperseg=fft_len , noverlap=lap_len)
        St_hat[i,:] = np.real(tmp)
    return St_hat