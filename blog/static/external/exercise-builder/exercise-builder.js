import { Item, Arrow } from './js/item.js'
import { Field } from './js/field.js'

const template = document.createElement('template')
template.innerHTML = /*html*/`
<style>
#eb__exercice-builder {
    width: 100%;
    display: flex;
    flex-direction: column;
}

#eb__exercice-builder > :first-child {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
}

#eb__items-container {
    padding: 10px;
    margin-left: 10px;
    width: 300px;
    background-color: #ffffff;
    /*box-shadow: 0px 0px 5px rgb(143, 143, 143, 0.5);*/
    border: 1px solid #cccccc;
    border-radius: 5px;
    overflow-y: auto;
    height: 480px
}

h3 {
    margin: 0;
    padding: 0;
}

#eb__items-container .item {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 5px 0;
    border-bottom: 1px solid #e0e0e0;
}

#eb__items-container .item-coordinates {
    padding: 5px;
}

#eb__items-container svg {
    height: 20px;
    width: 20px;
    padding: 5px;
}
#eb__items-container svg:hover {
    height: 20px;
    width: 20px;
    background-color: red;
    color: white;
    border-radius: 100%;
    transition: ease-in-out 0.2s;
    cursor: pointer;
}

canvas {
    border: 1px solid gray;
    height: 500px;
    width: 880px;
    border-radius: 10px;
}

#eb__actions {
    padding: 10px 0;
    display: flex;
    flex-direction: row;
    justify-content: start;
    width: 100%;
}

#image-buttons,
#arrow-buttons {
    padding: 8px;
    display: flex;
}
#image-buttons button,
#arrow-buttons button,
#download {
    margin: 0 10px 0 0;
    padding: 10px;
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    background-color: #f9f9f9;
    cursor: pointer;
    color: gray;
    display: flex;
    flex-direction: row;
    align-items: center;
}

#image-buttons button:hover,
#arrow-buttons button:hover {
    opacity: 0.7;
    transition: 0.2s;
}

.selected {
    color: red;
}
</style>

<div id="eb__exercice-builder">
    <div>
        <canvas width="880" height="500"></canvas>
        <div id="eb__items-container">
            <h3>Items</h3>
            <div id="eb__canvas-items">
            </div>
        </div>
    </div>
    <div id="image-buttons" class="eb__actions">
    </div>
    <div id="arrow-buttons" class="eb__actions">
    </div>
    <div>
        <button id="download">Download</button>
    </div>
</div>
`

class ExerciseBuilder extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.possible_items = {
            images: {
                ball: 'ball_24.png',
                plot: 'plot_24.png',
                player: 'player_24.png'
            },
            arrows: {
                black: {
                    label: 'Black',
                    color: '#000000',
                },
                blue: {
                    label: 'Blue',
                    color: '#4848ff',
                },
                red: {
                    label: 'Red',
                    color: '#f43f3f',
                },
                yellow: {
                    label: 'Yellow',
                    color: '#ffbf32',
                }
            }
        }
    }

    connectedCallback() {
        this.shadowRoot.appendChild(template.content.cloneNode(true));
        let canvas = this.shadowRoot.querySelector('canvas')
        this.field = new Field(canvas, this.shadowRoot)
        this.field.render()
        this.active_arrow = null

        // Create buttons for images
        let image_buttons = this.shadowRoot.querySelector('#image-buttons')
        for (let image in this.possible_items.images) {
            var button = document.createElement('button')
            button.innerHTML = image
            image_buttons.appendChild(button)
            button.addEventListener('click', () => {
                this.addItemToField(image)
            })
        }
        // Create buttons for arrows
        let arrow_buttons = this.shadowRoot.querySelector('#arrow-buttons')
        for (let arrow in this.possible_items.arrows) {
            var button = document.createElement('button')
            let arrow_object = this.possible_items.arrows[arrow]
            button.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" style="height: 20px; width:20px; color: ${arrow_object.color}" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
            `

            arrow_buttons.appendChild(button)
            button.addEventListener('click', () => {
                this.addArrow(arrow, arrow_object.color)
            })
        }

        let download_button = this.shadowRoot.getElementById('download')
        download_button.addEventListener('click', () => {
            this.download()
        })
    }

    addItemToField(name){
        let item = null
        switch (name){
            case 'ball':
                item = new Item('ball_24.png', 'Ball', {x: 0, y: 0})
                break
            case  'plot':
                item = new Item('plot_24.png', 'Plot', {x: 0, y: 0})
                break
            case 'player':
                item = new Item('player_24.png', 'Player', {x: 0, y: 0})
                break
        }
        this.field.addItem(item)
    }

    addArrow(name, color){
        let arrow = new Arrow(name, color)
        this.active_arrow = arrow
        this.field.addArrow(arrow)
    }

    arrowDrawn() {
        this.active_arrow = null
        console.log('drawn !')
    }

    download(){
        this.field.download()
    }

}

window.customElements.define('exercise-builder', ExerciseBuilder)