from converter import converter
import argparse

def main(args):

    conv = converter()
    conv.convert(imgs_path = args['path'], fps = float(args['fps']), img_format= args['img_format'], output_format= args['output_format'], output_name=args['name'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='converter')   
    parser.add_argument('-p','--path', help='path to the directory containing all images', required=True)
    parser.add_argument('-f', '--fps', help='the frames per second the video should have', required=True)
    parser.add_argument('-if', '--img_format', help='The format of the images (jpg, png, ...)', required=True)
    parser.add_argument('-of', '--output_format', help='The output format of the video (mp4, avi, ...)', required=True)
    parser.add_argument('-n', '--name', help='The output name of the video', required=True)

    args = vars(parser.parse_args())
    main(args)