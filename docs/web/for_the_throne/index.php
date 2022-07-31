<?php
if(array_key_exists("The_limited_edition_what", $_COOKIE)&&preg_match('/([Oo])reo+/', $_COOKIE["The_limited_edition_what"])){
	$output=('<p style="text-align: center;" >You got it! MAZE{ph0r_7h3_7hr0N3_0r305_c00k135}</p>');
  }else{
	  $output = ("<p style='text-align: center;' >Twist Lick Dunk</p>");
	  setcookie("The_limited_edition_what", 'putithere', time()+300);
  }
  
?>
<!DOCTYPE html>
<html>
    <head>
        <title>The limited edition what? </title>
    </head>
	<style>
		*{
			background-color:  #3B3B3B;
		}
		img {
    display: block;
    margin: 0 auto;
			}
			


	</style>
    <body>
		<main>
			<section style="text-align: center;" class="section">
				<div class="container">
					<h1 style="text-align: center;" class="title">The limited edition what?</h1>
					<h2 class="subtitle">
						<?php
						echo($output);
						?>
					</h2>
				</div>
			</section>
		</main>

		<img class="center" src="https://user-images.githubusercontent.com/74676945/174235505-42652d0b-94c5-4267-a429-fe8bc772f8d5.jpg" alt="">
	</body>
</html>
