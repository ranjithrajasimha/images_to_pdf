from PIL import Image
from PIL.ImageQt import ImageQt
import glob

class Image2Pdf:
    def ReadImages(self, img_path):
        # self.images = []
        # for img in glob.glob(dir_path + '/*.jpg'):
        self.image = Image.open(img_path).convert('RGB')

    def SaveToPdf(self, file_path):
        self.image.save(file_path, save_all=True)  

    def GetImages(self):
        return ImageQt(self.image.resize((300, 300)))