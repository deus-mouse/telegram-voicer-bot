from pyffmpeg import FFmpeg
import os
from platform import system
# import pytest
from pyffmpeg import FFmpeg
from pyffmpeg.misc import Paths

# inp = 'new.ogg'
# out = 'fff.wav'

# ff = FFmpeg()
#
# output_file = ff.convert(inp, out)
#
# print(output_file)
#


cwd = os.path.dirname(__file__)
print(cwd)
my_pat = os.path.join(cwd, "")
i = "new.ogg"
path = "D:\CodeProjects\PythonProjects\telegram-voicer-bot\new.ogg"

# def test_save_directory():
#
#     """
#     Test to see if save directory is used
#     """
#
#     sav_dir = 'H:\\FakePath'
#     ffmpeg = FFmpeg(sav_dir)
#     if ffmpeg:
#         assert ffmpeg.save_dir == sav_dir
#     else:
#         assert False


def test_convert():

    """
    """

    path = Paths().home_path
    print("path", path)
    out = os.path.join(path, 'newwav.wav')
    print("out", out)
    ff = FFmpeg()
    ff.loglevel = 'info'
    print(f'in and out: {i}, {out}')
    ff.convert(i, out)
    if ff.error:
        if 'Output' in ff.error:
            assert True
        else:
            print(ff.error)
            assert False
    else:
        assert True

# def test_get_ffmpeg_bin():
#
#     home_path = Paths().load_ffmpeg_bin()
#     bin_path = FFmpeg().get_ffmpeg_bin()
#     assert home_path == bin_path

# def test_loglevel():
#     ff = FFmpeg()
#     ff.loglevel = 'fa'
#
#     path = Paths().home_path
#     o = os.path.join(path, 'f.wav')
#
#     opt = ['-i', i, o]
#
#     ff.options(opt)
#     assert ff.loglevel != 'fa'

# def test_options():
#
#     path = Paths().home_path
#     o = os.path.join(path, 'f.wav')
#
#     opt = ['-i', i, o]
#
#     ff = FFmpeg()
#     print(f'in and out: {i}, {o}')
#     ret = ff.options(opt)
#     if ff.error:
#         if 'Output' in ff.error:
#             assert True
#         else:
#             print(ff.error)
#             assert False
#     else:
#         assert True


test_convert()