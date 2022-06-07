<div id="top"></div>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.pinimg.com/originals/72/cd/96/72cd969f8e21be3476277d12d44c791c.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">DeepFashion README-Template</h3>

  <p align="center">
    An awesome project to extract fashion details from image!
    <br />
  </p>
</div>




<!-- ABOUT THE PROJECT -->
<br><br>
## DeepFashion Model Results

* Accuracy on Validation Set : 0.99

<br>

## Model Inference 

* Download Pretrained Model.
```sh
  gdown.download(id="1e9lEjENXJAcNxAOC6yqstXk-c4hgKtNt")
  ```
* Load The Pretrained Model.
```sh
  model = Model()
  model.load_state_dict(torch.load(f="model.pt",map_location="cpu"))
  ```
* Preprocess Single Image.
```sh
  url = "https://m.media-amazon.com/images/I/61gxaHtXARL._UL1500_.jpg"
  url = urllib.urlopen(url)
  img = Image.open(url)
  img = torchvision.transforms.Resize(size=(299,299))(img)
  img = torchvision.transforms.ToTensor()(img)
  img = torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(img)
  img = img
  img = img[None]
  ```
  * Inference over the model.
```sh
  model.eval()
  yneck,ysleeve,ypattern = model(img,eval_=True)
  model.train()
  neck = int(torch.argmax(yneck[0]).data.cpu().numpy())
  sleeve = int(torch.argmax(ysleeve[0]).data.cpu().numpy())
  pattern = int(torch.argmax(ypattern[0]).data.cpu().numpy())
  ```

