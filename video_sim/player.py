from utils import *
from settings import *


# 这部分应该是对应test函数
# 应该还要抽出一部分用于进行内部计算
class VideoPlayer(object):
    def __init__(self, abr_model, network_trace, video_trace, debug):
        self.abr = abr_model
        self.allNetworkTime, self.allNetworkThr = load_network_trace(network_trace)
        self.allVideoTime, self.allVideoSize, self.allVideoFlag = load_video_trace(video_trace)
        self.debug = debug

        self.totalbitrate = totalBitRate

    def reset(self):
        self.bitrate = initialBitRate                           # 当前码率

        self.physicalTime = 0                                   # 当前物理时间
        self.curDownloadFrame = 0                               # 当前下载的帧序号
        self.newArrivedFrame = 0                                # 当前CDN中最新帧序号

        self.frameReward = 0                                    # 单个视频帧产生的reward
        self.singleFileReward = 0                               # 一个网络轨迹产生的reward
        self.totalFileReward = 0                                # 所有网络轨迹产生的reward

    def playing(self):
        pass

    def isVideoOver(self):
        pass

    def show(self):
        pass

    def result(self):
        pass