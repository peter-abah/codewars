// RGB To Hex Conversion
// KATA LINK: https://www.codewars.com/kata/513e08acc600c94f01000001

// The rgb function is incomplete. Complete it so that passing in RGB decimal values 
// will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
// Any values that fall out of that range must be rounded to the closest valid value.

function rgb(r, g, b) {
  const hex = (i) => {
    if (i < 0) i = 0;
    if (i > 255) i = 255;
    return i.toString(16).toUpperCase().padStart(2, '0');
  };
  
  return `${hex(r)}${hex(g)}${hex(b)}`

}