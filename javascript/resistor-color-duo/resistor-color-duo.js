export const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
];

function colorValue(color) {
  // assuming all color inputs are valid in COLORS
  return COLORS.indexOf(color);
}

export const decodedValue = (colors) => {
  // assuming colors has always more than two elements
  const [color1, color2] = colors;
  return colorValue(color1) * 10 + colorValue(color2);
}