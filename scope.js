var x = 5

function scope() {
  var y = 10 + x
  console.log(y)
}
scope()