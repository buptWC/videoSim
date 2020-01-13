import os


# 接收的参数形如 "network_trace/fixed"
def load_network_trace(network_file_path):
    if not network_file_path.endswith('/'):
        network_file_path += '/'

    network_file_list = os.listdir(network_file_path)
    all_time_record = []
    all_thr_record = []
    for network_file in network_file_list:
        time_record = []
        thr_record = []
        with open(network_file, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip('\n')
                if not line: break
                timestamp, throughput = map(float, line.split())
                time_record.append(timestamp)
                thr_record.append(throughput)
        all_time_record.append(time_record)
        all_thr_record.append(thr_record)
    return all_time_record, all_thr_record


# 接收的参数形如 "video_trace/game"
def load_video_trace(video_file_path):
    if not video_file_path.endswith('/'):
        video_file_path += '/'

    video_file_list = os.listdir(video_file_path)
    bit_count = len(video_file_list)

    all_time_record = []
    all_size_record = []
    all_flag_record = []

    for bit_rate in range(bit_count):
        video_file = video_file_path + 'frame_trace_' + str(bit_rate)
        time_record = []
        size_record = []
        flag_record = []

        with open(video_file, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().strip('\n')
                if not line: break
                timestamp, size, flag = map(float, line.split())
                time_record.append(timestamp)
                size_record.append(size)
                flag_record.append(flag)
        all_time_record.append(time_record)
        all_size_record.append(size_record)
        all_flag_record.append(flag_record)
    return all_time_record, all_size_record, all_flag_record
