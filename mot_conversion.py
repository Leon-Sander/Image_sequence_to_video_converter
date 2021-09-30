import configparser
from converter import converter
import glob
from tqdm import tqdm

config_parser = configparser.ConfigParser()
conv = converter()

path_train = '' #MOTXX/train/
path_test =  '' #MOTXX/test/
test_train_paths = [path_train, path_test]

for path_t in tqdm(test_train_paths):
    paths = glob.glob(path_t + "*")
    dirs_and_names = []
    for path in paths:
        name = path.replace(path_t, '')
        dirs_and_names.append((path, name))


    for folder in tqdm(dirs_and_names):
        config_path = folder[0] + '/seqinfo.ini'
        name = folder[1]
        imgs_path = folder[0]  + '/img1/'

        config_parser.read(config_path)
        fps = float(config_parser['Sequence']['framerate'])
        img_format = config_parser['Sequence']['imext']
        img_format = img_format.replace('.', '')

        output_dir = folder[0] + '/'

        conv.convert(imgs_path=imgs_path, fps= fps, img_format = img_format, output_name=name, output_dir=output_dir) 