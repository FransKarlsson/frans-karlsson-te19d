var player = {x: 100, y: 100, size: 20, color: "red", speedX: 0, speedY: 0};
var level = level0;

//skapar en lista med 100 dictionaries
var enemies = [];
var i = 0;
while (i<10) {
  enemies.push({
    x: Math.floor(Math.random() * 800),
    y: Math.floor(Math.random() * 600),
    speed: Math.floor(Math.random() * 5) + 1});
  i += 1;
}

  function update() {
    level();
  }

  function level0() {
    picture(0,0,"canvasAssets/splashScreen.png");
    if (keyboard.enter) {level = level1}
  }


  function level1()
  {
    // ränsar skärmen och renderar bakgrunden
    clearScreen();
    fill("lightBlue");
    picture(0,0,"canvasAssets/background.png");
    


    var i = 0; // renderar alla fiender
    while (i < 10)
    {
      var enemy = enemies[i];
      picture(enemy.x-20, enemy.y-20, "canvasAssets/enemy.png");
      

      // om fiendens x är högre eller lägre än spelarens så försöker fiendan ta sig dit.
      if (enemy.x < player.x) {
        enemy.x += enemy.speed
      } else {
        enemy.x -= enemy.speed
      }
      
      // samma sak som med x axeln fast med y axeln
      if (enemy.y < player.y) {
        enemy.y += enemy.speed
      } else {
        enemy.y -= enemy.speed
      }
      i += 1;
      
      if (distance(enemy,player) < 15) {
        alert('Game Over!');
        stopUpdate();
      }
    } 



    picture(player.x-10, player.y-10, "canvasAssets/player.png");
    player.x += player.speedX
    player.y += player.speedY
    
    // Kontroller. Ändrar hastighet istället för koordinaterna.
    if (keyboard.w)
    {
    	player.speedY -= 2;
    }
    if (keyboard.s)
    {
    	player.speedY += 2;
    }
    if (keyboard.d)
    {
    	player.speedX += 2;
    }
    if (keyboard.a)
    {
    	player.speedX -= 2;
    }
    
    // Logik för friktion, hastigheten ändras alltid med 0.5 i motsatt riktning.
    if (player.speedX > 0)
    {player.speedX -= 0.5}
    if (player.speedX < 0)
    {player.speedX += 0.5}
    if (player.speedY > 0)
    {player.speedY -= 0.5}
    if (player.speedY < 0)
    {player.speedY += 0.5}

    // Logik för maxhastighet, om hastigheten är högre än 30 i någon riktning så hoppar den tillbaka till 30 för bättre kontroll.
    if (player.speedX > 30)
    {player.speedX = 30}
    if (player.speedX < -30)
    {player.speedX = -30}
    if (player.speedY > 30)
    {player.speedY = 30}
    if (player.speedY < -30)
    {player.speedY = -30}
    
    // Kanter, om positionen är utanför spelfönstret så hoppar spelaren tillbaka till kanten.
    if (player.x < 0)
    {player.x = 0}
    if (player.x > 800)
    {player.x = 800}
    if (player.y < 0)
    {player.y = 0}
    if (player.y > 460)
    {player.y = 460}


    
  }



