Bubble sort


function bubble_sort(the_array){
	for (let i = array.length; i > 0; i--){
		var bool = false;
		for (let j = 0; j < array.length; j++){
			var temp = 0;
			if (array[j] > array[j+1]){
				temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;
				// If inside this condition, then we made a switch
				// Change bool over to true
				bool = true;
			}
		}
		if (bool == false){
			break;
		}else{
			count++;
		}
	}
	return {
		array: the_array,
		counter: counter
	}
}


var array_one = [1,2,3,4,5,6,7,8,9,10]
var array_two = [10,9,8,7,6,5,4,3,2,1]
var array_three = [10,2,8,4,6,7,5,3,9,1]

console.log(bubble_sort(array_one));
console.log(bubble_sort(array_two));
console.log(bubble_sort(array_three))