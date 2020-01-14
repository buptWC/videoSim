from utils import *
from settings import *


class VideoPlayer(object):
    def __init__(self, abr_model, network_trace, video_trace, debug):
        self.abr = abr_model
        self.allNetworkTime, self.allNetworkThr, self.allFileName = load_network_trace(network_trace)
        self.allVideoTime, self.allVideoSize, self.allVideoFlag = load_video_trace(video_trace)

        self.networkCnt = len(self.allNetworkTime)
        self.debug = debug

        self.totalbitrate = totalBitRate
        assert self.totalbitrate == len(self.allVideoTime)

    def reset(self):
        self.bitrate = initialBitRate                           # 当前码率

        self.physicalTime = 0                                   # 当前物理时间
        self.curDownloadFrame = 0                               # 当前下载的帧序号
        self.newArrivedFrame = 0                                # 当前CDN中最新帧序号
        self.bufferSize = 0                                     # 当前缓冲区内容量

        self.frameReward = 0                                    # 单个视频帧产生的reward
        self.singleFileReward = 0                               # 一个网络轨迹产生的reward
        self.totalFileReward = 0                                # 所有网络轨迹产生的reward

    def playVideo(self):
        while self.networkCnt:
            if self.isNewFrameArrived():
                self.playwithNewFrame()
            else:
                self.playwithoutNewFrame()

            if self.isVideoOver():
                self.networkCnt -= 1

    def isNewFrameArrived(self):
        assert self.bitrate < len(self.allVideoTime)

        arrivedTime = self.allVideoTime[self.bitrate][self.curDownloadFrame]
        return self.physicalTime >= arrivedTime

    def getDownloadTime(self):
        frameSize = self.allVideoSize[self.bitrate][self.curDownloadFrame]
        thrSeq = int(self.physicalTime / 0.5)
        throughput = self.allNetworkThr[self.networkCnt][thrSeq]
        return frameSize / throughput

    def playwithoutNewFrame(self):
        frameStatus = FrameStatus()

        return frameStatus

    def playwithNewFrame(self):
        frameStatus = FrameStatus()

        downloadTime = self.getDownloadTime()
        if self.bufferSize >= downloadTime:
            frameStatus.playingTime = downloadTime
            self.bufferSize = self.bufferSize - downloadTime +
        else:

        return frameStatus

    def isVideoOver(self):
        maxThrTime = self.allNetworkTime[self.networkCnt][-1]
        return self.physicalTime > maxThrTime

    def show(self):
        pass

    def result(self):
        pass