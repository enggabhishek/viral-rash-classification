import torch
import os
from torchvision import transforms, models
from PIL import Image
import timm
IMAGE_HEIGHT = 299
IMAGE_WIDTH = 299

#===========================Evaluate the model based on the test dataset=====================
label_map = {'Chicken Pox': 0, 'Measles': 1, 'Monkey Pox': 2}

def getType(id):
    return list(label_map.keys())[list(label_map.values()).index(id)]

def predict_images_class(model_name, image_data):
    model=''
    prediction = ''
    
    transform = transforms.Compose([
    transforms.Resize((IMAGE_WIDTH, IMAGE_HEIGHT)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    if model_name=='resnet50':
        model = models.resnet50(weights=None)
    else:
        model = timm.create_model('nasnetalarge', pretrained=False)
        
    model_name=os.path.join(os.getenv('MODEL_LOC'),model_name,'.keras')
    checkpoint = torch.load(model_name, weights_only=True)
    model.load_state_dict(checkpoint['model_state_dict'])
    eval = model.eval()
    
    image = Image.open(image_data).convert('RGB')
    image = transform(image)
    img = image.unsqueeze(0)
    with torch.no_grad():
        prediction = eval(img)
    predicted_class_index = torch.argmax(prediction).item()
    res = getType(predicted_class_index)
    return res












