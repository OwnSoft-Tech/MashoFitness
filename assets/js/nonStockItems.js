
function reloadPage() {
    window.location.reload();
    console.log("reload");
};

function SearchByStockField() {
    let field = document.getElementById('search-by-field').value;
    let value = document.getElementById('search-by-value').value;
    if (field != '' && value != '') {
        $.ajax({
            method: "GET",
            url: "/api/SearchByStockField/",
            data: { "field": field, "value": value },
            success: function (data) {
                // console.log("success on search" + data);
                update_table(data)
            },
            error: function () {
                console.log('error');
            }

        })
    }
};


function update_table(data){
    console.log(data);
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        console.log(elem);
        row = '<tr class="text-left hover:bg-red-200">'+
        '<td class="p-2">'+
            '<div class="float-left hover:text-red-600">'+
                '<span @click="openUpdateModal">'+
                    '<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">'+
                        '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />'+
                    '</svg>'+
                '</span>'+
            '</div>'+
        '</td>'+
        '<td class="p-2">'+elem['nonStock_item_code']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_name']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_unit']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_purchase_price']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_selling_price']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_category']+'</td>'+
        '<td class="p-2">'+elem['nonStock_item_status']+'</td>'+

    '</tr>'
                                    
    all_rows = all_rows + row;
    });
    $('#myTable tbody').html(all_rows);
}



