<script src="https://koda.nu/simple.js">

  var zombie = {x: random(totalWidth),
                y: random(totalHeight),
                speed: random(1,5)};
  
  function update()
  {
   clearScreen();
    
   picture(zombie.x, zombie.y, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Black_Circle.svg/120px-Black_Circle.svg.png");
   
   if (zombie.x < mouse.x)
     zombie.x += zombie.speed;
   else
     zombie.x -= zombie.speed;
   if (zombie.y < mouse.y)
     zombie.y += zombie.speed;
   else zombie.y -= zombie.speed;
    
   if (distance(zombie,mouse) < 5)
   {
    alert("Game over");
    stopUpdate();
   }
     
  }

</script>