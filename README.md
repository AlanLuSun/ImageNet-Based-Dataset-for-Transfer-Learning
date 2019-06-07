# ImageNet-Based-Dataset-for-Transfer-Learning
## 1. Introduction  
- A good dataset is extremely important to comprehensively evaluate the performance of a transfer learning method. However, we can see that in many papers the small-scale datasets such as Office-Caltech 10 and Office 31 are still widely used in experiments relating to the deep transfer networks which require to be trained under large amounts of data. The small-scale dataset will severely restrain the performance of deep transfer networks. Hereby, we hope to standardize this ImageNet based dataset to ease future research on deep transfer neural networks.  
- The authors hope and welcome all of the researchers and readers sharing this passion to participate in enriching this dataset. This ImageNet based dataset could be updated by pulling a request to merge the current version. 

## 2. Features of this dataset
- This dataset currently consists of 6 categories which can be divided into two domains for studying transfer learning, namely {cat, dog, car} and {tiger, wolf, truck}, and has 7,114 images in total. The number of images per category is shown as follows:  
  <img src="./pics/dataset-features.jpg" width="73%" height="73%">
- The image number per category averages 1185 and is with a minimum of 815 and a maximum of 1552.  
- The image samples of each category are shown as below figure.  
  <img src="./pics/dataset.jpg" width="73%" height="73%">

 ## 3. The generation approach of this dataset  
The images are all downloaded from corresponding image node of [ImageNet](http://www.image-net.org/). The detailed information of each image node are listed below

|Category|Detailed Information|  
|--------|--------------------|  
|**Cat**|It refers to the image node of "kitty, kitty-cat, puss, pussy, pussycat", which is under the node of "domestic cat, house cat" in ImageNet. The image urls can be found in [here](http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02122298).|  
|**Dog**|["Eskimo dog, husky"](http://www.image-net.org/synset?wnid=n02109961), [image urls](http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02109961)|  
|**Car**|["racer, race car, racing car"](http://www.image-net.org/synset?wnid=n04037443), [image urls](http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04037443)|  
|**Tiger**|["tiger, Panthera tigris"](http://www.image-net.org/synset?wnid=n02129604), [image urls](http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02129604)|  
|**Wolf**|["white wolf, Arctic wolf, Canis lupus tundrarum"](http://www.image-net.org/synset?wnid=n02114548), [image urls](http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02114548)|  
|**Truck**|["fire engine, fire truck"](http://www.image-net.org/synset?wnid=n03345487), [image urls](http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03345487)|  

## 4. How to use
We provide the interface in [Pytorch](https://pytorch.org/) to conveniently use the above dataset for developing your applications. Merely two steps for setup.
- Firstly, modify the root path of ImageNet based dataset and the folder name of each caterogy in [generate.py](generate.py), and then run 
  ```
  python generate.py
  ```  
  to generate the json files which specify the pairs of image path and the corresponding image label of ground truth.
- Secondly, add the file [generic_dataset.py](generic_dataset.py) to your appication, and import the GenericDataset class to your code. The usage example can be found in [generic_dataset.py](generic_dataset.py).
 

