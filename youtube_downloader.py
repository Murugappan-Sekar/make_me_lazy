from pytube import YouTube
import logging
# Logger code
logging.basicConfig(
                    filename='ytd_log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG
                )
logger = logging.getLogger('ytd_log')
# 


logger.info("starting script")
src_link_file = "/home/murugappan/Desktop/ytd_src"
storage_loc = "/media/murugappan/MurugappanSekar/songs"
try:
    logger.info("attempting to open source file")
    with open(src_link_file) as src_file:
        logger.info("source file opened")
        for line in src_file:
            try:
                logger.info("attempting to download " + line)
                yt_obj = YouTube(line)
                yt_obj.streams.filter(only_audio=True).first().download(storage_loc)
                logger.info(line + "downloaded")
            except Exception as e:
                logger.error(e)
except Exception as e:
    logger.error(e)
