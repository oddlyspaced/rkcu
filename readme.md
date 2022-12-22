
# RKCU - Royal Kludge Color Utility
Python based command line utility to manage led color profiles on Royal Kludge RK 61 Keyboard.

How to use:

    python rkcu.py <arguments>

Arguments :

    --speed, --sp [1-5]
    # speed of led animation.
    
    --brightness, -br [0-5]
    # brightness of led animation
	
	--sleep, -sl [1-5]
	# 1: 05 Minutes
	# 2: 10 Minutes
	# 3: 20 Minutes
	# 4: 30 Minutes
	# 5: Never Sleep
	
	--rainbow, -rb
	# Set LED color mode to Rainbow
	
	--red, -r 0-255
	# Red value of Color
	
	--green, -g 0-255
	# Green value of Color
	
	--blue, -b 0-255
	# Blue value of Color
	
	--animation, -an "animation_name"
	# List of availaible animations:
	 - neon_stream
	 - ripples_shining
	 - sine_wave
	 - rainbow_routlette
	 - stars_twinkle
	 - layer_upon_layer
	 - rich_and_honored
	 - marquee_effect
	 - rotating_storm
	 - serpentine_horse
	 - retro_snake
	 - diagonal_transformer
	 - ambilight
	 - streamer
	 - steady
	 - breathing
	 - neon
	 - shadow_disappear
	 - flash_away

