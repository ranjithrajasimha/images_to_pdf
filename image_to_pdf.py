from PIL import Image
import glob

class Image2Pdf:
    def ReadImages(self, dir_path):
        self.images = []
        for img in glob.glob(dir_path + '/*.jpg'):
            self.images.append(Image.open(img).convert('RGB'))

    def SaveToPdf(self, file_path):
        self.images[0].save(file_path+"/AllImages.pdf", save_all=True, append_images=self.images[1:])  

