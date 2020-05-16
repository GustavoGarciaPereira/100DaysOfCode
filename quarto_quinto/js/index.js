window.addEventListener("load", function(event) {
    
    //setar valores iniciais
    document.querySelector('#fname_r').value = document.querySelector('#vol_r').value
    document.querySelector('#fname_g').value = document.querySelector('#vol_g').value
    document.querySelector('#fname_b').value = document.querySelector('#vol_b').value

    cor(document.querySelector('#vol_r').value,document.querySelector('#vol_g').value,document.querySelector('#vol_b').value)
    
    //le e monitora o valor no input range
    document.querySelector('#vol_r').addEventListener('change',(even)=>{
        document.querySelector('#fname_r').value = document.querySelector('#vol_r').value
        cor(document.querySelector('#vol_r').value,document.querySelector('#vol_g').value,document.querySelector('#vol_b').value)
    
    })

    //le e monitora o valor no input range
    document.querySelector('#vol_g').addEventListener('change',(even)=>{
        document.querySelector('#fname_g').value = document.querySelector('#vol_g').value
        cor(document.querySelector('#vol_r').value,document.querySelector('#vol_g').value,document.querySelector('#vol_b').value)
        
    })

    //le e monitora o valor no input range
    document.querySelector('#vol_b').addEventListener('change',(even)=>{
        document.querySelector('#fname_b').value = document.querySelector('#vol_b').value
        cor(document.querySelector('#vol_r').value,document.querySelector('#vol_g').value,document.querySelector('#vol_b').value)
    })
    
    //função que aplica a cor no quadradro
    function cor(r,g,b){
        document.querySelector('#qua').setAttribute("style", 
        `background-color:rgb(${r},${g},${b});`);

        document.querySelector('.titolos_r').setAttribute("style", 
        `color:rgb(${r},${0},${0});`);

        document.querySelector('.titolos_g').setAttribute("style", 
        `color:rgb(${0},${g},${0});`);

        document.querySelector('.titolos_b').setAttribute("style", 
        `color:rgb(${0},${0},${b});`);
    }
});