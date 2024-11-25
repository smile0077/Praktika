const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
    'image5.jpg'
];

let currentIndex = 0;

function updateImage() {
    const imageElement = document.getElementById('currentImage');
    const counterElement = document.getElementById('imageCounter');

    imageElement.src = images[currentIndex];
    counterElement.textContent = Изображение ${currentIndex + 1} из ${images.length};
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length; // Переход к следующему изображению
    updateImage();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length; // Переход к предыдущему изображению
    updateImage();
}

// Инициализация отображения первого изображения
updateImage();
