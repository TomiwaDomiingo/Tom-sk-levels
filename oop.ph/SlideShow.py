class SlideShow:
    def __init__(self):
        self.slides = slides
        self.count = 1

    def viewNextSlide(self):
        self.count += 1

    def play(self):
        while self.count <= self.slides:
         print("Side ", self.current)
          self.viewNextSlide()

slideShow = SlideShow()
slideShow.play()