# audio_toolbox
 
关于这份toolbox的规范：

## input & output

+ 多通道时域信号一律按照 t , n_channel格式进行输入和输出

+ 多通道频域信号一律按照 n_freq , n_frame , n_channel格式进行输入输出


## function

+ 除了待处理的信号外，所有的参数一律需要有缺省模式，尤其是缺省模式