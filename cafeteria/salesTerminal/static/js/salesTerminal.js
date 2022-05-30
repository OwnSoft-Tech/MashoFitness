
item_name = [];
function addToCart(id) {
    $.ajax({
        url: '/api/salesTerminal/addToCart',
        type: 'GET',
        data: {
            id: id
        },
        success: function (data) {
            CreateRows(data);
            updateCart();
        }
    });

}


function CreateRows(data) {
    if (item_name.includes(data['inventory_item_id']['item_name'])) {
        alert("Item already in cart");
    }
    else {
        item_name.push(data['inventory_item_id']['item_name']);
        $('#myTable').find('tbody').append(
            '<tr class="border-2 text-center">' +
            '<td id="DeleteRow">' +
            '<svg xmlns="http://www.w3.org/2000/svg"' +
            'class="h-5 w-5 hover:border-blue-800 border-2 rounded-md text-red-900 cursor-pointer"' +
            'fill="none" viewBox="0 0 24 24"' +
            'stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round"' +
            'stroke-width="2" d="M6 18L18 6M6 6l12 12" />' +
            '</svg>' +
            '</td>' +
            '<td class="p-1">1</td>' +
            '<td class="p-1">' + data['inventory_item_id']['item_code'] + '</td>' +
            '<td class="p-1 product-name">' + data['inventory_item_id']['item_name'] + '</td>' +
            '<td class="p-1">' + data['inventory_item_id']['item_selling_price'] + '</td>' +
            '<td class="p-1"><span>1</span></td>' +
            '<td class="p-1 inline-flex items-center space-x-1">' +
            '<svg xmlns="http://www.w3.org/2000/svg" class="sub-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6" />' +
            '</svg>' +

            ' <svg xmlns="http://www.w3.org/2000/svg" class="add-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />' +
            '</svg>' +
            '</td>' +
            '<td class="totaldiscount p-1"><input placeholder="0" class="discount w-10"  /></td>' +
            '<td class="price p-1 font-semibold">' + data['inventory_item_id']['item_selling_price'] + '</td>' +
            '</tr>'
        );
    }

}

$(document).ready(function () {
    // code to read selected table row cell data (values).
    $("#myTable").on('click', '.sub-btn', function () {
        // get the current row
        var currentRow = $(this).closest("tr");
        var col4 = currentRow.find("td:eq(4)").text(); // get current row 4thTD
        var count = parseInt(currentRow.find("td:eq(5)").text()) - 1; // get current row 5thTD
        currentRow.find("td:eq(5)").text(count);
        currentRow.find("td:eq(8)").text(count * col4); // get current row 4thTD
        updateCart();
        //  console.log(col4);
    });
    $("#myTable").on('click', '.add-btn', function () {
        // get the current row
        var currentRow = $(this).closest("tr");
        var col4 = currentRow.find("td:eq(4)").text(); // get current row 4thTD
        var count = parseInt(currentRow.find("td:eq(5)").text()) + 1; // get current row 5thTD
        currentRow.find("td:eq(5)").text(count);
        currentRow.find("td:eq(8)").text(count * col4); // get current row 4thTD
        updateCart();
    });

});


(function () {
    "use strict";

    $("table").on("change", "input", function () {
        var row = $(this).closest("tr");
        var discount = parseFloat(row.find(".discount").val());
        var price = parseFloat(row.find(".price").text());
        var total = price - discount;
        row.find(".price").text(total);
        updateCart();
    });
})();

$("#myTable").on("click", "#DeleteRow", function () {
    item_name.pop($(this).closest("tr").find(".product-name").text());
    $(this).closest("tr").remove();
    updateCart();

});

function updateCart() {
    const rows = document.querySelectorAll("table > tbody > tr");
    var total = 0;
    var discount = 0;
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        if (row.querySelectorAll("td > input")[0].value != "") {
            discount += parseFloat(row.querySelectorAll("td > input")[0].value);
        }
        total += parseFloat(row.querySelector(".price").textContent);
    }
    document.getElementById("total-price").innerHTML = total - discount;
    document.getElementById("total-discount").innerHTML = discount;
    document.getElementById("subtotal").innerHTML = total;
    document.getElementById("amount-paid").innerHTML = total - discount;
}


function searchItemInSalesTerminal(value) {
    $.ajax({
        url: '/api/searchItemInSalesTerminal/',
        method: 'GET',
        data: {
            'item_name': value
        },
        success: function (data) {
            $('#item-main-div').empty();
            if (data['Stock']) {
                Object.keys(data['Stock']).forEach(key => {
                    $('#item-main-div').append(
                        '<div onclick="addToCart(' + data['Stock'][key]["id"] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['Stock'][key]['item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' + data['Stock'][key]['item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['Stock'][key]['item_selling_price'] + '</span>' +
                        '<img src=' + data['Stock'][key]['item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
                })

            }
            else if (data['NonStock']) {
                Object.keys(data['NonStock']).forEach(key => {
                $('#item-main-div').append(
                    '<div onclick="addToCart(' + data['NonStock'][key]["id"] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['NonStock'][key]['nonStock_item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' + data['NonStock'][key]['nonStock_item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['NonStock'][key]['nonStock_item_selling_price'] + '</span>' +
                        '<img src=' + data['NonStock'][key]['nonStock_item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
                })
            }
            else {
                // console.log(data);
                Object.keys(data['Both']).forEach(key => {
                $('#item-main-div').append(
                    '<div onclick="addToCart(' + data['Both'][key]['id'] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['Both'][key]['item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' +data['Both'][key]['item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['Both'][key]['item_price'] + '</span>' +
                        '<img src=' + data['Both'][key]['item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
            })
            }
        }
    });
}