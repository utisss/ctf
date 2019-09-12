# Shifted Image
* **Event:** BepisCTF (ISSS CTF 09-06-2016)
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **Tools Used:**
    * Java Image I/O

## Background
Any image manipulation library or tool.

## Steps
Through visual inspection and the problem description, we can guess that each column of the image is shifted down some constant number of pixels relative to the previous column, with extra pixels being rolled back up to the top. 

I used the below code to "decrypt" the image:
```java
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ImageUnshift {
    public static void main(String[] args) throws IOException {
        BufferedImage src = ImageIO.read(new File("jumbled.png"));
        BufferedImage dest = new BufferedImage(src.getWidth(), src.getHeight(), BufferedImage.TYPE_INT_RGB);
        
        for(int i = 0; i < src.getWidth(); i++){
            for(int j = 0; j < src.getHeight(); j++){
                
                int newI = i;
                int newJ = (j + (src.getHeight() - 5) * i) % src.getHeight();
                
                dest.setRGB(newI, newJ, src.getRGB(i, j));
            }
        }
        
        ImageIO.write(dest, "png", new File("restored.png"));
    }
}
```

In addition, an image manipulation program such as GIMP or Photoshop can be used to straighten the image to make the image easier to read. Using the fact that the columns are being rolled over, we can stack multiple copies of the image vertically to make straightening the image easier.