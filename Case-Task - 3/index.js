const IMAGES = [
    {src: 'https://images.unsplash.com/photo-1726711340699-952d47133b21', alt: 'горы'},
    {src: 'https://images.unsplash.com/photo-1726955179505-556d5e51c192', alt: 'барашки'},
    {src: 'https://images.unsplash.com/photo-1726706805887-0ac0e0d3a721', alt: 'цветы'},
    {src: 'https://images.unsplash.com/photo-1601042879364-f3947d3f9c16', alt: 'город'},
    {src: 'https://images.unsplash.com/photo-1727098044647-5544325689b9', alt: 'касеты'},
]

const slider = document.querySelector('.slider')
const getImages = () => IMAGES.map(({src, alt}) => {
    let img = document.createElement('img')
    img.src = src
    img.alt = alt
    return img
})
slider.append(...getImages())
const slides = Array.from(slider.querySelectorAll('img'))
const slideCount = slides.length
let slideIndex = 0

const prevButton = document.querySelector('.prev-button')
const nextButton = document.querySelector('.next-button')

const counter = document.getElementById('counter')
const getPagination = () => slides.map((_, index) => {
    let div = document.createElement('div')
    div.id = `counterListItem-${index}`
    div.style.width = `${100 / slideCount - 1}%`
    div.style.height = '4px'
    return div
})
counter.append(...getPagination())

const updateSlider = () => {
    slides.forEach((slide, index) => {
        const isCurrentIndex = index === slideIndex
        const listItem = document.getElementById(`counterListItem-${index}`)
        listItem.style.backgroundColor = isCurrentIndex ?  'rgba(0, 0, 0, 0.4)' : 'rgba(0, 0, 0, 0.1)'
        slide.style.display = isCurrentIndex ? 'block' : 'none'
    })
}

prevButton.addEventListener('click', () => {
    slideIndex = (slideIndex - 1 + slideCount) % slideCount
    updateSlider()
});

nextButton.addEventListener('click', () => {
    slideIndex = (slideIndex + 1) % slideCount
    updateSlider()
})

updateSlider()