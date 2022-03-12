class Item {
    constructor(name, label, coordinates) {
        // generate unique id based on date and time
        this.id = '_' + Math.random().toString(36).substr(2, 9);
        this.name = name
        this.label = label
        this.coordinates = coordinates
        this.draggable = false
        this.selected = null
    }

    render(ctx) {
        let image = new Image()
        image.src = base_asset_url + this.name
        image.onload = () => {
            this.image = image
            ctx.drawImage(this.image, this.coordinates.x, this.coordinates.y)
        }
    }

    draw(ctx) {
        ctx.drawImage(this.image, this.coordinates.x, this.coordinates.y)
    }

    move(mouseX, mouseY) {
        this.coordinates.x = mouseX - this.image.width / 2
        this.coordinates.y = mouseY - this.image.height / 2
    }

    asJson() {
        let data = {
            label: this.label,
            x: this.coordinates.x,
            y: this.coordinates.y,
        }
        return JSON.stringify(data)
    }

    asHtml(){
        return `
            <span class="item-name">${this.label}</span>
            <span class="item-coordinates">x: ${this.coordinates.x}, y:${this.coordinates.y}</span>
            <svg onclick="deleteItem('${this.id}')" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
        `
    }
}

class Items {
    static Ball = new Item('ball_32.png', {x: 0, y: 0});
    static Player = new Item('player_32.png', {x: 0, y: 0});
    static Plot = new Item('plot_32.png', {x: 0, y: 0});
    
    constructor(name) {
        this.name = name
    }
}